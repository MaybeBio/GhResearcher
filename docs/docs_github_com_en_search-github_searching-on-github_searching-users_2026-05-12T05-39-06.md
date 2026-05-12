## 选择区域 1

**来源页面:** [Searching users - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-users)

**选择器信息:**
- XPath: `//*[@id="_r_dp_--label"]`
- CSS Selector: `#_r_dp_--label`

Search GitHub Models

*选择时间: 2026/5/12 13:39:05*

---

## 选择区域 2

**来源页面:** [Searching users - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-users)

**选择器信息:**
- XPath: `//*[@id="__next"]/div[1]/div[2]/div[2]`
- CSS Selector: `#__next > div > div.d-lg-flex:nth-of-type(2) > div.flex-column.flex-1.min-width-0.md-selector-highlight:nth-of-type(2)`

- [Search on GitHub](https://docs.github.com/en/search-github) /
- [Searching on GitHub](https://docs.github.com/en/search-github/searching-on-github) /
- [Searching users](https://docs.github.com/en/search-github/searching-on-github/searching-users)
# Searching users
You can search for users on GitHub and narrow the results using these user search qualifiers in any combination.
Copy as Markdown
## In this article
- [Search only users or organizations](#search-only-users-or-organizations)
- [Search by account name, full name, or public email](#search-by-account-name-full-name-or-public-email)
- [Search by number of repositories a user owns](#search-by-number-of-repositories-a-user-owns)
- [Search by location](#search-by-location)
- [Search by repository language](#search-by-repository-language)
- [Search by when a personal account was created](#search-by-when-a-personal-account-was-created)
- [Search by number of followers](#search-by-number-of-followers)
- [Search based on ability to sponsor](#search-based-on-ability-to-sponsor)
- [Further reading](#further-reading)
You can search for users globally across a GitHub platform, for example: across GitHub.com or across GitHub Enterprise Server.
 For more information, see [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github).
 Tip
  - This article contains links to example searches on the GitHub.com website, but you can use the same search filters in any GitHub platform. In the linked example searches, replace `github.com` with the hostname for your GitHub platform.
- For a list of search syntaxes that you can add to any search qualifier to further improve your results, see [Understanding the search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
- Use quotations around multi-word search terms. For example, if you want to search for issues with the label "In progress," you'd search for `label:"in progress"`. Search is not case sensitive.
 ## [Search only users or organizations](#search-only-users-or-organizations)
 By default, searching users will return both personal and organizations. However, you can use the `type` qualifier to restrict search results to personal accounts or organizations only.
 QualifierExample`type:user`[**mike in:name created:<2011-01-01 type:user**](https://github.com/search?q=mike+in:name+created%3A%3C2011-01-01+type%3Auser&type=Users) matches personal accounts named "mike" that were created before 2011.`type:org`[**data in:email type:org**](https://github.com/search?q=data+in%3Aemail+type%3Aorg&type=Users) matches organizations with the word "data" in their email. ## [Search by account name, full name, or public email](#search-by-account-name-full-name-or-public-email)
 You can filter your search to the personal user or organization account name with `user` or `org` qualifiers.
 With the `in` qualifier you can restrict your search to the username ( `login`), full name, public email, or any combination of these. When you omit this qualifier, only the username and email address are searched. For privacy reasons, you cannot search by email domain name.
 QualifierExample`user:name`[**user:octocat**](https://github.com/search?q=user%3Aoctocat&type=Users) matches the user with the username "octocat".`org:name`[**org:electron type:user**](https://github.com/search?q=org%3Aelectron+type%3Ausers&type=User) matches the Electron organization's account name.`in:login`[**kenya in:login**](https://github.com/search?q=kenya+in%3Alogin&type=Users) matches users with the word "kenya" in their username.`in:name`[**bolton in:name**](https://github.com/search?q=bolton+in%3Afullname&type=Users) matches users whose real name contains the word "bolton."`fullname:firstname lastname`[**fullname:nat friedman**](https://github.com/search?q=fullname%3Anat+friedman&type=Users) matches a user with the full name "Nat Friedman." Note: This search qualifier is sensitive to spacing.`in:email`[**data in:email**](https://github.com/search?q=data+in%3Aemail&type=Users&utf8=%E2%9C%93) matches users with the word "data" in their email. ## [Search by number of repositories a user owns](#search-by-number-of-repositories-a-user-owns)
 You can filter users based on the number of repositories they own, using the `repos` qualifier and [greater than, less than, and range qualifiers](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
 QualifierExample`repos:n`[**repos:>9000**](https://github.com/search?q=repos%3A%3E%3D9000&type=Users) matches users whose repository count is over 9,000.*`name`* `repos:n`[**bert repos:10..30**](https://github.com/search?q=bert+repos%3A10..30&type=Users) matches users with the word "bert" in their username or real name who own 10 to 30 repositories. ## [Search by location](#search-by-location)
 You can search for users by the location indicated in their profile.
 QualifierExample`location:LOCATION`[**repos:1 location:iceland**](https://github.com/search?q=repos%3A1+location%3Aiceland&type=Users) matches users with exactly one repository that live in Iceland. ## [Search by repository language](#search-by-repository-language)
 Using the `language` qualifier you can search for users based on the languages of repositories they own.
 QualifierExample`language:LANGUAGE` `location:LOCATION`[**language:javascript location:russia**](https://github.com/search?q=language%3Ajavascript+location%3Arussia&type=Users) matches users in Russia with a majority of their repositories written in JavaScript.*`name`* `language:LANGUAGE` `in:fullname`[**jenny language:javascript in:fullname**](https://github.com/search?q=jenny+language%3Ajavascript+in%3Afullname&type=Users) matches users with JavaScript repositories whose full name contains the word "jenny." ## [Search by when a personal account was created](#search-by-when-a-personal-account-was-created)
 You can filter users based on when they joined GitHub with the `created` qualifier. This takes a date as its parameter. Date formatting must follow the [ISO8601](http://en.wikipedia.org/wiki/ISO_8601) standard, which is `YYYY-MM-DD` (year-month-day). You can also add optional time information `THH:MM:SS+00:00` after the date, to search by the hour, minute, and second. That's `T`, followed by `HH:MM:SS` (hour-minutes-seconds), and a UTC offset ( `+00:00`).
 When you search for a date, you can use greater than, less than, and range qualifiers to further filter results. For more information, see [Understanding the search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
 QualifierExample`created:YYYY-MM-DD`[**created:<2011-01-01**](https://github.com/search?q=created%3A%3C2011-01-01&type=Users) matches users that joined before 2011.`created:>=YYYY-MM-DD`[**created:>=2013-05-11**](https://github.com/search?q=created%3A%3E%3D2013-05-11&type=Users) matches users that joined at or after May 11th, 2013.`created:YYYY-MM-DD` `location:LOCATION`[**created:2013-03-06 location:london**](https://github.com/search?q=created%3A2013-03-06+location%3Alondon&type=Users) matches users that joined on March 6th, 2013, who list their location as London.`created:YYYY-MM-DD..YYYY-MM-DD` *`name`* `in:login`[**created:2010-01-01..2011-01-01 john in:login**](https://github.com/search?q=created%3A2010-01-01..2011-01-01+john+in%3Ausername&type=Users) matches users that joined between 2010 and 2011 with the word "john" in their username. ## [Search by number of followers](#search-by-number-of-followers)
 You can filter users based on the number of followers that they have, using the `followers` qualifier with [greater than, less than, and range qualifiers](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
 QualifierExample`followers:n`[**followers:>=1000**](https://github.com/search?q=followers%3A%3E%3D1000&type=Users) matches users with 1,000 or more followers.*`name`* `followers:n`[**sparkle followers:1..10**](https://github.com/search?q=sparkle+followers%3A1..10&type=Users) matches users with between 1 and 10 followers, with the word "sparkle" in their name. ## [Search based on ability to sponsor](#search-based-on-ability-to-sponsor)
 You can search for users and organizations who can be sponsored on GitHub Sponsors with the `is:sponsorable` qualifier. For more information, see [About GitHub Sponsors](https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors).
 QualifierExample`is:sponsorable`[**is:sponsorable**](https://github.com/search?q=is%3Asponsorable&type=Users) matches users and organizations who have a GitHub Sponsors profile. ## [Further reading](#further-reading)
 - [Sorting search results](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)## Help and support
### Did you find what you needed?
YesNo
[Privacy policy](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
### Help us make these docs great!
All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.
[Make a contribution](https://github.com/github/docs/blob/main/content/search-github/searching-on-github/searching-users.md)
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

*选择时间: 2026/5/12 13:39:05*

---

## 选择区域 3

**来源页面:** [Searching users - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-users)

**选择器信息:**
- XPath: `//*[@id="main-content"]/div[1]/div[2]`
- CSS Selector: `#main-content > div.container-xl.px-3.px-md-6.my-4 > div.ArticleGridLayout_containerBox__lLLio.md-selector-preview.md-selector-highlight:nth-of-type(2)`

# Searching users
You can search for users on GitHub and narrow the results using these user search qualifiers in any combination.
Copy as Markdown
## In this article
- [Search only users or organizations](#search-only-users-or-organizations)
- [Search by account name, full name, or public email](#search-by-account-name-full-name-or-public-email)
- [Search by number of repositories a user owns](#search-by-number-of-repositories-a-user-owns)
- [Search by location](#search-by-location)
- [Search by repository language](#search-by-repository-language)
- [Search by when a personal account was created](#search-by-when-a-personal-account-was-created)
- [Search by number of followers](#search-by-number-of-followers)
- [Search based on ability to sponsor](#search-based-on-ability-to-sponsor)
- [Further reading](#further-reading)
You can search for users globally across a GitHub platform, for example: across GitHub.com or across GitHub Enterprise Server.
 For more information, see [About searching on GitHub](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github).
 Tip
  - This article contains links to example searches on the GitHub.com website, but you can use the same search filters in any GitHub platform. In the linked example searches, replace `github.com` with the hostname for your GitHub platform.
- For a list of search syntaxes that you can add to any search qualifier to further improve your results, see [Understanding the search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
- Use quotations around multi-word search terms. For example, if you want to search for issues with the label "In progress," you'd search for `label:"in progress"`. Search is not case sensitive.
 ## [Search only users or organizations](#search-only-users-or-organizations)
 By default, searching users will return both personal and organizations. However, you can use the `type` qualifier to restrict search results to personal accounts or organizations only.
 QualifierExample`type:user`[**mike in:name created:<2011-01-01 type:user**](https://github.com/search?q=mike+in:name+created%3A%3C2011-01-01+type%3Auser&type=Users) matches personal accounts named "mike" that were created before 2011.`type:org`[**data in:email type:org**](https://github.com/search?q=data+in%3Aemail+type%3Aorg&type=Users) matches organizations with the word "data" in their email. ## [Search by account name, full name, or public email](#search-by-account-name-full-name-or-public-email)
 You can filter your search to the personal user or organization account name with `user` or `org` qualifiers.
 With the `in` qualifier you can restrict your search to the username ( `login`), full name, public email, or any combination of these. When you omit this qualifier, only the username and email address are searched. For privacy reasons, you cannot search by email domain name.
 QualifierExample`user:name`[**user:octocat**](https://github.com/search?q=user%3Aoctocat&type=Users) matches the user with the username "octocat".`org:name`[**org:electron type:user**](https://github.com/search?q=org%3Aelectron+type%3Ausers&type=User) matches the Electron organization's account name.`in:login`[**kenya in:login**](https://github.com/search?q=kenya+in%3Alogin&type=Users) matches users with the word "kenya" in their username.`in:name`[**bolton in:name**](https://github.com/search?q=bolton+in%3Afullname&type=Users) matches users whose real name contains the word "bolton."`fullname:firstname lastname`[**fullname:nat friedman**](https://github.com/search?q=fullname%3Anat+friedman&type=Users) matches a user with the full name "Nat Friedman." Note: This search qualifier is sensitive to spacing.`in:email`[**data in:email**](https://github.com/search?q=data+in%3Aemail&type=Users&utf8=%E2%9C%93) matches users with the word "data" in their email. ## [Search by number of repositories a user owns](#search-by-number-of-repositories-a-user-owns)
 You can filter users based on the number of repositories they own, using the `repos` qualifier and [greater than, less than, and range qualifiers](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
 QualifierExample`repos:n`[**repos:>9000**](https://github.com/search?q=repos%3A%3E%3D9000&type=Users) matches users whose repository count is over 9,000.*`name`* `repos:n`[**bert repos:10..30**](https://github.com/search?q=bert+repos%3A10..30&type=Users) matches users with the word "bert" in their username or real name who own 10 to 30 repositories. ## [Search by location](#search-by-location)
 You can search for users by the location indicated in their profile.
 QualifierExample`location:LOCATION`[**repos:1 location:iceland**](https://github.com/search?q=repos%3A1+location%3Aiceland&type=Users) matches users with exactly one repository that live in Iceland. ## [Search by repository language](#search-by-repository-language)
 Using the `language` qualifier you can search for users based on the languages of repositories they own.
 QualifierExample`language:LANGUAGE` `location:LOCATION`[**language:javascript location:russia**](https://github.com/search?q=language%3Ajavascript+location%3Arussia&type=Users) matches users in Russia with a majority of their repositories written in JavaScript.*`name`* `language:LANGUAGE` `in:fullname`[**jenny language:javascript in:fullname**](https://github.com/search?q=jenny+language%3Ajavascript+in%3Afullname&type=Users) matches users with JavaScript repositories whose full name contains the word "jenny." ## [Search by when a personal account was created](#search-by-when-a-personal-account-was-created)
 You can filter users based on when they joined GitHub with the `created` qualifier. This takes a date as its parameter. Date formatting must follow the [ISO8601](http://en.wikipedia.org/wiki/ISO_8601) standard, which is `YYYY-MM-DD` (year-month-day). You can also add optional time information `THH:MM:SS+00:00` after the date, to search by the hour, minute, and second. That's `T`, followed by `HH:MM:SS` (hour-minutes-seconds), and a UTC offset ( `+00:00`).
 When you search for a date, you can use greater than, less than, and range qualifiers to further filter results. For more information, see [Understanding the search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
 QualifierExample`created:YYYY-MM-DD`[**created:<2011-01-01**](https://github.com/search?q=created%3A%3C2011-01-01&type=Users) matches users that joined before 2011.`created:>=YYYY-MM-DD`[**created:>=2013-05-11**](https://github.com/search?q=created%3A%3E%3D2013-05-11&type=Users) matches users that joined at or after May 11th, 2013.`created:YYYY-MM-DD` `location:LOCATION`[**created:2013-03-06 location:london**](https://github.com/search?q=created%3A2013-03-06+location%3Alondon&type=Users) matches users that joined on March 6th, 2013, who list their location as London.`created:YYYY-MM-DD..YYYY-MM-DD` *`name`* `in:login`[**created:2010-01-01..2011-01-01 john in:login**](https://github.com/search?q=created%3A2010-01-01..2011-01-01+john+in%3Ausername&type=Users) matches users that joined between 2010 and 2011 with the word "john" in their username. ## [Search by number of followers](#search-by-number-of-followers)
 You can filter users based on the number of followers that they have, using the `followers` qualifier with [greater than, less than, and range qualifiers](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).
 QualifierExample`followers:n`[**followers:>=1000**](https://github.com/search?q=followers%3A%3E%3D1000&type=Users) matches users with 1,000 or more followers.*`name`* `followers:n`[**sparkle followers:1..10**](https://github.com/search?q=sparkle+followers%3A1..10&type=Users) matches users with between 1 and 10 followers, with the word "sparkle" in their name. ## [Search based on ability to sponsor](#search-based-on-ability-to-sponsor)
 You can search for users and organizations who can be sponsored on GitHub Sponsors with the `is:sponsorable` qualifier. For more information, see [About GitHub Sponsors](https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors).
 QualifierExample`is:sponsorable`[**is:sponsorable**](https://github.com/search?q=is%3Asponsorable&type=Users) matches users and organizations who have a GitHub Sponsors profile. ## [Further reading](#further-reading)
 - [Sorting search results](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)

*选择时间: 2026/5/12 13:39:05*

---

## 选择区域 4

**来源页面:** [Searching users - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-users)

**选择器信息:**
- XPath: `//*[@id="_r_1d_--label"]`
- CSS Selector: `#_r_1d_--label`

Sorting search results

*选择时间: 2026/5/12 13:39:05*

---

## 选择区域 5

**来源页面:** [Searching users - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-users)

**选择器信息:**
- XPath: `//*[@id="_r_6_--label"]`
- CSS Selector: `#_r_6_--label`

Troubleshoot search queries

*选择时间: 2026/5/12 13:39:05*