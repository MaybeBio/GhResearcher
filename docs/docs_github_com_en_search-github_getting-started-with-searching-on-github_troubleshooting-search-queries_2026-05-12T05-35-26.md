## 选择区域 1

**来源页面:** [Troubleshooting search queries - GitHub Docs](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/troubleshooting-search-queries)

**选择器信息:**
- XPath: `//*[@id="main-content"]/div[1]/div[2]`
- CSS Selector: `#main-content > div.container-xl.px-3.px-md-6.my-4 > div.ArticleGridLayout_containerBox__lLLio.md-selector-preview.md-selector-highlight:nth-of-type(2)`

# Troubleshooting search queries
If you encounter unexpected results while searching on GitHub, you can troubleshoot by reviewing common problems and limitations.
Copy as Markdown
## In this article
- [Potential timeouts](#potential-timeouts)
- [Limitations on query length](#limitations-on-query-length)
- [Further reading](#further-reading)
## [Potential timeouts](#potential-timeouts)
 Some queries are computationally expensive for our search infrastructure to execute. To keep search fast for everyone, we limit how long any individual query can run. In rare situations when a query exceeds the time limit, search returns all matches that were found prior to the timeout and informs you that a timeout occurred.
 Reaching a timeout does not necessarily mean that search results are incomplete. It just means that the query was discontinued before it searched through all possible data.
 ## [Limitations on query length](#limitations-on-query-length)
 There are some limits to the length of the queries when searching across GitHub:
 - Queries longer than 256 characters are not supported
- You can't construct a query using more than five `AND`, `OR`, or `NOT` operators
 Specific search types, such as code search, might have additional limitations. Check the documentation for these search types for more information. For more information on code search limitations specifically, see [About GitHub Code Search](https://docs.github.com/en/search-github/github-code-search/about-github-code-search#limitations).
 ## [Further reading](#further-reading)
 - [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github)

*选择时间: 2026/5/12 13:35:24*

---

## 选择区域 2

**来源页面:** [Troubleshooting search queries - GitHub Docs](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/troubleshooting-search-queries)

**选择器信息:**
- XPath: `//*[@id="_r_6_--label"]`
- CSS Selector: `#_r_6_--label`

Troubleshoot search queries

*选择时间: 2026/5/12 13:35:24*