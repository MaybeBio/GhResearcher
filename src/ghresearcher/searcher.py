from typing import *
import sys
from rich.console import Console
from .gh_client import run_gh_command

console = Console(soft_wrap=not sys.stdout.isatty())

def search_github(item_type: str, query: str, config: dict):
    """
    Execute gh search for different item types (repos, code, issues, etc.).
    Maps all keys in the YAML config directly to gh CLI flags.
    """
    # Explicitly avoid processing 'item_type' and 'query' as flags
    cmd = ["search", item_type, query]
    
    # Process dynamically
    for key, value in config.items():
        if key in ("item_type", "query"):
            continue
        
        # Convert snake_case to kebab-case (e.g. author_name -> author-name)
        flag = f"--{key.replace('_', '-')}"
        
        if isinstance(value, bool):
            # For GH CLI boolean flags, --flag=true or --flag=false is the safest syntax
            cmd.append(f"{flag}={str(value).lower()}")
        elif isinstance(value, (list, tuple)):
            # Join lists with commas (e.g. json fields)
            cmd.extend([flag, ",".join(str(v) for v in value)])
        elif value is not None:
            cmd.extend([flag, str(value)])
            
    console.print(f"[dim]Running command: gh {' '.join(cmd)}[/dim]")
    
    output = run_gh_command(cmd, capture_output=True)
    if isinstance(output, str):
        console.print(output)
    else:
        # JSON output (if --json was provided)
        console.print(output)
