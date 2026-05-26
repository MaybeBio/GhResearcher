import base64
import subprocess
import tempfile
from pathlib import Path
from typing import *
from urllib.parse import quote

from .gh_client import run_gh_command
from .source_registry import format_source_catalog

# keep only these extensions
# reomve ".json"/".yaml"/".yml"/".toml"/".ini"/".cfg"/".conf" if we want to exclude config files
# remove ".xml" if we want to exclude xml files
_PROGRAMMING_EXTENSIONS: FrozenSet[str] = frozenset({
    ".py", ".pyx", ".pxd", ".pyi", ".pyw",
    ".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx",
    ".html", ".htm", ".css", ".scss", ".sass", ".less",
    ".java", ".kt", ".kts", ".scala", ".groovy", ".gradle",
    ".c", ".cpp", ".cc", ".cxx", ".h", ".hpp", ".hh", ".hxx",
    ".rs", ".go", ".zig",
    ".rb", ".rake", ".php", ".phtml", ".pl", ".pm", ".lua", ".tcl",
    ".sh", ".bash", ".zsh", ".fish", ".ps1", ".psm1", ".psd1",
    ".swift", ".m", ".mm",
    ".cs", ".fs", ".fsx", ".vb",
    ".r", ".jl", ".ipynb",
    ".hs", ".lhs", ".elm", ".ex", ".exs", ".erl", ".hrl",
    ".clj", ".cljs", ".cljc", ".edn",
    ".dart", ".vue", ".svelte",
    ".xsl", ".xslt", ".svg",
    ".proto", ".avsc", ".thrift",
    ".tf", ".tfvars", ".hcl",
    ".cmake", ".mk", ".meson",
    ".sql", ".psql",
    ".graphql", ".gql",
    ".md", ".mdx", ".rst", ".markdown",
    ".lock",
    ".tex", ".sty", ".cls", ".bib",
})



def get_repo_view(repo_name: str) -> str:
    """
    Get the description and README of a repository using 'gh repo view'.
    """
    try:
        # Note: --json parameters can be added if we want structured data
        output = run_gh_command(["repo", "view", repo_name], capture_output=True)
        return str(output)
    except Exception as e:
        return f"Error fetching repo view: {e}"


def split_target(target: str) -> Tuple[str, str, Optional[str]]:
    """
    Split a GitHub target into owner/repo and an optional file path.
    """
    cleaned = target.strip().strip("/")
    parts = [part for part in cleaned.split("/") if part]
    if len(parts) < 2:
        raise ValueError("Target must look like owner/repo or owner/repo/path/to/file")

    owner, repo = parts[0], parts[1]
    file_path = "/".join(parts[2:]) if len(parts) > 2 else None
    return owner, repo, file_path


def get_repo_metadata(repo_name: str) -> Dict:
    """
    Fetch repository metadata from the GitHub API.
    """
    repo_info = run_gh_command(["api", f"repos/{repo_name}"], capture_output=True)
    if not isinstance(repo_info, dict):
        raise ValueError(f"Unexpected repository metadata response for {repo_name}")
    return repo_info


def get_default_branch(repo_name: str) -> str:
    repo_info = get_repo_metadata(repo_name)
    return repo_info.get("default_branch") or "main"


def get_repo_tree_entries(repo_name: str) -> List[Dict]:
    """
    Fetch a full tree for the repository's default branch without cloning.
    """
    default_branch = get_default_branch(repo_name)
    ref_info = run_gh_command(["api", f"repos/{repo_name}/git/ref/heads/{default_branch}"], capture_output=True)
    if not isinstance(ref_info, dict):
        raise ValueError(f"Unexpected branch ref response for {repo_name}")

    tree_sha = ref_info.get("object", {}).get("sha")
    if not tree_sha:
        raise ValueError(f"Could not resolve tree SHA for {repo_name}@{default_branch}")

    tree_info = run_gh_command(["api", f"repos/{repo_name}/git/trees/{tree_sha}?recursive=1"], capture_output=True)
    if not isinstance(tree_info, dict):
        raise ValueError(f"Unexpected tree response for {repo_name}")

    if tree_info.get("truncated"):
        raise RuntimeError(f"Tree API response truncated for {repo_name}")

    return tree_info.get("tree", [])


