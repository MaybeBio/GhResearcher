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
    # ── Output / formatting ──
    web: Optional[bool] = typer.Option(None, "--web", "-w", help="Open the search query in the web browser"),
    json: Optional[str] = typer.Option(None, "--json", help="Output JSON with the specified fields (comma-separated)"),
    jq: Optional[str] = typer.Option(None, "--jq", help="Filter JSON output using a jq expression"),
    template: Optional[str] = typer.Option(None, "--template", help="Format JSON output using a Go template"),
    # ── Controls ──
    limit: Optional[int] = typer.Option(None, "--limit", "-l", help="Maximum number of results [default: 30]"),
    sort: Optional[str] = typer.Option(None, "--sort", "-s", help="Sort criteria"),
    order: Optional[str] = typer.Option(None, "--order", "-O", help="Order of results: asc|desc"),
    # ── Common filters ──
    owner: Optional[str] = typer.Option(None, "--owner", "-o", help="Filter on repository owner"),
    repo: Optional[str] = typer.Option(None, "--repo", "-r", help="Filter on repository (owner/repo)"),
    language: Optional[str] = typer.Option(None, "--language", "-L", help="Filter by programming language"),
    visibility: Optional[str] = typer.Option(None, "--visibility", help="Filter by visibility: public|private|internal"),
    match: Optional[str] = typer.Option(None, "--match", help="Restrict search to specific field"),
    # ── Repository filters ──
    topic: Optional[str] = typer.Option(None, "--topic", "-t", help="Filter on repository topic"),
    license: Optional[str] = typer.Option(None, "--license", help="Filter by license type"),
    stars: Optional[str] = typer.Option(None, "--stars", help="Filter on number of stars (e.g. '>=100')"),
    forks: Optional[str] = typer.Option(None, "--forks", help="Filter on number of forks (e.g. '>=10')"),
    size: Optional[str] = typer.Option(None, "--size", help="Filter on size range in KB (e.g. '5000..10000')"),
    created: Optional[str] = typer.Option(None, "--created", help="Filter on created date (e.g. '>=2023-01-01')"),
    updated: Optional[str] = typer.Option(None, "--updated", help="Filter on last updated date"),
    archived: Optional[str] = typer.Option(None, "--archived", help="Filter based on archived state: true|false"),
    include_forks: Optional[str] = typer.Option(None, "--include-forks", help="Include forks: false|true|only"),
    good_first_issues: Optional[str] = typer.Option(None, "--good-first-issues", help="Filter on number of 'good first issue' labels"),
    help_wanted_issues: Optional[str] = typer.Option(None, "--help-wanted-issues", help="Filter on number of 'help wanted' labels"),
    number_topics: Optional[str] = typer.Option(None, "--number-topics", help="Filter on number of topics"),
    followers: Optional[str] = typer.Option(None, "--followers", help="Filter on number of followers"),
    # ── Code filters ──
    extension: Optional[str] = typer.Option(None, "--extension", "-e", help="Filter on file extension"),
    filename: Optional[str] = typer.Option(None, "--filename", "-f", help="Filter on filename"),
    # ── Issue / PR filters ──
    label: Optional[str] = typer.Option(None, "--label", help="Filter on label"),
    state: Optional[str] = typer.Option(None, "--state", help="Filter by state: open|closed"),
    author: Optional[str] = typer.Option(None, "--author", help="Filter by author"),
    assignee: Optional[str] = typer.Option(None, "--assignee", help="Filter by assignee"),
    mentions: Optional[str] = typer.Option(None, "--mentions", help="Filter by @mentions"),
    milestone: Optional[str] = typer.Option(None, "--milestone", help="Filter by milestone title"),
    comments: Optional[str] = typer.Option(None, "--comments", help="Filter on number of comments (e.g. '>100')"),
    no_assignee: Optional[bool] = typer.Option(None, "--no-assignee", help="Filter on missing assignee"),
    no_label: Optional[bool] = typer.Option(None, "--no-label", help="Filter on missing label"),
    no_milestone: Optional[bool] = typer.Option(None, "--no-milestone", help="Filter on missing milestone"),
    no_project: Optional[bool] = typer.Option(None, "--no-project", help="Filter on missing project"),
    include_prs: Optional[bool] = typer.Option(None, "--include-prs", help="Include pull requests in results"),
    locked: Optional[bool] = typer.Option(None, "--locked", help="Filter on locked conversation status"),
    closed: Optional[str] = typer.Option(None, "--closed", help="Filter on closed date (e.g. '>=2023-01-01')"),
    interactions: Optional[str] = typer.Option(None, "--interactions", help="Filter on number of reactions and comments"),
    reactions: Optional[str] = typer.Option(None, "--reactions", help="Filter on number of reactions"),
    app: Optional[str] = typer.Option(None, "--app", help="Filter by GitHub App author"),
    commenter: Optional[str] = typer.Option(None, "--commenter", help="Filter based on comments by user"),
    involves: Optional[str] = typer.Option(None, "--involves", help="Filter based on involvement of user"),
    project: Optional[str] = typer.Option(None, "--project", help="Filter on project board (owner/number)"),
    team_mentions: Optional[str] = typer.Option(None, "--team-mentions", help="Filter based on team mentions"),
    # ── PR-only filters ──
    draft: Optional[bool] = typer.Option(None, "--draft", help="Filter based on draft state"),
    merged: Optional[bool] = typer.Option(None, "--merged", help="Filter based on merged state"),
    base: Optional[str] = typer.Option(None, "--base", "-B", help="Filter on base branch name"),
    head: Optional[str] = typer.Option(None, "--head", "-H", help="Filter on head branch name"),
    checks: Optional[str] = typer.Option(None, "--checks", help="Filter by check status: pending|success|failure"),
    review: Optional[str] = typer.Option(None, "--review", help="Filter by review status: none|required|approved|changes_requested"),
    review_requested: Optional[str] = typer.Option(None, "--review-requested", help="Filter on requested reviewer"),
    reviewed_by: Optional[str] = typer.Option(None, "--reviewed-by", help="Filter on user who reviewed"),
    merged_at: Optional[str] = typer.Option(None, "--merged-at", help="Filter on merged date (e.g. '>=2023-01-01')"),
    # ── Commit filters ──
    committer: Optional[str] = typer.Option(None, "--committer", help="Filter by committer"),
    hash: Optional[str] = typer.Option(None, "--hash", help="Filter by commit hash"),
    merge: Optional[bool] = typer.Option(None, "--merge", help="Filter on merge commits"),
    author_date: Optional[str] = typer.Option(None, "--author-date", help="Filter on authored date"),
    author_email: Optional[str] = typer.Option(None, "--author-email", help="Filter on author email"),
    author_name: Optional[str] = typer.Option(None, "--author-name", help="Filter on author name"),
    committer_date: Optional[str] = typer.Option(None, "--committer-date", help="Filter on committed date"),
    committer_email: Optional[str] = typer.Option(None, "--committer-email", help="Filter on committer email"),
    committer_name: Optional[str] = typer.Option(None, "--committer-name", help="Filter on committer name"),
    parent: Optional[str] = typer.Option(None, "--parent", help="Filter by parent hash"),
    tree: Optional[str] = typer.Option(None, "--tree", help="Filter by tree hash"),
):
    """
    Search GitHub across multi-domains (repos, code, issues, prs, commits) with full query support.

    Accepts command line arguments, a structured YAML config profile, or a combination of both.
    CLI flags always take precedence over YAML config values.

    Examples:
        ghresearcher search repos "LLM agent" -L Python -t artificial-intelligence -s stars -l 20
        ghresearcher search code "TODO" -r MaybeBio/GhResearcher -f "*.py" -e py
        ghresearcher search prs "fix bug" -o microsoft --merged
        ghresearcher search --config examples/search_ai_repos.yaml
    """
    yaml_data: dict = {}
    if config:
        try:
            import yaml as _yaml
        except ImportError:
            console.print("[red]Error: PyYAML not found! Please run 'pip install PyYAML'.[/red]")
            raise typer.Exit(1)

        if not config.is_file():
            console.print(f"[red]Error: Configuration file not found at {config}[/red]")
            raise typer.Exit(1)

        with open(config, "r", encoding="utf-8") as f:
            yaml_data = _yaml.safe_load(f) or {}

    # ── Collect CLI overrides ─────────────────────────────────────
    # Only include parameters explicitly set by the user (non-None).
    _cli_param_names = [
        "web", "json", "jq", "template",
        "limit", "sort", "order",
        "owner", "repo", "language", "visibility", "match",
        "topic", "license", "stars", "forks", "size", "created", "updated",
        "archived", "include_forks", "good_first_issues", "help_wanted_issues",
        "number_topics", "followers",
        "extension", "filename",
        "label", "state", "author", "assignee", "mentions", "milestone",
        "comments", "no_assignee", "no_label", "no_milestone", "no_project",
        "include_prs", "locked", "closed", "interactions", "reactions",
        "app", "commenter", "involves", "project", "team_mentions",
        "draft", "merged", "base", "head", "checks", "review",
        "review_requested", "reviewed_by", "merged_at",
        "committer", "hash", "merge", "author_date", "author_email",
        "author_name", "committer_date", "committer_email", "committer_name",
        "parent", "tree",
    ]
    cli_overrides: dict = {}
    _frame = locals()
    for pn in _cli_param_names:
        v = _frame.get(pn)
        if v is not None:
            cli_overrides[pn] = v

    # ── Merge: YAML base, CLI overrides on top ────────────────────
    merged: dict = {**yaml_data, **cli_overrides}

    final_item_type = item_type or merged.get("item_type")
    final_query = query or merged.get("query")

    if not final_item_type:
        console.print("[red]Error: Missing 'item_type'. Provide as argument or via --config YAML.[/red]")
        raise typer.Exit(1)

    # query is optional for repos/issues/prs/commits, required for code
    if not final_query and final_item_type == "code":
        console.print("[red]Error: 'query' is required for code search.[/red]")
        raise typer.Exit(1)

    if "limit" not in merged:
        merged["limit"] = 30

    console.print(
        f"[bold blue]Searching {final_item_type}"
        + (f" for '{final_query}'" if final_query else "")
        + (f" (via {config.name})" if config else "")
        + "...[/bold blue]"
    )
    try:
        search_github(
            item_type=final_item_type,
            query=final_query or "",
            config=merged,
        )
    except Exception as e:
        console.print(f"[red]Search failed: {e}[/red]")

if __name__ == "__main__":
    app()
