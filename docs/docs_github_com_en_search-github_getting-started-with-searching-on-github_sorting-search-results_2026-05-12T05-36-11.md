## 选择区域 1

**来源页面:** [Sorting search results - GitHub Docs](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)

**选择器信息:**
- XPath: `//*[@id="__next"]/div[1]/div[2]/div[2]`
- CSS Selector: `#__next > div > div.d-lg-flex:nth-of-type(2) > div.flex-column.flex-1.min-width-0.md-selector-highlight:nth-of-type(2)`

- [Search on GitHub](https://docs.github.com/en/search-github) /
- [Start with search on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github) /
- [Sorting search results](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)
# Sorting search results
You can sort GitHub search results using the Sort menu, or by adding a `sort` qualifier to your query.
Copy as Markdown
## In this article
- [Sort by comments](#sort-by-comments)
- [Sort by created date](#sort-by-created-date)
- [Sort by relevance](#sort-by-relevance)
- [Sort by interactions](#sort-by-interactions)
- [Sort by reactions](#sort-by-reactions)
- [Sort by author date](#sort-by-author-date)
- [Sort by committer date](#sort-by-committer-date)
- [Sort by updated date](#sort-by-updated-date)
- [Further reading](#further-reading)
Note
 Sorting search results is not supported for GitHub code search. For more information on code search, see [About GitHub Code Search](https://docs.github.com/en/search-github/github-code-search/about-github-code-search).
 Use the **Sort** dropdown menu to sort results by relevance, number of stars, number of forks, and how recently the items were updated.
 To sort by interactions, reactions, comments, created date, relevance, author date, committer date, or how recently the items were updated, you can add a `sort` qualifier to your search query.
 ## [Sort by comments](#sort-by-comments)
 The `sort:comments` qualifier sorts by the number of comments.
 QualifierExample`sort:comments` or `sort:comments-desc`[**org:github sort:comments**](https://github.com/search?q=org%3Agithub+sort%3Acomments&type=Issues) matches issues in repositories owned by GitHub, sorted by the highest number of comments.`sort:comments-asc`[**org:github sort:comments-asc**](https://github.com/search?q=org%3Agithub+sort%3Acomments-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending number of comments (the fewest to the most). ## [Sort by created date](#sort-by-created-date)
 The `sort:created` qualifier sorts by the date when the items were created.
 QualifierExample`sort:created` or `sort:created-desc`[**org:github sort:created**](https://github.com/search?q=org%3Agithub+sort%3Acreated&type=Issues) matches issues in repositories owned by GitHub, sorted by the most recently created date.`sort:created-asc`[**org:github sort:created-asc**](https://github.com/search?q=org%3Agithub+sort%3Acreated-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending created date (oldest to newest). ## [Sort by relevance](#sort-by-relevance)
 The `sort:relevance` qualifier sorts by search relevance.
 QualifierExample`sort:relevance` or `sort:relevance-desc`[**org:github sort:relevance**](https://github.com/search?q=org%3Agithub+sort%3Arelevance&type=Issues) matches issues in repositories owned by GitHub, sorted by highest search relevance. ## [Sort by interactions](#sort-by-interactions)
 The `sort:interactions` qualifier sorts by the highest combined number of reactions and comments.
 QualifierExample`sort:interactions` or `sort:interactions-desc`[**org:github sort:interactions**](https://github.com/search?q=org%3Agithub+sort%3Ainteractions&type=Issues) matches issues in repositories owned by GitHub, sorted by the highest combined number of reactions and comments.`sort:interactions-asc`[**org:github sort:interactions-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Ainteractions-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by the lowest combined number of reactions and comments. ## [Sort by reactions](#sort-by-reactions)
 The `sort:reactions` qualifier sorts by the number or type of reactions.
 QualifierExample`sort:reactions` or `sort:reactions-desc`[**org:github sort:reactions**](https://github.com/search?q=org%3Agithub+sort%3Areactions&type=Issues) matches issues in repositories owned by GitHub, sorted by the highest number of reactions.`sort:reactions-asc`[**org:github sort:reactions-asc**](https://github.com/search?q=org%3Agithub+sort%3Areactions-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending number of reactions (the fewest to the most).`sort:reactions-+1` or `sort:reactions-+1-asc`[**org:github sort:reactions-+1-asc**](https://github.com/search?q=org%3Agithub+sort%3Areactions-%2B1-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending thumbs up (👍) reactions (the fewest to the most).`sort:reactions-+1-desc`[**org:github sort:reactions-+1-desc**](https://github.com/search?q=org%3Agithub+sort%3Areactions-%2B1-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending thumbs up (👍) reactions (the most to the fewest).`sort:reactions--1` or `sort:reactions--1-asc`[**org:github sort:reactions--1-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions--1-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending thumbs down (👎) reactions (the fewest to the most).`sort:reactions--1-desc`[**org:github sort:reactions--1-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions--1-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending thumbs down (👎) reactions (the most to the fewest).`sort:reactions-smile` or `sort:reactions-smile-asc`[**org:github sort:reactions-smile-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-smile-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending laugh (😄) reactions (the fewest to the most).`sort:reactions-smile-desc`[**org:github sort:reactions-smile-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-smile-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending laugh (😄) reactions (the most to the fewest).`sort:reactions-tada` or `sort:reactions-tada-asc`[**org:github sort:reactions-tada-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-tada-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending hurray (🎉) reactions (the fewest to the most).`sort:reactions-tada-desc`[**org:github sort:reactions-tada-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-tada-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending hurray (🎉) reactions (the most to the fewest).`sort:reactions-heart` or `sort:reactions-heart-asc`[**org:github sort:reactions-heart-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-heart-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending heart (❤️) reactions (the fewest to the most).`sort:reactions-heart-desc`[**org:github sort:reactions-heart-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-heart-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending heart (❤️) reactions (the most to the fewest).`sort:reactions-thinking_face` or `sort:reactions-thinking_face-asc`[**org:github sort:reactions-thinking_face-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-thinking_face-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending thinking face (:thinking_face:) reactions (the fewest to the most).`sort:reactions-thinking_face-desc`[**org:github sort:reactions-thinking_face-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-thinking_face-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending thinking face (:thinking_face:) reactions (the most to the fewest).`sort:reactions-rocket` or `sort:reactions-rocket-asc`[**org:github sort:reactions-rocket-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-rocket-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending rocket (🚀) reactions (the fewest to the most).`sort:reactions-rocket-desc`[**org:github sort:reactions-rocket-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-rocket-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending rocket (🚀) reactions (the most to the fewest).`sort:reactions-eyes` or `sort:reactions-eyes-asc`[**org:github sort:reactions-eyes-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-eyes-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending eyes (👀) reactions (the fewest to the most).`sort:reactions-eyes-desc`[**org:github sort:reactions-eyes-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-eyes-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending eyes (👀) reactions (the most to the fewest). ## [Sort by author date](#sort-by-author-date)
 The `sort:author-date` qualifier sorts by descending or ascending author date.
 QualifierExample`sort:author-date` or `sort:author-date-desc`[**feature org:github sort:author-date**](https://github.com/search?utf8=%E2%9C%93&q=feature+org%3Agithub+sort%3Aauthor-date&type=Commits) matches commits containing the word "feature" in repositories owned by GitHub, sorted by descending author date.`sort:author-date-asc`[**`feature org:github sort:author-date-asc`**](https://github.com/search?utf8=%E2%9C%93&q=feature+org%3Agithub+sort%3Aauthor-date-asc&type=Commits) matches commits containing the word "feature" in repositories owned by GitHub, sorted by ascending author date. ## [Sort by committer date](#sort-by-committer-date)
 The `sort:committer-date` qualifier sorts by descending or ascending committer date.
 QualifierExample`sort:committer-date` or `sort:committer-date-desc`[**feature org:github sort:committer-date**](https://github.com/search?utf8=%E2%9C%93&q=feature+org%3Agithub+sort%3Acommitter-date&type=Commits) matches commits containing the word "feature" in repositories owned by GitHub, sorted by descending committer date.`sort:committer-date-asc`[**`feature org:github sort:committer-date-asc`**](https://github.com/search?utf8=%E2%9C%93&q=feature+org%3Agithub+sort%3Acommitter-date-asc&type=Commits) matches commits containing the word "feature" in repositories owned by GitHub, sorted by ascending committer date. ## [Sort by updated date](#sort-by-updated-date)
 The `sort:updated` qualifier sorts by how recently the items were updated.
 QualifierExample`sort:updated` or `sort:updated-desc`[**feature sort:updated**](https://github.com/search?utf8=%E2%9C%93&q=feature+sort%3Aupdated&type=Repositories) matches repositories containing the word "feature," sorted by most recently updated date.`sort:updated-asc`[**feature sort:updated-asc**](https://github.com/search?utf8=%E2%9C%93&q=feature+sort%3Aupdated-asc&type=Repositories) matches repositories containing the word "feature," sorted by least recently updated date. ## [Further reading](#further-reading)
 - [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github)
- [Filtering and searching issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/filtering-and-searching-issues-and-pull-requests)## Help and support
### Did you find what you needed?
YesNo
[Privacy policy](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
### Help us make these docs great!
All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.
[Make a contribution](https://github.com/github/docs/blob/main/content/search-github/getting-started-with-searching-on-github/sorting-search-results.md)
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

*选择时间: 2026/5/12 13:36:09*

---

## 选择区域 2

**来源页面:** [Sorting search results - GitHub Docs](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)

**选择器信息:**
- XPath: `//*[@id="main-content"]/div[1]/div[2]`
- CSS Selector: `#main-content > div.container-xl.px-3.px-md-6.my-4 > div.ArticleGridLayout_containerBox__lLLio.md-selector-preview.md-selector-highlight:nth-of-type(2)`

# Sorting search results
You can sort GitHub search results using the Sort menu, or by adding a `sort` qualifier to your query.
Copy as Markdown
## In this article
- [Sort by comments](#sort-by-comments)
- [Sort by created date](#sort-by-created-date)
- [Sort by relevance](#sort-by-relevance)
- [Sort by interactions](#sort-by-interactions)
- [Sort by reactions](#sort-by-reactions)
- [Sort by author date](#sort-by-author-date)
- [Sort by committer date](#sort-by-committer-date)
- [Sort by updated date](#sort-by-updated-date)
- [Further reading](#further-reading)
Note
 Sorting search results is not supported for GitHub code search. For more information on code search, see [About GitHub Code Search](https://docs.github.com/en/search-github/github-code-search/about-github-code-search).
 Use the **Sort** dropdown menu to sort results by relevance, number of stars, number of forks, and how recently the items were updated.
 To sort by interactions, reactions, comments, created date, relevance, author date, committer date, or how recently the items were updated, you can add a `sort` qualifier to your search query.
 ## [Sort by comments](#sort-by-comments)
 The `sort:comments` qualifier sorts by the number of comments.
 QualifierExample`sort:comments` or `sort:comments-desc`[**org:github sort:comments**](https://github.com/search?q=org%3Agithub+sort%3Acomments&type=Issues) matches issues in repositories owned by GitHub, sorted by the highest number of comments.`sort:comments-asc`[**org:github sort:comments-asc**](https://github.com/search?q=org%3Agithub+sort%3Acomments-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending number of comments (the fewest to the most). ## [Sort by created date](#sort-by-created-date)
 The `sort:created` qualifier sorts by the date when the items were created.
 QualifierExample`sort:created` or `sort:created-desc`[**org:github sort:created**](https://github.com/search?q=org%3Agithub+sort%3Acreated&type=Issues) matches issues in repositories owned by GitHub, sorted by the most recently created date.`sort:created-asc`[**org:github sort:created-asc**](https://github.com/search?q=org%3Agithub+sort%3Acreated-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending created date (oldest to newest). ## [Sort by relevance](#sort-by-relevance)
 The `sort:relevance` qualifier sorts by search relevance.
 QualifierExample`sort:relevance` or `sort:relevance-desc`[**org:github sort:relevance**](https://github.com/search?q=org%3Agithub+sort%3Arelevance&type=Issues) matches issues in repositories owned by GitHub, sorted by highest search relevance. ## [Sort by interactions](#sort-by-interactions)
 The `sort:interactions` qualifier sorts by the highest combined number of reactions and comments.
 QualifierExample`sort:interactions` or `sort:interactions-desc`[**org:github sort:interactions**](https://github.com/search?q=org%3Agithub+sort%3Ainteractions&type=Issues) matches issues in repositories owned by GitHub, sorted by the highest combined number of reactions and comments.`sort:interactions-asc`[**org:github sort:interactions-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Ainteractions-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by the lowest combined number of reactions and comments. ## [Sort by reactions](#sort-by-reactions)
 The `sort:reactions` qualifier sorts by the number or type of reactions.
 QualifierExample`sort:reactions` or `sort:reactions-desc`[**org:github sort:reactions**](https://github.com/search?q=org%3Agithub+sort%3Areactions&type=Issues) matches issues in repositories owned by GitHub, sorted by the highest number of reactions.`sort:reactions-asc`[**org:github sort:reactions-asc**](https://github.com/search?q=org%3Agithub+sort%3Areactions-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending number of reactions (the fewest to the most).`sort:reactions-+1` or `sort:reactions-+1-asc`[**org:github sort:reactions-+1-asc**](https://github.com/search?q=org%3Agithub+sort%3Areactions-%2B1-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending thumbs up (👍) reactions (the fewest to the most).`sort:reactions-+1-desc`[**org:github sort:reactions-+1-desc**](https://github.com/search?q=org%3Agithub+sort%3Areactions-%2B1-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending thumbs up (👍) reactions (the most to the fewest).`sort:reactions--1` or `sort:reactions--1-asc`[**org:github sort:reactions--1-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions--1-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending thumbs down (👎) reactions (the fewest to the most).`sort:reactions--1-desc`[**org:github sort:reactions--1-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions--1-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending thumbs down (👎) reactions (the most to the fewest).`sort:reactions-smile` or `sort:reactions-smile-asc`[**org:github sort:reactions-smile-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-smile-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending laugh (😄) reactions (the fewest to the most).`sort:reactions-smile-desc`[**org:github sort:reactions-smile-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-smile-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending laugh (😄) reactions (the most to the fewest).`sort:reactions-tada` or `sort:reactions-tada-asc`[**org:github sort:reactions-tada-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-tada-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending hurray (🎉) reactions (the fewest to the most).`sort:reactions-tada-desc`[**org:github sort:reactions-tada-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-tada-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending hurray (🎉) reactions (the most to the fewest).`sort:reactions-heart` or `sort:reactions-heart-asc`[**org:github sort:reactions-heart-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-heart-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending heart (❤️) reactions (the fewest to the most).`sort:reactions-heart-desc`[**org:github sort:reactions-heart-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-heart-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending heart (❤️) reactions (the most to the fewest).`sort:reactions-thinking_face` or `sort:reactions-thinking_face-asc`[**org:github sort:reactions-thinking_face-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-thinking_face-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending thinking face (:thinking_face:) reactions (the fewest to the most).`sort:reactions-thinking_face-desc`[**org:github sort:reactions-thinking_face-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-thinking_face-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending thinking face (:thinking_face:) reactions (the most to the fewest).`sort:reactions-rocket` or `sort:reactions-rocket-asc`[**org:github sort:reactions-rocket-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-rocket-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending rocket (🚀) reactions (the fewest to the most).`sort:reactions-rocket-desc`[**org:github sort:reactions-rocket-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-rocket-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending rocket (🚀) reactions (the most to the fewest).`sort:reactions-eyes` or `sort:reactions-eyes-asc`[**org:github sort:reactions-eyes-asc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-eyes-asc&type=Issues) matches issues in repositories owned by GitHub, sorted by ascending eyes (👀) reactions (the fewest to the most).`sort:reactions-eyes-desc`[**org:github sort:reactions-eyes-desc**](https://github.com/search?utf8=%E2%9C%93&q=org%3Agithub+sort%3Areactions-eyes-desc&type=Issues) matches issues in repositories owned by GitHub, sorted by descending eyes (👀) reactions (the most to the fewest). ## [Sort by author date](#sort-by-author-date)
 The `sort:author-date` qualifier sorts by descending or ascending author date.
 QualifierExample`sort:author-date` or `sort:author-date-desc`[**feature org:github sort:author-date**](https://github.com/search?utf8=%E2%9C%93&q=feature+org%3Agithub+sort%3Aauthor-date&type=Commits) matches commits containing the word "feature" in repositories owned by GitHub, sorted by descending author date.`sort:author-date-asc`[**`feature org:github sort:author-date-asc`**](https://github.com/search?utf8=%E2%9C%93&q=feature+org%3Agithub+sort%3Aauthor-date-asc&type=Commits) matches commits containing the word "feature" in repositories owned by GitHub, sorted by ascending author date. ## [Sort by committer date](#sort-by-committer-date)
 The `sort:committer-date` qualifier sorts by descending or ascending committer date.
 QualifierExample`sort:committer-date` or `sort:committer-date-desc`[**feature org:github sort:committer-date**](https://github.com/search?utf8=%E2%9C%93&q=feature+org%3Agithub+sort%3Acommitter-date&type=Commits) matches commits containing the word "feature" in repositories owned by GitHub, sorted by descending committer date.`sort:committer-date-asc`[**`feature org:github sort:committer-date-asc`**](https://github.com/search?utf8=%E2%9C%93&q=feature+org%3Agithub+sort%3Acommitter-date-asc&type=Commits) matches commits containing the word "feature" in repositories owned by GitHub, sorted by ascending committer date. ## [Sort by updated date](#sort-by-updated-date)
 The `sort:updated` qualifier sorts by how recently the items were updated.
 QualifierExample`sort:updated` or `sort:updated-desc`[**feature sort:updated**](https://github.com/search?utf8=%E2%9C%93&q=feature+sort%3Aupdated&type=Repositories) matches repositories containing the word "feature," sorted by most recently updated date.`sort:updated-asc`[**feature sort:updated-asc**](https://github.com/search?utf8=%E2%9C%93&q=feature+sort%3Aupdated-asc&type=Repositories) matches repositories containing the word "feature," sorted by least recently updated date. ## [Further reading](#further-reading)
 - [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github)
- [Filtering and searching issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/filtering-and-searching-issues-and-pull-requests)

*选择时间: 2026/5/12 13:36:09*

---

## 选择区域 3

**来源页面:** [Sorting search results - GitHub Docs](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)

**选择器信息:**
- XPath: `//*[@id="_r_1d_--label"]`
- CSS Selector: `#_r_1d_--label`

Sorting search results

*选择时间: 2026/5/12 13:36:09*

---

## 选择区域 4

**来源页面:** [Sorting search results - GitHub Docs](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)

**选择器信息:**
- XPath: `//*[@id="_r_6_--label"]`
- CSS Selector: `#_r_6_--label`

Troubleshoot search queries

*选择时间: 2026/5/12 13:36:09*