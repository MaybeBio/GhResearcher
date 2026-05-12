import os
import shutil
import tempfile
import subprocess
from pathlib import Path
from .gh_client import run_gh_command

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

def generate_tree(dir_path: Path, ignore_dirs=None) -> str:
    """
    Generate a simple ascii tree representation of the directory.
    """
    if ignore_dirs is None:
        ignore_dirs = {'.git', 'build', 'vendor', '__pycache__', 'node_modules'}
        
    tree_str = []
    
    def _walk(current_path: Path, prefix: str = ""):
        try:
            entries = sorted(list(current_path.iterdir()), key=lambda e: (not e.is_dir(), e.name))
        except PermissionError:
            return
            
        # Filter entries
        entries = [e for e in entries if e.name not in ignore_dirs and not e.name.startswith('.')]
        
        for i, entry in enumerate(entries):
            is_last = (i == len(entries) - 1)
            connector = "└── " if is_last else "├── "
            tree_str.append(f"{prefix}{connector}{entry.name}")
            
            if entry.is_dir():
                extension = "    " if is_last else "│   "
                _walk(entry, prefix + extension)

    tree_str.append(dir_path.name + "/")
    _walk(dir_path)
    return "\n".join(tree_str)

def scrape_repository(repo_name: str, output_file: str = "Context.md"):
    """
    Scrape a repository by getting its README and optionally its shallow structure.
    Save the combined result to a Markdown file.
    """
    content = []
    
    # 1. Get Repo View (Description + README)
    content.append(f"# Repository: {repo_name}\n")
    repo_view = get_repo_view(repo_name)
    content.append(repo_view)
    content.append("\n---\n")
    
    # 2. Shallow Clone for Structure
    content.append(f"## Repository Structure\n")
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        repo_dir = tmp_path / repo_name.split('/')[-1]
        
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", f"https://github.com/{repo_name}.git", str(repo_dir)],
                capture_output=True,
                check=True
            )
            tree_output = generate_tree(repo_dir)
            content.append("```\n" + tree_output + "\n```\n")
        except subprocess.CalledProcessError as e:
            content.append(f"Error cloning repository: {e}")
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(content))
        
    return output_file
