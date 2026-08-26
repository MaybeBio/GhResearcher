from typing import *
import sys
from rich.console import Console
from .gh_client import run_gh_command

console = Console(soft_wrap=not sys.stdout.isatty())

# ── Field validation ──────────────────────────────────────────────

VALID_SEARCH_FIELDS: dict[str, set[str]] = {
    "repos": {
        "query", "limit", "sort", "order", "web",
        "archived", "language", "topic", "owner", "match",
        "created", "followers", "forks", "good_first_issues",
        "help_wanted_issues", "include_forks", "license",
        "number_topics", "size", "stars", "updated", "visibility",
        "json", "jq", "template",
    },
    "code": {
        "query", "limit", "web",
        "sort", "order",  # recognized but unsupported by gh code search (warned below)
        "extension", "filename", "language", "match", "owner",
        "repo", "size",
        "json", "jq", "template",
    },
    "issues": {
        "query", "limit", "sort", "order", "web",
        "app", "archived", "assignee", "author", "closed",
        "commenter", "comments", "created", "include_prs",
        "interactions", "involves", "label", "language",
        "locked", "match", "mentions", "milestone",
        "no_assignee", "no_label", "no_milestone", "no_project",
        "owner", "project", "reactions", "repo", "state",
        "team_mentions", "updated", "visibility",
        "json", "jq", "template",
    },
    "prs": {
        "query", "limit", "sort", "order", "web",
        "app", "archived", "assignee", "author", "base",
        "checks", "closed", "commenter", "comments", "created",
        "draft", "head", "interactions", "involves", "label",
        "language", "locked", "match", "mentions", "merged",
        "merged_at", "milestone", "no_assignee", "no_label",
        "no_milestone", "no_project", "owner", "project",
        "reactions", "repo", "review", "review_requested",
        "reviewed_by", "state", "team_mentions", "updated",
        "visibility",
        "json", "jq", "template",
    },
    "commits": {
        "query", "limit", "sort", "order", "web",
        "author", "author_date", "author_email", "author_name",
        "committer", "committer_date", "committer_email",
        "committer_name", "hash", "merge", "owner", "parent",
        "repo", "tree", "visibility",
        "json", "jq", "template",
    },
}

# Boolean flags that are pure presence indicators (no =true/=false)
PRESENCE_FLAGS: set[str] = {
    "web", "draft", "merged", "include_prs", "locked", "merge",
    "no_assignee", "no_label", "no_milestone", "no_project",
}

# Boolean flags that accept true/false values
VALUE_BOOLEAN_FLAGS: set[str] = {
    "archived",
}

VALID_SORT_VALUES: dict[str, set[str]] = {
    "repos": {"forks", "help-wanted-issues", "stars", "updated"},
    "issues": {
        "comments", "created", "interactions", "reactions",
        "reactions-+1", "reactions--1", "reactions-heart",
        "reactions-smile", "reactions-tada", "reactions-thinking_face",
        "updated",
    },
    "prs": {
        "comments", "reactions", "reactions-+1", "reactions--1",
        "reactions-smile", "reactions-thinking_face", "reactions-heart",
        "reactions-tada", "interactions", "created", "updated",
    },
    "commits": {"author-date", "committer-date"},
}


def _validate_config(item_type: str, config: dict) -> list[str]:
    valid_fields = VALID_SEARCH_FIELDS.get(item_type)
    if valid_fields is None:
        return []

    warnings: list[str] = []
    for key in config:
        if key in ("item_type",):
            continue
        if key not in valid_fields:
            warnings.append(
                f"Unknown field '{key}' for item_type '{item_type}' — will be passed to gh but may be ignored."
            )

    sort_val = config.get("sort")
    if sort_val and item_type == "code":
        warnings.append("'sort'/'order' are not supported for code search and will be ignored.")
    elif sort_val and item_type in VALID_SORT_VALUES:
        if sort_val not in VALID_SORT_VALUES[item_type]:
            valid = "', '".join(sorted(VALID_SORT_VALUES[item_type]))
            warnings.append(
                f"Invalid sort value '{sort_val}' for '{item_type}'. Valid values: '{valid}'"
            )

    return warnings


# ── Main search function ──────────────────────────────────────────

def search_github(item_type: str, query: str, config: dict):
    """Execute gh search for different item types (repos, code, issues, etc.).
    Maps all keys in the config dict directly to gh CLI flags.
    """
    warnings = _validate_config(item_type, config)
    for w in warnings:
        console.print(f"[yellow]Warning: {w}[/yellow]")

    cmd = ["search", item_type]
    if query:
        cmd.append(query)

    use_web = config.get("web", False)

    for key, value in config.items():
        if key in ("item_type", "query", "web"):
            continue
        if item_type == "code" and key in ("sort", "order"):
            continue  # warned by _validate_config; gh code search has no --sort/--order

        flag = f"--{key.replace('_', '-')}"

        if key in VALUE_BOOLEAN_FLAGS:
            # gh value-booleans (--archived) only accept --flag=true/false syntax.
            if isinstance(value, str):
                normalized = value.strip().lower() == "true"
            else:
                normalized = bool(value)
            cmd.append(f"{flag}={str(normalized).lower()}")
        elif isinstance(value, bool):
            if key in PRESENCE_FLAGS:
                if value:
                    cmd.append(flag)
            else:
                cmd.append(f"{flag}={str(value).lower()}")
        elif isinstance(value, (list, tuple)):
            cmd.extend([flag, ",".join(str(v) for v in value)])
        elif value is not None:
            cmd.extend([flag, str(value)])

    if use_web:
        cmd.append("--web")

    console.print(f"[dim]Running command: gh {' '.join(cmd)}[/dim]")

    if use_web:
        run_gh_command(cmd, capture_output=False)
    else:
        output = run_gh_command(cmd, capture_output=True)
        if isinstance(output, str):
            console.print(output)
        else:
            console.print(output)