def render_tree_from_paths(paths: Iterable[str], root_label: str, compact: bool = False) -> str:
    """
    Render a tree view from a collection of repository paths.
    When compact=True, only programming/md files are shown per directory;
    all other files at that level are collapsed into a single '...' entry.
    """
    trie: Dict[str, Dict] = {}

    for raw_path in paths:
        if not raw_path:
            continue
        node = trie
        for part in Path(raw_path).parts:
            node = node.setdefault(part, {})

    lines = [f"{root_label}/"]

    def walk(node: Dict[str, Dict], prefix: str = "") -> None:
        if compact:
            dirs: Dict[str, Dict] = {}
            interesting_files: Dict[str, Dict] = {}
            other_count = 0

            for name, child in node.items():
                if child:
                    dirs[name] = child
                elif Path(name).suffix.lower() in _PROGRAMMING_EXTENSIONS:
                    interesting_files[name] = child
                else:
                    other_count += 1

            display = (
                sorted(dirs.items(), key=lambda item: item[0].lower())
                + sorted(interesting_files.items(), key=lambda item: item[0].lower())
            )
            if other_count > 0:
                display.append(("...", {}))

            for index, (name, child) in enumerate(display):
                is_last = index == len(display) - 1
                connector = "└── " if is_last else "├── "
                lines.append(f"{prefix}{connector}{name}")
                if child:
                    walk(child, prefix + ("    " if is_last else "│   "))
        else:
            items = sorted(node.items(), key=lambda item: (len(item[1]) == 0, item[0].lower()))
            for index, (name, child) in enumerate(items):
                is_last = index == len(items) - 1
                connector = "└── " if is_last else "├── "
                lines.append(f"{prefix}{connector}{name}")
                if child:
                    walk(child, prefix + ("    " if is_last else "│   "))

    walk(trie)
    return "\n".join(lines)


