## 选择区域 1

**来源页面:** [GitHub CLI | Take GitHub to the command line](https://cli.github.com/manual/gh_search_code)

**选择器信息:**
- XPath: `//*[@id="main"]`
- CSS Selector: `#main`

## gh search code
 ```
gh search code <query> [flags]

```
 Search within code in GitHub repositories.
 The search syntax is documented at: [https://docs.github.com/search-github/searching-on-github/searching-code](https://docs.github.com/search-github/searching-on-github/searching-code)
 Note that these search results are powered by what is now a legacy GitHub code search engine. The results might not match what is seen on `github.com`, and new features like regex search are not yet available via the GitHub API.
 For more information on handling search queries containing a hyphen, run `gh search --help`.
 ### Options
 `--extension <string>` Filter on file extension `--filename <string>` Filter on filename `-q`, `--jq <expression>` Filter JSON output using a jq expression `--json <fields>` Output JSON with the specified fields `--language <string>` Filter results by language `-L`, `--limit <int> (default 30)` Maximum number of code results to fetch `--match <strings>` Restrict search to file contents or file path: {file|path} `--owner <strings>` Filter on owner `-R`, `--repo <strings>` Filter on repository `--size <string>` Filter on size range, in kilobytes `-t`, `--template <string>` Format JSON output using a Go template; see "gh help formatting" `-w`, `--web` Open the search query in the web browser ### JSON Fields
 `path`, `repository`, `sha`, `textMatches`, `url`
 ### Examples
 ```bash
# Search code matching "react" and "lifecycle"
$ gh search code react lifecycle

# Search code matching "error handling"
$ gh search code "error handling"

# Search code matching "deque" in Python files
$ gh search code deque --language=python

# Search code matching "cli" in repositories owned by microsoft organization
$ gh search code cli --owner=microsoft

# Search code matching "panic" in the GitHub CLI repository
$ gh search code panic --repo cli/cli

# Search code matching keyword "lint" in package.json files
$ gh search code lint --filename package.json
``` ### See also
 - [gh search](https://cli.github.com/manual/gh_search)

*选择时间: 2026/5/19 18:54:00*