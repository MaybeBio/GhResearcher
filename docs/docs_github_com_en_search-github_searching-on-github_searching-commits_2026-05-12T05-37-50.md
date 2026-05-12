## 选择区域 1

**来源页面:** [Searching commits - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-commits)

**选择器信息:**
- XPath: `//*[@id="__next"]/div[1]/div[2]/div[2]`
- CSS Selector: `#__next > div > div.d-lg-flex:nth-of-type(2) > div.flex-column.flex-1.min-width-0.md-selector-highlight:nth-of-type(2)`

- [Search on GitHub](https://docs.github.com/en/search-github) /
- [Searching on GitHub](https://docs.github.com/en/search-github/searching-on-github) /
- [Searching commits](https://docs.github.com/en/search-github/searching-on-github/searching-commits)
# Searching commits
You can search for commits on GitHub and narrow the results using these commit search qualifiers in any combination.
Copy as Markdown
## In this article
- [Search within commit messages](#search-within-commit-messages)
- [Search by author or committer](#search-by-author-or-committer)
- [Search by authored or committed date](#search-by-authored-or-committed-date)
- [Filter merge commits](#filter-merge-commits)
- [Search by hash](#search-by-hash)
- [Search by parent](#search-by-parent)
- [Search by tree](#search-by-tree)
- [Search within a user's or organization's repositories](#search-within-a-users-or-organizations-repositories)
- [Filter by repository visibility](#filter-by-repository-visibility)
- [Further reading](#further-reading)
You can search for commits globally across all of GitHub, or search for commits within a particular repository or organization. For more information, see [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github).
 When you search for commits, only the [default branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches) of a repository is searched.
 Tip
  - This article contains links to example searches on the GitHub.com website, but you can use the same search filters in any GitHub platform. In the linked example searches, replace `github.com` with the hostname for your GitHub platform.
- For a list of search syntaxes that you can add to any search qualifier to further improve your results, see [Understanding the search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
- Use quotations around multi-word search terms. For example, if you want to search for issues with the label "In progress," you'd search for `label:"in progress"`. Search is not case sensitive.
 ## [Search within commit messages](#search-within-commit-messages)
 You can find commits that contain particular words in the message. For example, [**fix typo**](https://github.com/search?q=fix+typo&type=Commits) matches commits containing the words "fix" and "typo."
 ## [Search by author or committer](#search-by-author-or-committer)
 You can find commits by a particular user with the `author` or `committer` qualifiers.
 QualifierExample`author:USERNAME`[**author:defunkt**](https://github.com/search?q=author%3Adefunkt&type=Commits) matches commits authored by @defunkt.`committer:USERNAME`[**committer:defunkt**](https://github.com/search?q=committer%3Adefunkt&type=Commits) matches commits committed by @defunkt. The `author-name` and `committer-name` qualifiers match commits by the name of the author or committer.
 QualifierExample`author-name:NAME`[**author-name:wanstrath**](https://github.com/search?q=author-name%3Awanstrath&type=Commits) matches commits with "wanstrath" in the author name.`committer-name:NAME`[**committer-name:wanstrath**](https://github.com/search?q=committer-name%3Awanstrath&type=Commits) matches commits with "wanstrath" in the committer name. The `author-email` and `committer-email` qualifiers match commits by the author's or committer's full email address.
 QualifierExample`author-email:EMAIL`[**author-email:chris@github.com**](https://github.com/search?q=author-email%3Achris%40github.com&type=Commits) matches commits authored by [chris@github.com](mailto:chris@github.com).`committer-email:EMAIL`[**committer-email:chris@github.com**](https://github.com/search?q=committer-email%3Achris%40github.com&type=Commits) matches commits committed by [chris@github.com](mailto:chris@github.com). ## [Search by authored or committed date](#search-by-authored-or-committed-date)
 Use the `author-date` and `committer-date` qualifiers to match commits authored or committed within the specified date range.
 When you search for a date, you can use greater than, less than, and range qualifiers to further filter results. For more information, see [Understanding the search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
 QualifierExample`author-date:YYYY-MM-DD`[**author-date:<2016-01-01**](https://github.com/search?q=author-date%3A%3C2016-01-01&type=Commits) matches commits authored before 2016-01-01.`committer-date:YYYY-MM-DD`[**committer-date:>2016-01-01**](https://github.com/search?q=committer-date%3A%3E2016-01-01&type=Commits) matches commits committed after 2016-01-01. ## [Filter merge commits](#filter-merge-commits)
 The `merge` qualifier filters merge commits.
 QualifierExample`merge:true`[**merge:true**](https://github.com/search?q=merge%3Atrue&type=Commits) matches merge commits.`merge:false`[**merge:false**](https://github.com/search?q=merge%3Afalse&type=Commits) matches non-merge commits. ## [Search by hash](#search-by-hash)
 The `hash` qualifier matches commits with the specified SHA-1 hash.
 QualifierExample`hash:HASH`[**hash:124a9a0ee1d8f1e15e833aff432fbb3b02632105**](https://github.com/github/gitignore/search?q=hash%3A124a9a0ee1d8f1e15e833aff432fbb3b02632105&type=Commits) matches commits with the hash `124a9a0ee1d8f1e15e833aff432fbb3b02632105`. ## [Search by parent](#search-by-parent)
 The `parent` qualifier matches commits whose parent has the specified SHA-1 hash.
 QualifierExample`parent:HASH`[**parent:124a9a0ee1d8f1e15e833aff432fbb3b02632105**](https://github.com/github/gitignore/search?q=parent%3A124a9a0ee1d8f1e15e833aff432fbb3b02632105&type=Commits&utf8=%E2%9C%93) matches children of commits with the hash `124a9a0ee1d8f1e15e833aff432fbb3b02632105`. ## [Search by tree](#search-by-tree)
 The `tree` qualifier matches commits with the specified SHA-1 git tree hash.
 QualifierExample`tree:HASH`[**tree:99ca967**](https://github.com/github/gitignore/search?q=tree%3A99ca967&type=Commits) matches commits that refer to the tree hash `99ca967`. ## [Search within a user's or organization's repositories](#search-within-a-users-or-organizations-repositories)
 To search commits in all repositories owned by a certain user or organization, use the `user` or `org` qualifier. To search commits in a specific repository, use the `repo` qualifier.
 QualifierExample`user:USERNAME`[**gibberish user:defunkt**](https://github.com/search?q=gibberish+user%3Adefunkt&type=Commits&utf8=%E2%9C%93) matches commit messages with the word "gibberish" in repositories owned by @defunkt.`org:ORGNAME`[**test org:github**](https://github.com/search?utf8=%E2%9C%93&q=test+org%3Agithub&type=Commits) matches commit messages with the word "test" in repositories owned by @github.`repo:USERNAME/REPO`[**language repo:defunkt/gibberish**](https://github.com/search?utf8=%E2%9C%93&q=language+repo%3Adefunkt%2Fgibberish&type=Commits) matches commit messages with the word "language" in @defunkt's "gibberish" repository. ## [Filter by repository visibility](#filter-by-repository-visibility)
 The `is` qualifier matches commits from repositories with the specified visibility. For more information, see [About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility).
 QualifierExample`is:public`[**is:public**](https://github.com/search?q=is%3Apublic&type=Commits) matches commits to public repositories.`is:private`[**is:private**](https://github.com/search?q=is%3Aprivate&type=Commits) matches commits to private repositories. ## [Further reading](#further-reading)
 - [Sorting search results](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)## Help and support
### Did you find what you needed?
YesNo
[Privacy policy](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
### Help us make these docs great!
All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.
[Make a contribution](https://github.com/github/docs/blob/main/content/search-github/searching-on-github/searching-commits.md)
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

*选择时间: 2026/5/12 13:37:48*

---

## 选择区域 2

**来源页面:** [Searching commits - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-commits)

**选择器信息:**
- XPath: `//*[@id="main-content"]/div[1]/div[2]`
- CSS Selector: `#main-content > div.container-xl.px-3.px-md-6.my-4 > div.ArticleGridLayout_containerBox__lLLio.md-selector-preview.md-selector-highlight:nth-of-type(2)`

# Searching commits
You can search for commits on GitHub and narrow the results using these commit search qualifiers in any combination.
Copy as Markdown
## In this article
- [Search within commit messages](#search-within-commit-messages)
- [Search by author or committer](#search-by-author-or-committer)
- [Search by authored or committed date](#search-by-authored-or-committed-date)
- [Filter merge commits](#filter-merge-commits)
- [Search by hash](#search-by-hash)
- [Search by parent](#search-by-parent)
- [Search by tree](#search-by-tree)
- [Search within a user's or organization's repositories](#search-within-a-users-or-organizations-repositories)
- [Filter by repository visibility](#filter-by-repository-visibility)
- [Further reading](#further-reading)
You can search for commits globally across all of GitHub, or search for commits within a particular repository or organization. For more information, see [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github).
 When you search for commits, only the [default branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches) of a repository is searched.
 Tip
  - This article contains links to example searches on the GitHub.com website, but you can use the same search filters in any GitHub platform. In the linked example searches, replace `github.com` with the hostname for your GitHub platform.
- For a list of search syntaxes that you can add to any search qualifier to further improve your results, see [Understanding the search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
- Use quotations around multi-word search terms. For example, if you want to search for issues with the label "In progress," you'd search for `label:"in progress"`. Search is not case sensitive.
 ## [Search within commit messages](#search-within-commit-messages)
 You can find commits that contain particular words in the message. For example, [**fix typo**](https://github.com/search?q=fix+typo&type=Commits) matches commits containing the words "fix" and "typo."
 ## [Search by author or committer](#search-by-author-or-committer)
 You can find commits by a particular user with the `author` or `committer` qualifiers.
 QualifierExample`author:USERNAME`[**author:defunkt**](https://github.com/search?q=author%3Adefunkt&type=Commits) matches commits authored by @defunkt.`committer:USERNAME`[**committer:defunkt**](https://github.com/search?q=committer%3Adefunkt&type=Commits) matches commits committed by @defunkt. The `author-name` and `committer-name` qualifiers match commits by the name of the author or committer.
 QualifierExample`author-name:NAME`[**author-name:wanstrath**](https://github.com/search?q=author-name%3Awanstrath&type=Commits) matches commits with "wanstrath" in the author name.`committer-name:NAME`[**committer-name:wanstrath**](https://github.com/search?q=committer-name%3Awanstrath&type=Commits) matches commits with "wanstrath" in the committer name. The `author-email` and `committer-email` qualifiers match commits by the author's or committer's full email address.
 QualifierExample`author-email:EMAIL`[**author-email:chris@github.com**](https://github.com/search?q=author-email%3Achris%40github.com&type=Commits) matches commits authored by [chris@github.com](mailto:chris@github.com).`committer-email:EMAIL`[**committer-email:chris@github.com**](https://github.com/search?q=committer-email%3Achris%40github.com&type=Commits) matches commits committed by [chris@github.com](mailto:chris@github.com). ## [Search by authored or committed date](#search-by-authored-or-committed-date)
 Use the `author-date` and `committer-date` qualifiers to match commits authored or committed within the specified date range.
 When you search for a date, you can use greater than, less than, and range qualifiers to further filter results. For more information, see [Understanding the search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
 QualifierExample`author-date:YYYY-MM-DD`[**author-date:<2016-01-01**](https://github.com/search?q=author-date%3A%3C2016-01-01&type=Commits) matches commits authored before 2016-01-01.`committer-date:YYYY-MM-DD`[**committer-date:>2016-01-01**](https://github.com/search?q=committer-date%3A%3E2016-01-01&type=Commits) matches commits committed after 2016-01-01. ## [Filter merge commits](#filter-merge-commits)
 The `merge` qualifier filters merge commits.
 QualifierExample`merge:true`[**merge:true**](https://github.com/search?q=merge%3Atrue&type=Commits) matches merge commits.`merge:false`[**merge:false**](https://github.com/search?q=merge%3Afalse&type=Commits) matches non-merge commits. ## [Search by hash](#search-by-hash)
 The `hash` qualifier matches commits with the specified SHA-1 hash.
 QualifierExample`hash:HASH`[**hash:124a9a0ee1d8f1e15e833aff432fbb3b02632105**](https://github.com/github/gitignore/search?q=hash%3A124a9a0ee1d8f1e15e833aff432fbb3b02632105&type=Commits) matches commits with the hash `124a9a0ee1d8f1e15e833aff432fbb3b02632105`. ## [Search by parent](#search-by-parent)
 The `parent` qualifier matches commits whose parent has the specified SHA-1 hash.
 QualifierExample`parent:HASH`[**parent:124a9a0ee1d8f1e15e833aff432fbb3b02632105**](https://github.com/github/gitignore/search?q=parent%3A124a9a0ee1d8f1e15e833aff432fbb3b02632105&type=Commits&utf8=%E2%9C%93) matches children of commits with the hash `124a9a0ee1d8f1e15e833aff432fbb3b02632105`. ## [Search by tree](#search-by-tree)
 The `tree` qualifier matches commits with the specified SHA-1 git tree hash.
 QualifierExample`tree:HASH`[**tree:99ca967**](https://github.com/github/gitignore/search?q=tree%3A99ca967&type=Commits) matches commits that refer to the tree hash `99ca967`. ## [Search within a user's or organization's repositories](#search-within-a-users-or-organizations-repositories)
 To search commits in all repositories owned by a certain user or organization, use the `user` or `org` qualifier. To search commits in a specific repository, use the `repo` qualifier.
 QualifierExample`user:USERNAME`[**gibberish user:defunkt**](https://github.com/search?q=gibberish+user%3Adefunkt&type=Commits&utf8=%E2%9C%93) matches commit messages with the word "gibberish" in repositories owned by @defunkt.`org:ORGNAME`[**test org:github**](https://github.com/search?utf8=%E2%9C%93&q=test+org%3Agithub&type=Commits) matches commit messages with the word "test" in repositories owned by @github.`repo:USERNAME/REPO`[**language repo:defunkt/gibberish**](https://github.com/search?utf8=%E2%9C%93&q=language+repo%3Adefunkt%2Fgibberish&type=Commits) matches commit messages with the word "language" in @defunkt's "gibberish" repository. ## [Filter by repository visibility](#filter-by-repository-visibility)
 The `is` qualifier matches commits from repositories with the specified visibility. For more information, see [About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility).
 QualifierExample`is:public`[**is:public**](https://github.com/search?q=is%3Apublic&type=Commits) matches commits to public repositories.`is:private`[**is:private**](https://github.com/search?q=is%3Aprivate&type=Commits) matches commits to private repositories. ## [Further reading](#further-reading)
 - [Sorting search results](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)

*选择时间: 2026/5/12 13:37:48*

---

## 选择区域 3

**来源页面:** [Searching commits - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-commits)

**选择器信息:**
- XPath: `//*[@id="_r_1d_--label"]`
- CSS Selector: `#_r_1d_--label`

Sorting search results

*选择时间: 2026/5/12 13:37:48*

---

## 选择区域 4

**来源页面:** [Searching commits - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-commits)

**选择器信息:**
- XPath: `//*[@id="_r_6_--label"]`
- CSS Selector: `#_r_6_--label`

Troubleshoot search queries

*选择时间: 2026/5/12 13:37:48*