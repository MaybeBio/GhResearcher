## 选择区域 1

**来源页面:** [GitHub CLI | Take GitHub to the command line](https://cli.github.com/manual/gh_search)

**选择器信息:**
- XPath: `//*[@id="main"]`
- CSS Selector: `#main`

## gh search
 Search across all of GitHub.
 Excluding search results that match a qualifier
 In a browser, the GitHub search syntax supports excluding results that match a search qualifier by prefixing the qualifier with a hyphen. For example, to search for issues that do not have the label "bug", you would use `-label:bug` as a search qualifier.
 `gh` supports this syntax in `gh search` as well, but it requires extra command line arguments to avoid the hyphen being interpreted as a command line flag because it begins with a hyphen.
 On Unix-like systems, you can use the `--` argument to indicate that the arguments that follow are not a flag, but rather a query string. For example:
 $ gh search issues -- "my-search-query -label:bug"
 On PowerShell, you must use both the `--%` argument and the `--` argument to produce the same effect. For example:
 $ gh --% search issues -- "my search query -label:bug"
 See the following for more information:
 - GitHub search syntax: [https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#exclude-results-that-match-a-qualifier](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#exclude-results-that-match-a-qualifier)
- The PowerShell stop parse flag `--%`: [https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_parsing?view=powershell-7.5#the-stop-parsing-token](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_parsing?view=powershell-7.5#the-stop-parsing-token)
- The Unix-like `--` argument: [https://www.gnu.org/software/bash/manual/bash.html#Shell-Builtin-Commands-1](https://www.gnu.org/software/bash/manual/bash.html#Shell-Builtin-Commands-1)
 ### Available commands
 - [gh search code](https://cli.github.com/manual/gh_search_code)
- [gh search commits](https://cli.github.com/manual/gh_search_commits)
- [gh search issues](https://cli.github.com/manual/gh_search_issues)
- [gh search prs](https://cli.github.com/manual/gh_search_prs)
- [gh search repos](https://cli.github.com/manual/gh_search_repos)
 ### See also
 - [gh](https://cli.github.com/manual/gh)

*选择时间: 2026/5/19 18:53:19*