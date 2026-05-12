from typing import List, Optional
from rich.console import Console
from .gh_client import run_gh_command

console = Console()

def search_github(
    item_type: str,
    query: str,
    limit: int = 30,
    sort: Optional[str] = None,
    order: Optional[str] = "desc",
    match: Optional[str] = None,
    language: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    extension: Optional[str] = None,
    filename: Optional[str] = None,
    topic: Optional[str] = None
):
    """
    Execute gh search for different item types (repos, code, issues, etc.).
    """
    cmd = ["search", item_type, query]
    
    cmd.extend(["--limit", str(limit)])
    
    if sort and item_type not in ('code'):
        cmd.extend(["--sort", sort])
    if order and item_type not in ('code'):
        cmd.extend(["--order", order])
    if match:
        cmd.extend(["--match", match])
    if language:
        cmd.extend(["--language", language])
    if owner:
        cmd.extend(["--owner", owner])
    if repo:
        cmd.extend(["--repo", repo])
    if topic and item_type == 'repos':
        cmd.extend(["--topic", topic])
    if extension and item_type == 'code':
        cmd.extend(["--extension", extension])
    if filename and item_type == 'code':
        cmd.extend(["--filename", filename])
        
    console.print(f"[dim]Running command: gh {' '.join(cmd)}[/dim]")
    
    output = run_gh_command(cmd, capture_output=True)
    if isinstance(output, str):
        # Already formatted string from gh CLI standard non-json output
        console.print(output)
    else:
        # JSON output
        console.print(output)
