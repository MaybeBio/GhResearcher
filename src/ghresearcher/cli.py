import typer
import os
import sys
from pathlib import Path
from rich.console import Console
from typing import *
from datetime import datetime, timezone, timedelta

from .gh_client import check_auth, run_gh_command
from .tracker import get_user_events, get_received_events, get_org_events, get_repo_events, format_event
from .scraper import build_parse_text, build_parse_view, build_source_catalog_text, split_target
from .searcher import search_github

app = typer.Typer(help="GhResearcher: GitHub Code & Repo Analysis CLI")
console = Console(soft_wrap=not sys.stdout.isatty())

@app.callback()
def main():
    if not check_auth():
        console.print("[red]Error: You are not authenticated with GitHub CLI.[/red]")
        console.print("Please run [bold]gh auth login[/bold] first.")
        raise typer.Exit(code=1)

def parse_date(date_str: str, is_end_of_day: bool = False) -> Optional[datetime]:
    if not date_str:
        return None
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone(timedelta(hours=8)))
        if is_end_of_day:
            dt = dt + timedelta(days=1, seconds=-1)
        return dt
    except ValueError:
        console.print(f"[red]Invalid date format: {date_str}. Expected YYYY-MM-DD.[/red]")
        raise typer.Exit(1)

@app.command()
def monitor(
    target_name: Optional[str] = typer.Argument(None, help="The GitHub user, org, or repo to monitor"),
    users_file: Optional[str] = typer.Option(None, "--file", "-f", help="File containing GitHub targets (one per line)"),
    received: bool = typer.Option(False, "--received", "-r", help="Fetch feed instead of user's own events"),
    is_org: bool = typer.Option(False, "--org", "-O", help="Treat target as an Organization instead of a User"),
    is_repo: bool = typer.Option(False, "--repo", "-R", help="Treat target as a Repository (owner/repo format)"),
    limit: int = typer.Option(30, "--limit", "-l", help="Number of events to fetch per target"),
    since: Optional[str] = typer.Option(None, "--since", help="Filter events on or after this date (YYYY-MM-DD)"),
    until: Optional[str] = typer.Option(None, "--until", help="Filter events on or before this date (YYYY-MM-DD)"),
    expand_commits: bool = typer.Option(False, "--expand-commits", help="Make additional API calls to get commit details for PushEvents if missing")
):
    """
    Track and view the recent events of specific GitHub user(s), organization(s), or repos.
    Supports single target directly or batch targets via file.
    Events from multiple targets are combined into a global chronological timeline.
    """
    targets = []
    if target_name:
        targets.append(target_name)
    
    if users_file:
        if os.path.isfile(users_file):
            with open(users_file, "r") as f:
                lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
                targets.extend(lines)
        else:
            console.print(f"[red]Users file not found: {users_file}[/red]")
            raise typer.Exit(1)
            
    # Deduplicate while preserving order
    targets = list(dict.fromkeys(targets))
            
    if not targets:
        console.print("[red]Please provide a username or a valid --file.[/red]")
        raise typer.Exit(1)

    since_dt = parse_date(since, is_end_of_day=False)
    until_dt = parse_date(until, is_end_of_day=True)

    console.print(f"[bold blue]Fetching events for target(s): {', '.join(targets)}...[/bold blue]\n")
    
    all_events = []
    try:
        from concurrent.futures import ThreadPoolExecutor
        
        # Helper function to fetch events for a single user/org/repo
        def fetch_for_target(t: str):
            if is_repo:
                if received:
                    console.print(f"[yellow]Warning: --received feed ignores repositories ({t}). Skipping.[/yellow]")
                    return []
                return get_repo_events(t, limit=limit, since_dt=since_dt, until_dt=until_dt)
            elif is_org:
                if received:
                    console.print(f"[yellow]Warning: --received feed ignores organizations ({t}). Skipping.[/yellow]")
                    return []
                return get_org_events(t, limit=limit, since_dt=since_dt, until_dt=until_dt)
            elif received:
                return get_received_events(t, limit=limit, since_dt=since_dt, until_dt=until_dt)
            else:
                return get_user_events(t, limit=limit, since_dt=since_dt, until_dt=until_dt)

        # Batch download concurrently or sequentially
        with ThreadPoolExecutor(max_workers=min(len(targets), 10)) as executor:
            results = executor.map(fetch_for_target, targets)
            for res in results:
                if isinstance(res, list):
                    all_events.extend(res)

        if not all_events:
            console.print("[yellow]No events found within the given criteria.[/yellow]")
            return
            
        # Global sort: Descending by created_at
        all_events.sort(key=lambda x: x.get("created_at", ""), reverse=True)
            
        for event in all_events:
            console.print(format_event(event, expand_commits=expand_commits))
            
    except Exception as e:
        console.print(f"[red]Failed to fetch events: {e}[/red]")

def _default_output_name(target: str, source_catalog: bool = False) -> str:
    if source_catalog:
        return "Sources.md"
    parts = [part for part in target.strip().strip("/").split("/") if part]
    if len(parts) > 2:
        return Path(parts[-1]).name or "Context.md"
    return "Context.md"


