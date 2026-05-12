## 选择区域 1

**来源页面:** [Searching code (legacy) - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-code)

**选择器信息:**
- XPath: `//*[@id="__next"]/div[1]/div[2]/div[2]`
- CSS Selector: `#__next > div > div.d-lg-flex:nth-of-type(2) > div.flex-column.flex-1.min-width-0.md-selector-preview.md-selector-highlight:nth-of-type(2)`

- [Search on GitHub](https://docs.github.com/en/search-github) /
- [Searching on GitHub](https://docs.github.com/en/search-github/searching-on-github) /
- [Searching code (legacy)](https://docs.github.com/en/search-github/searching-on-github/searching-code)
# Searching code (legacy)
You only need to use the legacy code search syntax if you are using the code search API.
Copy as Markdown
## In this article
- [Considerations for code search](#considerations-for-code-search)
- [Search by the file contents or file path](#search-by-the-file-contents-or-file-path)
- [Search within a user's or organization's repositories](#search-within-a-users-or-organizations-repositories)
- [Search by file location](#search-by-file-location)
- [Search by language](#search-by-language)
- [Search by file size](#search-by-file-size)
- [Search by filename](#search-by-filename)
- [Search by file extension](#search-by-file-extension)
- [Further reading](#further-reading)
Note
 This article covers the syntax for legacy code search, which you should only need to use for the [REST API endpoint for searching code](https://docs.github.com/en/rest/search/search#search-code).
 For information on the code search syntax that you can use on GitHub, see [Understanding GitHub Code Search syntax](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax).
 You can search globally across all of GitHub, or scope your search to a particular repository or organization. For more information, see [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github).
 You can only search code using these code search qualifiers. Search qualifiers specifically for repositories, users, or commits, will not work when searching for code.
 Tip
  - This article contains links to example searches on the GitHub.com website, but you can use the same search filters in any GitHub platform. In the linked example searches, replace `github.com` with the hostname for your GitHub platform.
- For a list of search syntaxes that you can add to any search qualifier to further improve your results, see [Understanding the search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
- Use quotations around multi-word search terms. For example, if you want to search for issues with the label "In progress," you'd search for `label:"in progress"`. Search is not case sensitive.
 ## [Considerations for code search](#considerations-for-code-search)
 Due to the complexity of searching code, there are some restrictions on how searches are performed:
 - You must be signed into a personal account on GitHub to search for code across all public repositories.
- Code in [forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks) is only searchable if the fork has more stars than the parent repository, and the forked repository has at least one pushed commit after being created. Forks with fewer stars than the parent repository or no commits are **not** indexed for code search. To include forks with more stars than their parent and at least one pushed commit in the search results, you will need to add `fork:true` or `fork:only` to your query. For more information, see [Searching in forks](https://docs.github.com/en/search-github/searching-on-github/searching-in-forks).
- Only the *default branch* is indexed for code search.
- Only files smaller than 384 KB are searchable.
- Up to 4,000 private repositories are searchable. These 4,000 repositories will be the most recently updated of the first 10,000 private repositories that you have access to.
- Only repositories with fewer than 500,000 files are searchable.
- Only repositories that have had activity or have been returned in search results in the last year are searchable.
- Archived repositories are not searchable.
- Except with [`filename`](#search-by-filename) searches, you must always include at least one search term when searching source code. For example, searching for [`language:javascript`](https://github.com/search?utf8=%E2%9C%93&q=language%3Ajavascript&type=Code&ref=searchresults) is not valid, while [`amazing language:javascript`](https://github.com/search?utf8=%E2%9C%93&q=amazing+language%3Ajavascript&type=Code&ref=searchresults) is.
- At most, search results can show two fragments from the same file, but there may be more results within the file.
- You can't use the following wildcard characters as part of your search query: `. , : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < > ( ) { } [ ] @`. The search will simply ignore these symbols.
 ## [Search by the file contents or file path](#search-by-the-file-contents-or-file-path)
 With the `in` qualifier you can restrict your search to the contents of the source code file, the file path, or both. When you omit this qualifier, only the file contents are searched.
 QualifierExample`in:file`[**octocat in:file**](https://github.com/search?q=octocat+in%3Afile&type=Code) matches code where "octocat" appears in the file contents.`in:path`[**octocat in:path**](https://github.com/search?q=octocat+in%3Apath&type=Code) matches code where "octocat" appears in the file path.`in:file,path`[**octocat in:file,path**](https://github.com/search?q=octocat+in%3Afile%2Cpath&type=Code) matches code where "octocat" appears in the file contents or the file path. ## [Search within a user's or organization's repositories](#search-within-a-users-or-organizations-repositories)
 To search the code in all repositories owned by a certain user or organization, you can use the `user` or `org` qualifier. To search the code in a specific repository, you can use the `repo` qualifier.
 QualifierExample`user:USERNAME`[**user:defunkt extension:rb**](https://github.com/search?q=user%3Agithub+extension%3Arb&type=Code) matches code from @defunkt that ends in *.rb*.`org:ORGNAME`[**org:github extension:js**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+extension%3Ajs&type=Code) matches code from GitHub that ends in *.js*.`repo:USERNAME/REPOSITORY`[**repo:mozilla/shumway extension:as**](https://github.com/search?q=repo%3Amozilla%2Fshumway+extension%3Aas&type=Code) matches code from @mozilla's shumway project that ends in *.as*. ## [Search by file location](#search-by-file-location)
 You can use the `path` qualifier to search for source code that appears at a specific location in a repository. Use `path:/` to search for files that are located at the root level of a repository. Or specify a directory name or the path to a directory to search for files that are located within that directory or any of its subdirectories.
 QualifierExample`path:/`[**octocat filename:readme path:/**](https://github.com/search?utf8=%E2%9C%93&q=octocat+filename%3Areadme+path%3A%2F&type=Code) matches *readme* files with the word "octocat" that are located at the root level of a repository.`path:DIRECTORY`[**form path:cgi-bin language:perl**](https://github.com/search?q=form+path%3Acgi-bin+language%3Aperl&type=Code) matches Perl files with the word "form" in the *cgi-bin* directory, or in any of its subdirectories.`path:PATH/TO/DIRECTORY`[**`console path:app/public language:javascript`**](https://github.com/search?q=console+path%3A%22app%2Fpublic%22+language%3Ajavascript&type=Code) matches JavaScript files with the word "console" in the *app/public* directory, or in any of its subdirectories (even if they reside in *app/public/js/form-validators*). ## [Search by language](#search-by-language)
 You can search for code based on what language it's written in. The `language` qualifier can be the language name or alias. For a full list of supported languages with their names and aliases, see the [github-linguist/linguist repository](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml).
 QualifierExample`language:LANGUAGE`[**element language:xml size:100**](https://github.com/search?q=element+language%3Axml+size%3A100&type=Code) matches code with the word "element" that's marked as being XML and has exactly 100 bytes.`language:LANGUAGE`[**display language:scss**](https://github.com/search?q=display+language%3Ascss&type=Code) matches code with the word "display," that's marked as being SCSS.`language:LANGUAGE`[**org:mozilla language:markdown**](https://github.com/search?utf8=%E2%9C%93&q=org%3Amozilla+language%3Amarkdown&type=Code) matches code from all @mozilla's repositories that's marked as Markdown. ## [Search by file size](#search-by-file-size)
 You can use the `size` qualifier to search for source code based on the size of the file where the code exists. The `size` qualifier uses [greater than, less than, and range qualifiers](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax) to filter results based on the byte size of the file in which the code is found.
 QualifierExample`size:n`[**function size:>10000 language:python**](https://github.com/search?q=function+size%3A%3E10000+language%3Apython&type=Code) matches code with the word "function," written in Python, in files that are larger than 10 KB. ## [Search by filename](#search-by-filename)
 The `filename` qualifier matches code files with a certain filename. You can also find a file in a repository using the file finder. For more information, see [Finding files on GitHub](https://docs.github.com/en/search-github/searching-on-github/finding-files-on-github).
 QualifierExample`filename:FILENAME`[**filename:linguist**](https://github.com/search?utf8=%E2%9C%93&q=filename%3Alinguist&type=Code) matches files named "linguist."`filename:FILENAME`[**filename:.vimrc commands**](https://github.com/search?q=filename%3A.vimrc+commands&type=Code) matches *.vimrc* files with the word "commands."`filename:FILENAME`[**filename:test_helper path:test language:ruby**](https://github.com/search?q=minitest+filename%3Atest_helper+path%3Atest+language%3Aruby&type=Code) matches Ruby files named *test_helper* within the *test* directory. ## [Search by file extension](#search-by-file-extension)
 The `extension` qualifier matches code files with a certain file extension.
 QualifierExample`extension:EXTENSION`[**form path:cgi-bin extension:pm**](https://github.com/search?q=form+path%3Acgi-bin+extension%3Apm&type=Code) matches code with the word "form," under *cgi-bin*, with the *.pm* file extension.`extension:EXTENSION`[**icon size:>200000 extension:css**](https://github.com/search?utf8=%E2%9C%93&q=icon+size%3A%3E200000+extension%3Acss&type=Code) matches files larger than 200 KB that end in .css and have the word "icon." ## [Further reading](#further-reading)
 - [Sorting search results](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)
- [Searching in forks](https://docs.github.com/en/search-github/searching-on-github/searching-in-forks)
- [Navigating code on GitHub](https://docs.github.com/en/repositories/working-with-files/using-files/navigating-code-on-github)## Help and support
### Did you find what you needed?
YesNo
[Privacy policy](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
### Help us make these docs great!
All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.
[Make a contribution](https://github.com/github/docs/blob/main/content/search-github/searching-on-github/searching-code.md)
[Learn how to contribute](https://docs.github.com/contributing)
### Still need help?
[Ask the GitHub community](https://github.com/orgs/community/discussions)
[Contact support](https://support.github.com)## Legal
- © 2026 GitHub, Inc.
- [Terms](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)
- [Privacy](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
- [Status](https://www.githubstatus.com/)
- [Pricing](https://github.com/pricing)
- [Expert services](https://services.github.com)
- [Blog](https://github.blog)

*选择时间: 2026/5/12 13:32:35*