import typer
import os
from rich.console import Console
from typing import *
from datetime import datetime, timezone, timedelta

from .gh_client import check_auth
from .tracker import get_user_events, get_received_events, get_org_events, get_repo_events, format_event
from .scraper import scrape_repository
from .searcher import search_github

app = typer.Typer(help="GhResearcher: GitHub Code & Repo Analysis CLI")
console = Console()

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

@app.command()
def scrape(
    repo: str = typer.Argument(..., help="The repository to scrape (e.g. 'owner/repo')"),
    output: str = typer.Option("Context.md", "--output", "-o", help="Output Markdown file")
):
    """
    Scrape a repository's README and directory structure into a single context file.
    """
    console.print(f"[bold blue]Scraping repository {repo}...[/bold blue]")
    try:
        out_file = scrape_repository(repo, output_file=output)
        console.print(f"[green]Successfully scraped Context to {out_file}[/green]")
    except Exception as e:
        console.print(f"[red]Scraping failed: {e}[/red]")

@app.command()
def search(
    item_type: str = typer.Argument(..., help="Type to search: repos, code, issues, prs, commits, users"),
    query: str = typer.Argument(..., help="The search query"),
    limit: int = typer.Option(30, "--limit", "-l", help="Maximum results"),
    sort: Optional[str] = typer.Option(None, "--sort", "-s", help="Sort criteria"),
    order: Optional[str] = typer.Option("desc", "--order", "-O", help="Order (asc/desc)"),
    language: Optional[str] = typer.Option(None, "--language", "-L", help="Filter by language"),
    topic: Optional[str] = typer.Option(None, "--topic", "-t", help="Filter by topic (repos only)"),
    match: Optional[str] = typer.Option(None, "--match", "-m", help="Match specific fields")
):
    """
    Search GitHub across multi-domains (repos, code, issues) with full query support.
    """
    console.print(f"[bold blue]Searching {item_type} for '{query}'...[/bold blue]")
    try:
        search_github(
            item_type=item_type,
            query=query,
            limit=limit,
            sort=sort,
            order=order,
            language=language,
            topic=topic,
            match=match
        )
    except Exception as e:
        console.print(f"[red]Search failed: {e}[/red]")

if __name__ == "__main__":
    app()
