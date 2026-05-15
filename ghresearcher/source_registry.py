import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


DEFAULT_SOURCE_ENTRIES: List[Dict[str, Any]] = [
    {"name": "deepwiki", "kind": "template", "url": "https://deepwiki.com/{owner}/{repo}"},
    {"name": "zreadai", "kind": "template", "url": "https://zread.ai/{owner}/{repo}"},
    {"name": "readmex", "kind": "template", "url": "https://readmex.com/{owner}/{repo}"},
    {"name": "gitdiagram", "kind": "template", "url": "https://gitdiagram.com/{owner}/{repo}"},
]


def _normalize_source_entry(entry: dict) -> Optional[Dict[str, Any]]:
    name = str(entry.get("name", "")).strip().lower()
    kind = str(entry.get("kind", "template")).strip().lower() or "template"
    description = str(entry.get("description", "")).strip()

    if not name:
        return None

    if kind == "fixed":
        url = str(entry.get("url", "")).strip()
        if not url:
            return None
        return {
            "name": name,
            "kind": "fixed",
            "url": url,
            "description": description,
        }

    url = str(entry.get("url", "")).strip()
    if not url:
        return None
    return {
        "name": name,
        "kind": "template",
        "url": url,
        "description": description,
    }


def _entry_to_url(entry: Dict[str, Any], owner: str, repo: str) -> str:
    url = str(entry.get("url", "")).strip()
    if entry.get("kind") == "fixed":
        return url
    return url.format(owner=owner, repo=repo)


def _load_payload_entries(payload: Any) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []

    if isinstance(payload, dict) and "sources" in payload:
        source_items = payload.get("sources", [])
        if not isinstance(source_items, list):
            raise ValueError("sources.json must contain a list under 'sources'")
        for entry in source_items:
            if isinstance(entry, dict):
                normalized = _normalize_source_entry(entry)
                if normalized:
                    entries.append(normalized)
        return entries

    if isinstance(payload, list):
        for entry in payload:
            if isinstance(entry, dict):
                normalized = _normalize_source_entry(entry)
                if normalized:
                    entries.append(normalized)
        return entries

    if isinstance(payload, dict):
        for name, value in payload.items():
            if not name:
                continue
            if isinstance(value, dict):
                candidate = dict(value)
                candidate.setdefault("name", name)
                normalized = _normalize_source_entry(candidate)
                if normalized:
                    entries.append(normalized)
                continue

            if isinstance(value, str):
                text = value.strip()
                if not text:
                    continue
                candidate = {"name": name, "kind": "template" if "{owner}" in text or "{repo}" in text else "fixed"}
                candidate["url"] = text
                normalized = _normalize_source_entry(candidate)
                if normalized:
                    entries.append(normalized)
        return entries

    raise ValueError("Unsupported sources.json format")


def load_source_entries(sources_file: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Load source entries from an optional JSON file and merge them with built-ins.
    """
    entries: Dict[str, Dict[str, Any]] = {entry["name"]: dict(entry) for entry in DEFAULT_SOURCE_ENTRIES}

    if not sources_file:
        default_path = Path.cwd() / "sources.json"
        if not default_path.is_file():
            return list(entries.values())
        sources_path = default_path
    else:
        sources_path = Path(sources_file).expanduser()

    if not sources_path.is_file():
        raise FileNotFoundError(f"Sources file not found: {sources_path}")

    payload = json.loads(sources_path.read_text(encoding="utf-8"))
    for entry in _load_payload_entries(payload):
        entries[entry["name"]] = entry

    return list(entries.values())


def load_source_templates(sources_file: Optional[str] = None) -> Dict[str, str]:
    """
    Load source templates from an optional JSON file and merge them with built-ins.

    Supported JSON shapes:
    - {"sources": [{"name": "deepwiki", "url": "..."}, ...]}
    - [{"name": "deepwiki", "url": "..."}, ...]
    - {"deepwiki": "https://...", "zreadai": "https://..."}
    """
    templates: Dict[str, str] = {}
    for entry in load_source_entries(sources_file):
        if entry.get("kind") == "template":
            templates[entry["name"]] = str(entry.get("url", "")).strip()
    return templates


def list_source_urls(repo_name: str, sources_file: Optional[str] = None) -> List[Dict[str, str]]:
    """
    Return resolved URLs for saved sources for a repository.
    """
    owner, repo = repo_name.split("/", 1)
    resolved: List[Dict[str, str]] = []

    for entry in load_source_entries(sources_file):
        resolved.append(
            {
                "name": str(entry.get("name", "")).strip(),
                "kind": str(entry.get("kind", "template")).strip(),
                "url": _entry_to_url(entry, owner, repo),
                "description": str(entry.get("description", "")).strip(),
            }
        )

    return resolved


def format_source_catalog(repo_name: str, sources_file: Optional[str] = None) -> str:
    """
    Format a repository source catalog for display.
    """
    entries = list_source_urls(repo_name, sources_file=sources_file)
    lines = [f"# Saved Sources for {repo_name}", ""]

    for index, entry in enumerate(entries, start=1):
        description = f" - {entry['description']}" if entry.get("description") else ""
        lines.append(f"{index}. {entry['name']} [{entry['kind']}] {description}".rstrip())
        lines.append(f"   {entry['url']}")
        lines.append("")

    if len(entries) == 0:
        lines.append("No saved sources found.")

    return "\n".join(lines).rstrip() + "\n"