def generate_tree_from_clone(repo_name: str, compact: bool = False) -> str:
    """
    Generate an ASCII tree by shallow-cloning the repository into a temporary directory.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_dir = Path(tmpdir) / repo_name.split("/")[-1]
        subprocess.run(
            ["git", "clone", "--depth", "1", f"https://github.com/{repo_name}.git", str(repo_dir)],
            capture_output=True,
            check=True,
        )

        ignore_dirs = {".git", "build", "vendor", "__pycache__", "node_modules"}

        def list_entries(path: Path) -> List[Path]:
            entries = []
            for entry in sorted(path.iterdir(), key=lambda item: (not item.is_dir(), item.name)):
                if entry.name in ignore_dirs or entry.name.startswith("."):
                    continue
                entries.append(entry)
            return entries

        lines = [f"{repo_dir.name}/"]

        def render(path: Path, prefix: str = "") -> None:
            entries = list_entries(path)
            if compact:
                dirs: List[Path] = []
                interesting_files: List[Path] = []
                other_count = 0

                for entry in entries:
                    if entry.is_dir():
                        dirs.append(entry)
                    elif entry.suffix.lower() in _PROGRAMMING_EXTENSIONS:
                        interesting_files.append(entry)
                    else:
                        other_count += 1

                display: List[Tuple[str, bool, Optional[Path]]] = []
                for d in dirs:
                    display.append((d.name, True, d))
                for f in interesting_files:
                    display.append((f.name, False, f))
                if other_count > 0:
                    display.append(("...", False, None))

                for index, (name, is_dir, child_path) in enumerate(display):
                    is_last = index == len(display) - 1
                    connector = "└── " if is_last else "├── "
                    lines.append(f"{prefix}{connector}{name}")
                    if is_dir and child_path is not None:
                        render(child_path, prefix + ("    " if is_last else "│   "))
            else:
                for index, entry in enumerate(entries):
                    is_last = index == len(entries) - 1
                    connector = "└── " if is_last else "├── "
                    lines.append(f"{prefix}{connector}{entry.name}")
                    if entry.is_dir():
                        render(entry, prefix + ("    " if is_last else "│   "))

        render(repo_dir)
        return "\n".join(lines)


def build_repository_context(repo_name: str, compact: bool = False) -> str:
    """
    Build the full repository context: gh repo view plus a tree derived from GitHub API.
    """
    repo_view = get_repo_view(repo_name)
    try:
        tree_entries = get_repo_tree_entries(repo_name)
        tree_paths = [entry.get("path", "") for entry in tree_entries if entry.get("path")]
        tree_output = render_tree_from_paths(tree_paths, repo_name, compact=compact)
        tree_source = "GitHub API"
    except Exception:
        tree_output = generate_tree_from_clone(repo_name, compact=compact)
        tree_source = "shallow clone fallback"

    content = [
        f"# Repository: {repo_name}\n",
        repo_view,
        "\n---\n",
        f"## Repository Structure ({tree_source})\n",
        "```\n" + tree_output + "\n```\n",
    ]
    return "\n".join(content)


def get_file_content(repo_name: str, file_path: str) -> str:
    """
    Fetch a single file's raw content from GitHub without cloning.
    """
    default_branch = get_default_branch(repo_name)
    encoded_path = quote(file_path.lstrip("/"), safe="/")
    file_info = run_gh_command(
        ["api", f"repos/{repo_name}/contents/{encoded_path}?ref={default_branch}"],
        capture_output=True,
    )
    if not isinstance(file_info, dict):
        raise ValueError(f"Unexpected file content response for {repo_name}/{file_path}")

    if file_info.get("type") == "file" and file_info.get("encoding") == "base64":
        content = file_info.get("content", "")
        decoded = base64.b64decode(content.encode("utf-8")).decode("utf-8", errors="replace")
        return decoded

    if file_info.get("download_url"):
        return f"Error: unable to decode file content for {repo_name}/{file_path}; download_url={file_info['download_url']}"

    return str(file_info)


def resolve_source_url(source_name: str, repo_name: str, sources_file: Optional[str] = None) -> str:
    """
    Build a reader-view URL for a supported source site.
    """
    from .source_registry import load_source_templates

    source_templates = load_source_templates(sources_file)
    source_key = source_name.lower().strip()
    template = source_templates.get(source_key)
    if not template:
        raise ValueError(f"Unsupported source '{source_name}'. Expected one of: {', '.join(sorted(source_templates))}")

    owner, repo, file_path = split_target(repo_name)
    if file_path:
        raise ValueError("--source currently only supports owner/repo targets")

    return template.format(owner=owner, repo=repo)


def build_file_context(repo_name: str, file_path: str) -> str:
    """
    Build a file-focused context block.
    """
    content = get_file_content(repo_name, file_path)
    return content


def build_parse_text(target: str, source: Optional[str] = None, sources_file: Optional[str] = None, compact: bool = False) -> str:
    """
    Build the text that parse should render or save.
    """
    owner, repo, file_path = split_target(target)
    repo_name = f"{owner}/{repo}"

    if source:
        return resolve_source_url(source, repo_name, sources_file=sources_file)

    if file_path:
        return build_file_context(repo_name, file_path)

    return build_repository_context(repo_name, compact=compact)


def build_parse_view(target: str, view_mode: str = "both", source: Optional[str] = None, sources_file: Optional[str] = None, compact: bool = False) -> str:
    """
    Build text for pager display. View mode controls whether README, tree, or both are shown.
    """
    owner, repo, file_path = split_target(target)
    repo_name = f"{owner}/{repo}"

    if source:
        return resolve_source_url(source, repo_name, sources_file=sources_file)

    if file_path:
        return build_file_context(repo_name, file_path)

    normalized_mode = view_mode.lower().strip()
    if normalized_mode == "readme":
        return get_repo_view(repo_name)
    if normalized_mode == "tree":
        try:
            tree_entries = get_repo_tree_entries(repo_name)
            tree_paths = [entry.get("path", "") for entry in tree_entries if entry.get("path")]
            return render_tree_from_paths(tree_paths, repo_name, compact=compact)
        except Exception:
            return generate_tree_from_clone(repo_name, compact=compact)

    return build_repository_context(repo_name, compact=compact)


def build_source_catalog_text(target: str, sources_file: Optional[str] = None) -> str:
    """
    Build a catalog of saved source URLs for a repository target.
    """
    owner, repo, file_path = split_target(target)
    if file_path:
        raise ValueError("--source catalog is only supported for repository targets, not file targets")

    repo_name = f"{owner}/{repo}"
    return format_source_catalog(repo_name, sources_file=sources_file)

def scrape_repository(repo_name: str, output_file: str = "Context.md"):
    """
    Backwards-compatible wrapper that writes the parsed repository context to disk.
    """
    content = build_repository_context(repo_name)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_file
