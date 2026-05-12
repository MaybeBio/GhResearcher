from typing import *
from datetime import datetime, timezone, timedelta
from .gh_client import run_gh_command

def _fetch_paginated_events(endpoint: str, limit: int, since_dt: Optional[datetime] = None, until_dt: Optional[datetime] = None) -> List[Dict[str, Any]]:
    events = []
    page = 1
    per_page = min(limit, 100) if limit < 100 else 100
    
    while len(events) < limit:
        args = ["api", f"{endpoint}?per_page={per_page}&page={page}"]
        page_events = run_gh_command(args)
        
        if not isinstance(page_events, list) or not page_events:
            break
            
        should_break = False
        for event in page_events:
            created_at_raw = event.get("created_at", "")
            dt_cst = None
            if created_at_raw:
                try:
                    dt_utc = datetime.strptime(created_at_raw, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                    dt_cst = dt_utc.astimezone(timezone(timedelta(hours=8)))
                except ValueError:
                    pass
            
            # Since GitHub sorted newest to oldest, if event is older than since_dt we can break
            if since_dt and dt_cst and dt_cst < since_dt:
                should_break = True
                break
                
            # If event is newer than until_dt, skip this event
            if until_dt and dt_cst and dt_cst > until_dt:
                continue
                
            events.append(event)
            if len(events) >= limit:
                break
                
        if should_break:
            break
            
        page += 1
        
    return events

def get_user_events(username: str, limit: int = 30, since_dt: Optional[datetime] = None, until_dt: Optional[datetime] = None) -> List[Dict[str, Any]]:
    return _fetch_paginated_events(f"/users/{username}/events", limit, since_dt, until_dt)

def get_received_events(username: str, limit: int = 30, since_dt: Optional[datetime] = None, until_dt: Optional[datetime] = None) -> List[Dict[str, Any]]:
    return _fetch_paginated_events(f"/users/{username}/received_events", limit, since_dt, until_dt)

def get_org_events(org: str, limit: int = 30, since_dt: Optional[datetime] = None, until_dt: Optional[datetime] = None) -> List[Dict[str, Any]]:
    return _fetch_paginated_events(f"/orgs/{org}/events", limit, since_dt, until_dt)

def get_repo_events(owner_repo: str, limit: int = 30, since_dt: Optional[datetime] = None, until_dt: Optional[datetime] = None) -> List[Dict[str, Any]]:
    return _fetch_paginated_events(f"/repos/{owner_repo}/events", limit, since_dt, until_dt)

def format_event(event: Dict[str, Any], expand_commits: bool = False) -> str:
    event_type = event.get("type", "UnknownEvent")
    actor = event.get("actor", {}).get("login", "Unknown")
    repo = event.get("repo", {}).get("name", "Unknown Repo")
    
    created_at_raw = event.get("created_at", "")
    if created_at_raw:
        try:
            dt_utc = datetime.strptime(created_at_raw, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            dt_cst = dt_utc.astimezone(timezone(timedelta(hours=8)))
            created_at = dt_cst.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            created_at = created_at_raw.replace("T", " ").replace("Z", "")
    else:
        created_at = ""

    # highlight actor color
    actor_colored = f"[bold cyan]{actor}[/bold cyan]"

    if event_type == "WatchEvent":
        return f"{created_at} | ⭐️ {actor_colored} starred {repo}"
    elif event_type == "FollowEvent":
        target = event.get("payload", {}).get("target", {}).get("login", "Unknown")
        return f"{created_at} | 👤 {actor_colored} followed {target}"
    elif event_type == "PushEvent":
        commits = event.get("payload", {}).get("commits", [])
        lines = [f"{created_at} | 🚀 {actor_colored} pushed to {repo}"]
        
        # Expand missing commits if option enabled
        if not commits and expand_commits:
            head = event.get("payload", {}).get("head")
            if head:
                try:
                    commit_detail = run_gh_command(["api", f"repos/{repo}/commits/{head}"])
                    if isinstance(commit_detail, dict) and "sha" in commit_detail:
                        sha = commit_detail.get("sha", head)[:7]
                        commit_info = commit_detail.get("commit", {})
                        if isinstance(commit_info, dict):
                            msg = str(commit_info.get("message", "no msg"))
                        else:
                            msg = "no msg"
                        msg = msg.splitlines()[0] if msg else "no msg"
                        commits = [{"sha": sha, "message": f"(expanded) {msg}"}]
                except Exception:
                    pass
                    
        for c in commits:
            sha = c.get("sha", "0000000")[:7]
            msg = c.get("message", "no msg").splitlines()[0]
            # Escape brackets so rich won't treat it as markup
            lines.append(f"    - \\[{sha}] {msg}")
            
        if len(lines) == 1:
            lines[0] += " (no commit info)"
        return "\n".join(lines)
    elif event_type == "CreateEvent":
        ref_type = event.get("payload", {}).get("ref_type", "repo")
        ref_name = event.get("payload", {}).get("ref", "")
        detail = f" '{ref_name}'" if ref_name and ref_type != "repo" else ""
        return f"{created_at} | 🆕 {actor_colored} created {ref_type}{detail} at {repo}"
    elif event_type == "ForkEvent":
        return f"{created_at} | 🍴 {actor_colored} forked {repo}"
    elif event_type == "IssuesEvent":
        action = event.get("payload", {}).get("action", "")
        title = event.get("payload", {}).get("issue", {}).get("title", "")
        title_str = f": '{title}'" if title else ""
        return f"{created_at} | 🐛 {actor_colored} {action} issue in {repo}{title_str}"
    elif event_type == "IssueCommentEvent":
        action = event.get("payload", {}).get("action", "commented on")
        title = event.get("payload", {}).get("issue", {}).get("title", "")
        title_str = f" '{title}'" if title else ""
        return f"{created_at} | 💬 {actor_colored} {action} issue{title_str} in {repo}"
    elif event_type == "PullRequestEvent":
        action = event.get("payload", {}).get("action", "")
        title = event.get("payload", {}).get("pull_request", {}).get("title", "")
        title_str = f": '{title}'" if title else ""
        return f"{created_at} | 🔀 {actor_colored} {action} PR in {repo}{title_str}"
    elif event_type == "ReleaseEvent":
        action = event.get("payload", {}).get("action", "published")
        release = event.get("payload", {}).get("release", {})
        tag = release.get("tag_name") or release.get("name", "")
        tag_str = f" {tag}" if tag else ""
        return f"{created_at} | 🏷️  {actor_colored} {action} release{tag_str} in {repo}"
    
    return f"{created_at} | 🔹 {actor_colored} performed {event_type} on {repo}"
