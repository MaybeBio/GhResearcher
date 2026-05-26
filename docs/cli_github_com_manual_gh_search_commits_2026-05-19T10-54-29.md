## 选择区域 1

**来源页面:** [GitHub CLI | Take GitHub to the command line](https://cli.github.com/manual/gh_search_commits)

**选择器信息:**
- XPath: `//*[@id="main"]`
- CSS Selector: `#main`

## gh search commits
 ```
gh search commits [<query>] [flags]

```
 Search for commits on GitHub.
 The command supports constructing queries using the GitHub search syntax, using the parameter and qualifier flags, or a combination of the two.
 GitHub search syntax is documented at: [https://docs.github.com/search-github/searching-on-github/searching-commits](https://docs.github.com/search-github/searching-on-github/searching-commits)
 For more information on handling search queries containing a hyphen, run `gh search --help`.
 ### Options
 `--author <string>` Filter by author `--author-date <date>` Filter based on authored date `--author-email <string>` Filter on author email `--author-name <string>` Filter on author name `--committer <string>` Filter by committer `--committer-date <date>` Filter based on committed date `--committer-email <string>` Filter on committer email `--committer-name <string>` Filter on committer name `--hash <string>` Filter by commit hash `-q`, `--jq <expression>` Filter JSON output using a jq expression `--json <fields>` Output JSON with the specified fields `-L`, `--limit <int> (default 30)` Maximum number of commits to fetch `--merge` Filter on merge commits `--order <string> (default "desc")` Order of commits returned, ignored unless '--sort' flag is specified: {asc|desc} `--owner <strings>` Filter on repository owner `--parent <string>` Filter by parent hash `-R`, `--repo <strings>` Filter on repository `--sort <string> (default "best-match")` Sort fetched commits: {author-date|committer-date} `-t`, `--template <string>` Format JSON output using a Go template; see "gh help formatting" `--tree <string>` Filter by tree hash `--visibility <strings>` Filter based on repository visibility: {public|private|internal} `-w`, `--web` Open the search query in the web browser ### JSON Fields
 `author`, `commit`, `committer`, `id`, `parents`, `repository`, `sha`, `url`
 ### Examples
 ```bash
# Search commits matching set of keywords "readme" and "typo"
$ gh search commits readme typo

# Search commits matching phrase "bug fix"
$ gh search commits "bug fix"

# Search commits committed by user "monalisa"
$ gh search commits --committer=monalisa

# Search commits authored by users with name "Jane Doe"
$ gh search commits --author-name="Jane Doe"

# Search commits matching hash "8dd03144ffdc6c0d486d6b705f9c7fba871ee7c3"
$ gh search commits --hash=8dd03144ffdc6c0d486d6b705f9c7fba871ee7c3

# Search commits authored before February 1st, 2022
$ gh search commits --author-date="<2022-02-01"
``` ### See also
 - [gh search](https://cli.github.com/manual/gh_search)

*选择时间: 2026/5/19 18:54:25*