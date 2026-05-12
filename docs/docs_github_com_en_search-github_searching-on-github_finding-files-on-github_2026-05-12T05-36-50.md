## 选择区域 1

**来源页面:** [Finding files on GitHub - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/finding-files-on-github)

**选择器信息:**
- XPath: `//*[@id="__next"]/div[1]/div[2]/div[2]`
- CSS Selector: `#__next > div > div.d-lg-flex:nth-of-type(2) > div.flex-column.flex-1.min-width-0.md-selector-highlight:nth-of-type(2)`

- [Search on GitHub](https://docs.github.com/en/search-github) /
- [Searching on GitHub](https://docs.github.com/en/search-github/searching-on-github) /
- [Finding files on GitHub](https://docs.github.com/en/search-github/searching-on-github/finding-files-on-github)
# Finding files on GitHub
You can search for a file in a repository using the file finder. To search for a file in multiple repositories on GitHub, use the [`path` code search qualifier](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax#path-qualifier).
Copy as Markdown
## In this article
- [Using the file finder](#using-the-file-finder)
- [Customizing excluded files](#customizing-excluded-files)
- [Further reading](#further-reading)
Tip
  - By default, file finder results exclude some directories like `build`, `log`, `tmp`, and `vendor`. To search for files in these directories, use the [`path` code search qualifier](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax#path-qualifier). Alternatively, you can customize which directories are excluded by default [using a `.gitattributes` file](#customizing-excluded-files).
- You can also open the file finder by pressing `t` on your keyboard. For more information, see [Keyboard shortcuts](https://docs.github.com/en/get-started/accessibility/keyboard-shortcuts).
 ## [Using the file finder](#using-the-file-finder)
 1. On GitHub, navigate to the main page of the repository.
2. In the “Go to file” search bar, type the name of the file or directory you'd like to find. ![Screenshot of the main view for a repository. A search bar, labeled "Go to file", is outlined in dark orange.](https://docs.github.com/assets/cb-19343/images/help/repository/repository-main-page-go-to-file.png)
3. Alternatively, if there is no "Go to file" search bar, click **Go to file**, then type the name of the file or directory you'd like to find. ![Screenshot of the main view for a repository. A "Go to file" button is outlined in dark orange.](https://docs.github.com/assets/cb-13185/images/help/repository/repository-main-page-go-to-file-no-search-bar.png)
4. In the list of results, click the file or directory you wanted to find. You can view the file path for a directory or file below each search result.
 ## [Customizing excluded files](#customizing-excluded-files)
 By default, file finder results do not include files in the following directories:
 - `.git`
- `.hg`
- `.sass-cache`
- `.svn`
- `build`
- `dot_git`
- `log`
- `tmp`
- `vendor`
 You can override these default exclusions using a `.gitattributes` file.
 To do this, create or update a file called `.gitattributes` in your repository root, setting the [`linguist-generated`](https://github.com/github-linguist/linguist/blob/main/docs/overrides.md) attribute to `false` for each directory that should be included in file finder results.
 For example, the following `.gitattributes` file would cause files in the `build/` directory to be available to the file finder:
 ```text
build/** linguist-generated=false

```
 Note that this override requires the use of the recursive glob pattern ( `**`). For more information, see [pattern format](https://git-scm.com/docs/gitignore#_pattern_format) in the Git documentation. More complex overrides of subdirectories within excluded-by-default directories are not supported.
 ## [Further reading](#further-reading)
 - [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github)
- [Customizing how changed files appear on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/customizing-how-changed-files-appear-on-github)
- [`.gitattributes`](https://git-scm.com/docs/gitattributes) in the Git documentation## Help and support
### Did you find what you needed?
YesNo
[Privacy policy](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
### Help us make these docs great!
All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.
[Make a contribution](https://github.com/github/docs/blob/main/content/search-github/searching-on-github/finding-files-on-github.md)
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

*选择时间: 2026/5/12 13:36:47*

---

## 选择区域 2

**来源页面:** [Finding files on GitHub - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/finding-files-on-github)

**选择器信息:**
- XPath: `//*[@id="main-content"]/div[1]/div[2]`
- CSS Selector: `#main-content > div.container-xl.px-3.px-md-6.my-4 > div.ArticleGridLayout_containerBox__lLLio.md-selector-preview.md-selector-highlight:nth-of-type(2)`

# Finding files on GitHub
You can search for a file in a repository using the file finder. To search for a file in multiple repositories on GitHub, use the [`path` code search qualifier](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax#path-qualifier).
Copy as Markdown
## In this article
- [Using the file finder](#using-the-file-finder)
- [Customizing excluded files](#customizing-excluded-files)
- [Further reading](#further-reading)
Tip
  - By default, file finder results exclude some directories like `build`, `log`, `tmp`, and `vendor`. To search for files in these directories, use the [`path` code search qualifier](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax#path-qualifier). Alternatively, you can customize which directories are excluded by default [using a `.gitattributes` file](#customizing-excluded-files).
- You can also open the file finder by pressing `t` on your keyboard. For more information, see [Keyboard shortcuts](https://docs.github.com/en/get-started/accessibility/keyboard-shortcuts).
 ## [Using the file finder](#using-the-file-finder)
 1. On GitHub, navigate to the main page of the repository.
2. In the “Go to file” search bar, type the name of the file or directory you'd like to find. ![Screenshot of the main view for a repository. A search bar, labeled "Go to file", is outlined in dark orange.](https://docs.github.com/assets/cb-19343/images/help/repository/repository-main-page-go-to-file.png)
3. Alternatively, if there is no "Go to file" search bar, click **Go to file**, then type the name of the file or directory you'd like to find. ![Screenshot of the main view for a repository. A "Go to file" button is outlined in dark orange.](https://docs.github.com/assets/cb-13185/images/help/repository/repository-main-page-go-to-file-no-search-bar.png)
4. In the list of results, click the file or directory you wanted to find. You can view the file path for a directory or file below each search result.
 ## [Customizing excluded files](#customizing-excluded-files)
 By default, file finder results do not include files in the following directories:
 - `.git`
- `.hg`
- `.sass-cache`
- `.svn`
- `build`
- `dot_git`
- `log`
- `tmp`
- `vendor`
 You can override these default exclusions using a `.gitattributes` file.
 To do this, create or update a file called `.gitattributes` in your repository root, setting the [`linguist-generated`](https://github.com/github-linguist/linguist/blob/main/docs/overrides.md) attribute to `false` for each directory that should be included in file finder results.
 For example, the following `.gitattributes` file would cause files in the `build/` directory to be available to the file finder:
 ```text
build/** linguist-generated=false

```
 Note that this override requires the use of the recursive glob pattern ( `**`). For more information, see [pattern format](https://git-scm.com/docs/gitignore#_pattern_format) in the Git documentation. More complex overrides of subdirectories within excluded-by-default directories are not supported.
 ## [Further reading](#further-reading)
 - [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github)
- [Customizing how changed files appear on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/customizing-how-changed-files-appear-on-github)
- [`.gitattributes`](https://git-scm.com/docs/gitattributes) in the Git documentation

*选择时间: 2026/5/12 13:36:47*

---

## 选择区域 3

**来源页面:** [Finding files on GitHub - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/finding-files-on-github)

**选择器信息:**
- XPath: `//*[@id="_r_1d_--label"]`
- CSS Selector: `#_r_1d_--label`

Sorting search results

*选择时间: 2026/5/12 13:36:47*

---

## 选择区域 4

**来源页面:** [Finding files on GitHub - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/finding-files-on-github)

**选择器信息:**
- XPath: `//*[@id="_r_6_--label"]`
- CSS Selector: `#_r_6_--label`

Troubleshoot search queries

*选择时间: 2026/5/12 13:36:47*