def _run_parse(
    target: str,
    output: Optional[str],
    view: bool,
    view_mode: str,
    source: bool,
    sources_file: Optional[str],
    clear: bool = False,
) -> None:
    output_name = output or _default_output_name(target, source_catalog=source)

    try:
        if view:
            if not source:
                try:
                    owner, repo, file_path = split_target(target)
                    if file_path is None and view_mode.lower().strip() == "readme":
                        run_gh_command(["repo", "view", f"{owner}/{repo}"], capture_output=False)
                        return
                except Exception:
                    pass

            if source:
                text = build_source_catalog_text(target, sources_file=sources_file)
            else:
                text = build_parse_view(target, view_mode=view_mode, source=None, sources_file=sources_file, compact=clear)
            with console.pager():
                console.print(text)
            return

        if source:
            text = build_source_catalog_text(target, sources_file=sources_file)
        else:
            text = build_parse_text(target, source=None, sources_file=sources_file, compact=clear)

        with open(output_name, "w", encoding="utf-8") as f:
            f.write(text)

        console.print(f"[green]Successfully wrote parsed content to {output_name}[/green]")
    except Exception as e:
        console.print(f"[red]Parse failed: {e}[/red]")


@app.command("parse")
def parse(
    target: str = typer.Argument(..., help="The GitHub repo (owner/repo) or file (owner/repo/path/to/file)"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path"),
    view: bool = typer.Option(False, "--view", help="View in a pager instead of writing to disk"),
    view_mode: str = typer.Option("both", "--view-mode", help="View mode for repositories: both, readme, or tree"),
    source: bool = typer.Option(False, "--source", help="List saved source URLs for the repository"),
    sources_file: Optional[str] = typer.Option(None, "--sources-file", help="JSON file containing extra or overridden source URLs"),
    clear: bool = typer.Option(False, "--clear", "-C", help="Compact tree: show only programming/md files, collapse other files to '...'"),
):
    """
    Parse a repository, file, or source URL into Markdown/text.
    """
    _run_parse(
        target=target,
        output=output,
        view=view,
        view_mode=view_mode,
        source=source,
        sources_file=sources_file,
        clear=clear,
    )


@app.command("scrape")
def scrape(
    target: str = typer.Argument(..., help="Compatibility alias for parse"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path"),
    view: bool = typer.Option(False, "--view", help="View in a pager instead of writing to disk"),
    view_mode: str = typer.Option("both", "--view-mode", help="View mode for repositories: both, readme, or tree"),
    source: bool = typer.Option(False, "--source", help="List saved source URLs for the repository"),
    sources_file: Optional[str] = typer.Option(None, "--sources-file", help="JSON file containing extra or overridden source URLs"),
    clear: bool = typer.Option(False, "--clear", "-C", help="Compact tree: show only programming/md files, collapse other files to '...'"),
):
    """
    Compatibility alias for parse.
    """
    _run_parse(
        target=target,
        output=output,
        view=view,
        view_mode=view_mode,
        source=source,
        sources_file=sources_file,
        clear=clear,
    )

@app.command()
def search(
    item_type: Optional[str] = typer.Argument(None, help="Type to search: repos, code, issues, prs, commits"),
    query: Optional[str] = typer.Argument(None, help="The search query"),
    config: Optional[Path] = typer.Option(None, "--config", "-c", help="Path to YAML search config file"),
    # Common CLI overrides
    limit: int = typer.Option(30, "--limit", "-l", help="Maximum results"),
    sort: Optional[str] = typer.Option(None, "--sort", "-s", help="Sort criteria"),
    order: Optional[str] = typer.Option(None, "--order", "-O", help="Order (asc/desc)")
):
    """
    Search GitHub across multi-domains (repos, code, issues) with full query support.
    Accepts command line arguments or a structured YAML config profile.
    """
    yaml_data = {}
    if config:
        try:
            import yaml
        except ImportError:
            console.print("[red]Error: PyYAML not found! Please run 'pip install PyYAML'.[/red]")
            raise typer.Exit(1)
            
        if not config.is_file():
            console.print(f"[red]Error: Configuration file not found at {config}[/red]")
            raise typer.Exit(1)
            
        with open(config, "r", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f) or {}

    final_item_type = item_type or yaml_data.get("item_type")
    final_query = query or yaml_data.get("query")
    
    if not final_item_type or not final_query:
        console.print("[red]Error: Missing required parameters. Please provide 'item_type' and 'query' either via CLI or YAML config.[/red]")
        raise typer.Exit(1)
        
    # CLI options take precedence over yaml_data if explicitly set
    if limit != 30:
        yaml_data["limit"] = limit
    if "limit" not in yaml_data:
        yaml_data["limit"] = 30
        
    if sort:
        yaml_data["sort"] = sort
    if order:
        yaml_data["order"] = order

    console.print(f"[bold blue]Searching {final_item_type} for '{final_query}' " + (f"(via {config.name})" if config else "") + "...[/bold blue]")
    try:
        search_github(
            item_type=final_item_type,
            query=final_query,
            config=yaml_data
        )
    except Exception as e:
        console.print(f"[red]Search failed: {e}[/red]")

if __name__ == "__main__":
    app()
