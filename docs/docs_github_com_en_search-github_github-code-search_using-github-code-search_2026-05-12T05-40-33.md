## 选择区域 1

**来源页面:** [Using GitHub Code Search - GitHub Docs](https://docs.github.com/en/search-github/github-code-search/using-github-code-search)

**选择器信息:**
- XPath: `//*[@id="_r_dp_--label"]`
- CSS Selector: `#_r_dp_--label`

Search GitHub Models

*选择时间: 2026/5/12 13:40:33*

---

## 选择区域 2

**来源页面:** [Using GitHub Code Search - GitHub Docs](https://docs.github.com/en/search-github/github-code-search/using-github-code-search)

**选择器信息:**
- XPath: `//*[@id="__next"]/div[1]/div[2]/div[2]`
- CSS Selector: `#__next > div > div.d-lg-flex:nth-of-type(2) > div.flex-column.flex-1.min-width-0.md-selector-highlight:nth-of-type(2)`

- [Search on GitHub](https://docs.github.com/en/search-github) /
- [GitHub Code Search](https://docs.github.com/en/search-github/github-code-search) /
- [Using GitHub Code Search](https://docs.github.com/en/search-github/github-code-search/using-github-code-search)
# Using GitHub Code Search
You can use suggestions, completions and saved searches in the upgraded search interface to quickly find what you are looking for across GitHub.
Copy as Markdown
## In this article
- [About using GitHub code search](#about-using-github-code-search)
- [Using the search bar](#using-the-search-bar)
- [Getting answers with Copilot from the search bar](#getting-answers-with-copilot-from-the-search-bar)
- [Creating and managing saved searches](#creating-and-managing-saved-searches)
- [Using the search results view](#using-the-search-results-view)
- [Using GitHub code search on GitHub Mobile](#using-github-code-search-on-github-mobile)
## [About using GitHub code search](#about-using-github-code-search)
 GitHub indexes repositories you own and repositories in organizations you are a member of, whether public, private, or internal. This means that you can search across all of your repositories, in addition to the public repositories on GitHub that have already been indexed. Only users with permission to view your code will be able to see your code in search results. Forks are indexed and searchable in the same way as other repositories.
 Not all code is indexed, and you can currently only search the default branches of repositories. For more information on known limitations, see [About GitHub Code Search](https://docs.github.com/en/search-github/github-code-search/about-github-code-search#limitations).
 You must be logged in to a GitHub account to use code search, including for searching code in public repositories.
 ## [Using the search bar](#using-the-search-bar)
 You can search using the search interface on GitHub. Using suggestions, completions, and saved searches, you can quickly find what you are looking for, often without having to fully type a query or view the search results page.
 For more information about the search syntax of code search, see [Understanding GitHub Code Search syntax](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax).
 Note that the syntax and qualifiers for searching for non-code content, such as issues, users, and discussions, is not the same as the syntax for code search. For more information on non-code search, see [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github) and [Searching on GitHub](https://docs.github.com/en/search-github/searching-on-github).
 1. In the top navigation of GitHub, click the search bar.
2. Under the search bar, you will see a list of suggestions organized by category, including recent searches and suggested repositories, teams, and projects that you have access to. You can also see a list of saved searches that you have created. For more information on saved searches, see [Creating and managing saved searches](#creating-and-managing-saved-searches).
 ![Screenshot of the GitHub search bar. There is a list of search suggestions by category below the search bar.](https://docs.github.com/assets/cb-53314/images/help/search/code-search-beta-search-bar.png)
 If you click on any of the specific suggestions, you will be taken directly to the page for that suggestion (for example, the repository or project page). If you click on a recent or saved search, depending on the type of search, the search query will appear in the search bar or you will be taken to the search results page for the search term.
3. Once you start typing a search query, you will see a list of completions and suggestions that match your query. You can click on a suggestion to jump to a specific location. As you type more qualifiers, you will see more specific suggestions, such as code files you can jump to directly.
 ![Screenshot of a search for "repo:octocat/spoon-knife". The code results are outlined in dark orange.](https://docs.github.com/assets/cb-41581/images/help/search/code-search-beta-search-bar-code-suggestions.png)
4. After typing your query, you can also press Enter to go to the full search results view, where you can see each match and a visual interface for applying filters. For more information, see [Using the search results view](#using-the-search-results-view).
 ## [Getting answers with Copilot from the search bar](#getting-answers-with-copilot-from-the-search-bar)
 Note
 You'll need access to GitHub Copilot. For more information, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
 You can use GitHub Copilot to ask questions about an entire repository directly from the main search box. Simply type your question into the search bar, and Copilot can provide insights or explanations about the repository’s structure, purpose, or specific components. This makes it easy to get quick answers without navigating through multiple files, helping you stay focused and maintain your workflow.
 1. Navigate to a repository on GitHub.
2. Press /, or click in the main search box at the top of the page.
3. In the search box, after `repo:OWNER/REPO`, type the question you want to ask Copilot.
 For example, you could enter:
 - `What does this repo do?`
- `Where is authentication implemented in this codebase?`
- `How does license file detection work in this repo?`
4. Click **Ask Copilot**.
 ![Screenshot of the main search box on GitHub. The drop-down option "Ask Copilot" is highlighted with an orange outline.](https://docs.github.com/assets/cb-58192/images/help/copilot/ask-copilot-from-search-bar.png)
 The GitHub Copilot Chat panel is displayed and Copilot responds to your request.
5. Optionally, after submitting a question, you can click  in the text box to stop the response.
 ## [Creating and managing saved searches](#creating-and-managing-saved-searches)
 1. In the top navigation of GitHub, click the search bar and type `saved:`.
2. Under the search bar, in the "Saved queries" section, click **Manage saved searches**.
3. In the pop-up window, type both the name you want for your saved search and the query you want to save.
4. To finish creating your saved search, click **Create saved search**.
5. To see your saved search, click the search bar. Your saved search will be in the "Saved queries" section. Clicking on a saved search entry will add the query to the search bar and filter the suggestions accordingly.
6. To manage a saved search, type `saved:` in the search bar, then click **Manage saved searches**. - To edit a saved search, to the right of the search, click .
- To delete a saved search, to the right of the search, click .
 ## [Using the search results view](#using-the-search-results-view)
 To construct a search query, as well as view and filter results, using a visual interface, you can use the [search](https://github.com/search) page or [advanced search](https://github.com/search/advanced) page. If you press Enter after typing a search query in the search bar, you will also be taken to the search results view.
 On the search results view, you can navigate between different types of search results, including code, issues, pull request, repositories, and more. You can also view and use filters.
 ## [Using GitHub code search on GitHub Mobile](#using-github-code-search-on-github-mobile)
 On GitHub Mobile, you can use code search directly from the search bar in the home screen. Code search on GitHub Mobile uses the same syntax as code search on GitHub. For more information, see [About GitHub Code Search](https://docs.github.com/en/search-github/github-code-search/about-github-code-search#limitations).
 Once you start typing a search query, you will see a list of completions and suggestions that match your query. You can click on a suggestion to jump to a specific location. As you type more qualifiers, you will see more specific suggestions, such as code files you can jump to directly.## Help and support
### Did you find what you needed?
YesNo
[Privacy policy](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
### Help us make these docs great!
All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.
[Make a contribution](https://github.com/github/docs/blob/main/content/search-github/github-code-search/using-github-code-search.md)
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

*选择时间: 2026/5/12 13:40:33*

---

## 选择区域 3

**来源页面:** [Using GitHub Code Search - GitHub Docs](https://docs.github.com/en/search-github/github-code-search/using-github-code-search)

**选择器信息:**
- XPath: `//*[@id="main-content"]/div[1]/div[2]`
- CSS Selector: `#main-content > div.container-xl.px-3.px-md-6.my-4 > div.ArticleGridLayout_containerBox__lLLio.md-selector-preview.md-selector-highlight:nth-of-type(2)`

# Using GitHub Code Search
You can use suggestions, completions and saved searches in the upgraded search interface to quickly find what you are looking for across GitHub.
Copy as Markdown
## In this article
- [About using GitHub code search](#about-using-github-code-search)
- [Using the search bar](#using-the-search-bar)
- [Getting answers with Copilot from the search bar](#getting-answers-with-copilot-from-the-search-bar)
- [Creating and managing saved searches](#creating-and-managing-saved-searches)
- [Using the search results view](#using-the-search-results-view)
- [Using GitHub code search on GitHub Mobile](#using-github-code-search-on-github-mobile)
## [About using GitHub code search](#about-using-github-code-search)
 GitHub indexes repositories you own and repositories in organizations you are a member of, whether public, private, or internal. This means that you can search across all of your repositories, in addition to the public repositories on GitHub that have already been indexed. Only users with permission to view your code will be able to see your code in search results. Forks are indexed and searchable in the same way as other repositories.
 Not all code is indexed, and you can currently only search the default branches of repositories. For more information on known limitations, see [About GitHub Code Search](https://docs.github.com/en/search-github/github-code-search/about-github-code-search#limitations).
 You must be logged in to a GitHub account to use code search, including for searching code in public repositories.
 ## [Using the search bar](#using-the-search-bar)
 You can search using the search interface on GitHub. Using suggestions, completions, and saved searches, you can quickly find what you are looking for, often without having to fully type a query or view the search results page.
 For more information about the search syntax of code search, see [Understanding GitHub Code Search syntax](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax).
 Note that the syntax and qualifiers for searching for non-code content, such as issues, users, and discussions, is not the same as the syntax for code search. For more information on non-code search, see [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github) and [Searching on GitHub](https://docs.github.com/en/search-github/searching-on-github).
 1. In the top navigation of GitHub, click the search bar.
2. Under the search bar, you will see a list of suggestions organized by category, including recent searches and suggested repositories, teams, and projects that you have access to. You can also see a list of saved searches that you have created. For more information on saved searches, see [Creating and managing saved searches](#creating-and-managing-saved-searches).
 ![Screenshot of the GitHub search bar. There is a list of search suggestions by category below the search bar.](https://docs.github.com/assets/cb-53314/images/help/search/code-search-beta-search-bar.png)
 If you click on any of the specific suggestions, you will be taken directly to the page for that suggestion (for example, the repository or project page). If you click on a recent or saved search, depending on the type of search, the search query will appear in the search bar or you will be taken to the search results page for the search term.
3. Once you start typing a search query, you will see a list of completions and suggestions that match your query. You can click on a suggestion to jump to a specific location. As you type more qualifiers, you will see more specific suggestions, such as code files you can jump to directly.
 ![Screenshot of a search for "repo:octocat/spoon-knife". The code results are outlined in dark orange.](https://docs.github.com/assets/cb-41581/images/help/search/code-search-beta-search-bar-code-suggestions.png)
4. After typing your query, you can also press Enter to go to the full search results view, where you can see each match and a visual interface for applying filters. For more information, see [Using the search results view](#using-the-search-results-view).
 ## [Getting answers with Copilot from the search bar](#getting-answers-with-copilot-from-the-search-bar)
 Note
 You'll need access to GitHub Copilot. For more information, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
 You can use GitHub Copilot to ask questions about an entire repository directly from the main search box. Simply type your question into the search bar, and Copilot can provide insights or explanations about the repository’s structure, purpose, or specific components. This makes it easy to get quick answers without navigating through multiple files, helping you stay focused and maintain your workflow.
 1. Navigate to a repository on GitHub.
2. Press /, or click in the main search box at the top of the page.
3. In the search box, after `repo:OWNER/REPO`, type the question you want to ask Copilot.
 For example, you could enter:
 - `What does this repo do?`
- `Where is authentication implemented in this codebase?`
- `How does license file detection work in this repo?`
4. Click **Ask Copilot**.
 ![Screenshot of the main search box on GitHub. The drop-down option "Ask Copilot" is highlighted with an orange outline.](https://docs.github.com/assets/cb-58192/images/help/copilot/ask-copilot-from-search-bar.png)
 The GitHub Copilot Chat panel is displayed and Copilot responds to your request.
5. Optionally, after submitting a question, you can click  in the text box to stop the response.
 ## [Creating and managing saved searches](#creating-and-managing-saved-searches)
 1. In the top navigation of GitHub, click the search bar and type `saved:`.
2. Under the search bar, in the "Saved queries" section, click **Manage saved searches**.
3. In the pop-up window, type both the name you want for your saved search and the query you want to save.
4. To finish creating your saved search, click **Create saved search**.
5. To see your saved search, click the search bar. Your saved search will be in the "Saved queries" section. Clicking on a saved search entry will add the query to the search bar and filter the suggestions accordingly.
6. To manage a saved search, type `saved:` in the search bar, then click **Manage saved searches**. - To edit a saved search, to the right of the search, click .
- To delete a saved search, to the right of the search, click .
 ## [Using the search results view](#using-the-search-results-view)
 To construct a search query, as well as view and filter results, using a visual interface, you can use the [search](https://github.com/search) page or [advanced search](https://github.com/search/advanced) page. If you press Enter after typing a search query in the search bar, you will also be taken to the search results view.
 On the search results view, you can navigate between different types of search results, including code, issues, pull request, repositories, and more. You can also view and use filters.
 ## [Using GitHub code search on GitHub Mobile](#using-github-code-search-on-github-mobile)
 On GitHub Mobile, you can use code search directly from the search bar in the home screen. Code search on GitHub Mobile uses the same syntax as code search on GitHub. For more information, see [About GitHub Code Search](https://docs.github.com/en/search-github/github-code-search/about-github-code-search#limitations).
 Once you start typing a search query, you will see a list of completions and suggestions that match your query. You can click on a suggestion to jump to a specific location. As you type more qualifiers, you will see more specific suggestions, such as code files you can jump to directly.

*选择时间: 2026/5/12 13:40:33*

---

## 选择区域 4

**来源页面:** [Using GitHub Code Search - GitHub Docs](https://docs.github.com/en/search-github/github-code-search/using-github-code-search)

**选择器信息:**
- XPath: `//*[@id="_r_1d_--label"]`
- CSS Selector: `#_r_1d_--label`

Sorting search results

*选择时间: 2026/5/12 13:40:33*

---

## 选择区域 5

**来源页面:** [Using GitHub Code Search - GitHub Docs](https://docs.github.com/en/search-github/github-code-search/using-github-code-search)

**选择器信息:**
- XPath: `//*[@id="_r_6_--label"]`
- CSS Selector: `#_r_6_--label`

Troubleshoot search queries

*选择时间: 2026/5/12 13:40:33*