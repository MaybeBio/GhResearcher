## 选择区域 1

**来源页面:** [Searching GitHub Models - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-github-models)

**选择器信息:**
- XPath: `//*[@id="_r_dp_--label"]`
- CSS Selector: `#_r_dp_--label`

Search GitHub Models

*选择时间: 2026/5/12 13:38:49*

---

## 选择区域 2

**来源页面:** [Searching GitHub Models - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-github-models)

**选择器信息:**
- XPath: `//*[@id="__next"]/div[1]/div[2]/div[2]`
- CSS Selector: `#__next > div > div.d-lg-flex:nth-of-type(2) > div.flex-column.flex-1.min-width-0.md-selector-highlight:nth-of-type(2)`

- [Search on GitHub](https://docs.github.com/en/search-github) /
- [Searching on GitHub](https://docs.github.com/en/search-github/searching-on-github) /
- [Search GitHub Models](https://docs.github.com/en/search-github/searching-on-github/searching-github-models)
# Searching GitHub Models
You can search for models that are available on GitHub Models.
Copy as Markdown
## In this article
- [About searching GitHub Models](#about-searching-github-models)
- [Searching in GitHub Marketplace](#searching-in-github-marketplace)
- [Searching across GitHub](#searching-across-github)
- [Searching within a specific field](#searching-within-a-specific-field)
- [Search by category](#search-by-category)
- [Search by input modality](#search-by-input-modality)
- [Search by output modality](#search-by-output-modality)
- [Search by language](#search-by-language)
- [Search by task](#search-by-task)
- [Search by publisher](#search-by-publisher)
- [Search by input token limit](#search-by-input-token-limit)
- [Search by output token limit](#search-by-output-token-limit)
- [Search by rate limit tier](#search-by-rate-limit-tier)
- [Search by license type](#search-by-license-type)
- [Sorting results](#sorting-results)
- [Further reading](#further-reading)
## [About searching GitHub Models](#about-searching-github-models)
 You can find models on GitHub Models in two ways:
 - Search from GitHub Marketplace.
- Search across all of GitHub and then filter the results to Marketplace.
 ## [Searching in GitHub Marketplace](#searching-in-github-marketplace)
 1. To open GitHub Marketplace, in the top-left corner of GitHub, select , then click **Marketplace**.
 ![Screenshot of the navigation bar on GitHub. The "Open global navigation menu" icon is outlined in dark orange.](https://docs.github.com/assets/cb-2683/images/help/navigation/global-navigation-menu-icon.png)
2. Type any keywords and `type:models` and press **Enter**.
 ## [Searching across GitHub](#searching-across-github)
 Anytime you search across all of GitHub, you can filter the results to see matching models from GitHub Marketplace.
 1. Navigate to [https://github.com/search](https://github.com/search).
2. Type any keywords and press **Enter**.
3. To see all available filters for your search, in the "Filter by" sidebar, click **More**.
4. To see results from GitHub Models, click **Marketplace**.
 ## [Searching within a specific field](#searching-within-a-specific-field)
 The `in` qualifier used in conjunction with search text finds models that match the specified text in that field. Possible fields include `tags`, `license`, `name`, `description`, `transparency`, and `task`.
 QualifierExample`in:FIELD`[**in:tags agents**](https://github.com/search?q=in:tags+agents&type=marketplace) matches models with the 'agents' tag.`in:FIELD`[**in:license distribute**](https://github.com/search?q=in:license+distribute&type=marketplace) matches models who mention 'distribute' in their license.`in:FIELD`[**in:transparency "responsible ai"**](https://github.com/search?q=in:transparency+%22responsible+ai%22&type=marketplace) matches models who mention 'responsible ai' in their transparency information. ## [Search by category](#search-by-category)
 The `category` qualifier finds models that are tagged with a specific term.
 QualifierExample`category:CATEGORY`[**category:multilingual**](https://github.com/search?q=category:multilingual&type=marketplace) matches models in the multilingual category.`category:CATEGORY`[**category:"large context"**](https://github.com/search?q=category:%22large+context%22+&type=marketplace) matches models in the large context category. ## [Search by input modality](#search-by-input-modality)
 The `input-modality` qualifier finds models that support a particular medium for providing input. Possible modalities include `text`, `image`, and `audio`.
 QualifierExample`input-modality:MODALITY`[**input-modality:text**](https://github.com/search?q=input-modality:text&type=marketplace) matches models that support text input. ## [Search by output modality](#search-by-output-modality)
 The `output-modality` qualifier finds models that support a particular medium for providing output. Possible modalities include `text` and `embeddings`.
 QualifierExample`output-modality:MODALITY`[**output-modality:embeddings**](https://github.com/search?q=output-modality:embeddings&type=marketplace) matches models that support embedding output. ## [Search by language](#search-by-language)
 The `language` qualifier finds models that support a specified human language.
 QualifierExample`language:TWO_CHARACTER_CODE`[**language:es**](https://github.com/search?q=language:es&type=marketplace) matches models that support Spanish.`language:NAME`[**language:arabic**](https://github.com/search?q=language:arabic&type=marketplace) matches models that support Arabic. ## [Search by task](#search-by-task)
 The `task` qualifier finds models that can be used to accomplish a specific task.
 QualifierExample`task:TASK`[**task:embeddings**](https://github.com/search?q=task:embeddings&type=marketplace) matches models that support embedding.`task:TASK`[**task:chat-completion**](https://github.com/search?q=task:chat-completion&type=marketplace) matches models that support interaction via chat. ## [Search by publisher](#search-by-publisher)
 The `publisher` qualifier finds models released by a particular publisher.
 QualifierExample`publisher:PUBLISHER_NAME`[**publisher:"Mistral AI"**](https://github.com/search?q=publisher:%22Mistral+AI%22&type=marketplace) matches models by Mistral AI. ## [Search by input token limit](#search-by-input-token-limit)
 The `input-tokens` qualifier finds models with an input token limit above or below a particular value, or within a range.
 QualifierExample`input-tokens:VALUE`[**input-tokens:>10000**](https://github.com/search?q=input-tokens:%3E10000&type=marketplace) matches models with an input token limit greater than 10,000.`input-tokens:VALUE`[**input-tokens:15000..20000**](https://github.com/search?q=input-tokens:15000..20000&type=marketplace) matches models with an input token limit between 15,000 and 20,000. ## [Search by output token limit](#search-by-output-token-limit)
 The `output-tokens` qualifier finds models with an output token limit above or below a particular value, or within a range.
 QualifierExample`output-tokens:VALUE`[**output-tokens:<8000**](https://github.com/search?q=output-tokens:%3C8000&type=marketplace) matches models with an output token limit less than 8,000.`output-tokens:VALUE`[**output-tokens:15000..20000**](https://github.com/search?q=output-tokens:15000..20000&type=marketplace) matches models with an output token limit between 15,000 and 20,000. ## [Search by rate limit tier](#search-by-rate-limit-tier)
 The `rate-limit-tier` qualifier finds models with a particular tier of rate limit. Possible tiers include `low`, `high`, and `custom`.
 QualifierExample`rate-limit-tier:TIER`[**rate-limit-tier:low**](https://github.com/search?q=rate-limit-tier:low&type=marketplace) matches models with a low rate limit tier. ## [Search by license type](#search-by-license-type)
 The `license` qualifier finds models that use a particular license.
 QualifierExample`license:LICENSE`[**license:mit**](https://github.com/search?q=license:mit&type=marketplace) matches models that use the MIT license.`license:LICENSE`[**license:custom**](https://github.com/search?q=license:custom&type=marketplace) matches models that use a custom license. ## [Sorting results](#sorting-results)
 The `sort` qualifier is used to sort results. It can be used alone or combined with other qualifiers and search text.
 QualifierExample`sort:FIELD`[**sort:created-desc publisher:meta**](https://github.com/search?q=sort:created-desc+publisher:meta&type=marketplace) matches models published by Meta, sorted with the most recently added first.`sort:FIELD`[**sort:name-asc in:task chat-completion**](https://github.com/search?q=sort:name-asc+in:task+chat-completion&type=marketplace) matches models that allow chat completion, sorted alphabetically. ## [Further reading](#further-reading)
 - [Sorting search results](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)## Help and support
### Did you find what you needed?
YesNo
[Privacy policy](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
### Help us make these docs great!
All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.
[Make a contribution](https://github.com/github/docs/blob/main/content/search-github/searching-on-github/searching-github-models.md)
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

*选择时间: 2026/5/12 13:38:49*

---

## 选择区域 3

**来源页面:** [Searching GitHub Models - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-github-models)

**选择器信息:**
- XPath: `//*[@id="main-content"]/div[1]/div[2]`
- CSS Selector: `#main-content > div.container-xl.px-3.px-md-6.my-4 > div.ArticleGridLayout_containerBox__lLLio.md-selector-preview.md-selector-highlight:nth-of-type(2)`

# Searching GitHub Models
You can search for models that are available on GitHub Models.
Copy as Markdown
## In this article
- [About searching GitHub Models](#about-searching-github-models)
- [Searching in GitHub Marketplace](#searching-in-github-marketplace)
- [Searching across GitHub](#searching-across-github)
- [Searching within a specific field](#searching-within-a-specific-field)
- [Search by category](#search-by-category)
- [Search by input modality](#search-by-input-modality)
- [Search by output modality](#search-by-output-modality)
- [Search by language](#search-by-language)
- [Search by task](#search-by-task)
- [Search by publisher](#search-by-publisher)
- [Search by input token limit](#search-by-input-token-limit)
- [Search by output token limit](#search-by-output-token-limit)
- [Search by rate limit tier](#search-by-rate-limit-tier)
- [Search by license type](#search-by-license-type)
- [Sorting results](#sorting-results)
- [Further reading](#further-reading)
## [About searching GitHub Models](#about-searching-github-models)
 You can find models on GitHub Models in two ways:
 - Search from GitHub Marketplace.
- Search across all of GitHub and then filter the results to Marketplace.
 ## [Searching in GitHub Marketplace](#searching-in-github-marketplace)
 1. To open GitHub Marketplace, in the top-left corner of GitHub, select , then click **Marketplace**.
 ![Screenshot of the navigation bar on GitHub. The "Open global navigation menu" icon is outlined in dark orange.](https://docs.github.com/assets/cb-2683/images/help/navigation/global-navigation-menu-icon.png)
2. Type any keywords and `type:models` and press **Enter**.
 ## [Searching across GitHub](#searching-across-github)
 Anytime you search across all of GitHub, you can filter the results to see matching models from GitHub Marketplace.
 1. Navigate to [https://github.com/search](https://github.com/search).
2. Type any keywords and press **Enter**.
3. To see all available filters for your search, in the "Filter by" sidebar, click **More**.
4. To see results from GitHub Models, click **Marketplace**.
 ## [Searching within a specific field](#searching-within-a-specific-field)
 The `in` qualifier used in conjunction with search text finds models that match the specified text in that field. Possible fields include `tags`, `license`, `name`, `description`, `transparency`, and `task`.
 QualifierExample`in:FIELD`[**in:tags agents**](https://github.com/search?q=in:tags+agents&type=marketplace) matches models with the 'agents' tag.`in:FIELD`[**in:license distribute**](https://github.com/search?q=in:license+distribute&type=marketplace) matches models who mention 'distribute' in their license.`in:FIELD`[**in:transparency "responsible ai"**](https://github.com/search?q=in:transparency+%22responsible+ai%22&type=marketplace) matches models who mention 'responsible ai' in their transparency information. ## [Search by category](#search-by-category)
 The `category` qualifier finds models that are tagged with a specific term.
 QualifierExample`category:CATEGORY`[**category:multilingual**](https://github.com/search?q=category:multilingual&type=marketplace) matches models in the multilingual category.`category:CATEGORY`[**category:"large context"**](https://github.com/search?q=category:%22large+context%22+&type=marketplace) matches models in the large context category. ## [Search by input modality](#search-by-input-modality)
 The `input-modality` qualifier finds models that support a particular medium for providing input. Possible modalities include `text`, `image`, and `audio`.
 QualifierExample`input-modality:MODALITY`[**input-modality:text**](https://github.com/search?q=input-modality:text&type=marketplace) matches models that support text input. ## [Search by output modality](#search-by-output-modality)
 The `output-modality` qualifier finds models that support a particular medium for providing output. Possible modalities include `text` and `embeddings`.
 QualifierExample`output-modality:MODALITY`[**output-modality:embeddings**](https://github.com/search?q=output-modality:embeddings&type=marketplace) matches models that support embedding output. ## [Search by language](#search-by-language)
 The `language` qualifier finds models that support a specified human language.
 QualifierExample`language:TWO_CHARACTER_CODE`[**language:es**](https://github.com/search?q=language:es&type=marketplace) matches models that support Spanish.`language:NAME`[**language:arabic**](https://github.com/search?q=language:arabic&type=marketplace) matches models that support Arabic. ## [Search by task](#search-by-task)
 The `task` qualifier finds models that can be used to accomplish a specific task.
 QualifierExample`task:TASK`[**task:embeddings**](https://github.com/search?q=task:embeddings&type=marketplace) matches models that support embedding.`task:TASK`[**task:chat-completion**](https://github.com/search?q=task:chat-completion&type=marketplace) matches models that support interaction via chat. ## [Search by publisher](#search-by-publisher)
 The `publisher` qualifier finds models released by a particular publisher.
 QualifierExample`publisher:PUBLISHER_NAME`[**publisher:"Mistral AI"**](https://github.com/search?q=publisher:%22Mistral+AI%22&type=marketplace) matches models by Mistral AI. ## [Search by input token limit](#search-by-input-token-limit)
 The `input-tokens` qualifier finds models with an input token limit above or below a particular value, or within a range.
 QualifierExample`input-tokens:VALUE`[**input-tokens:>10000**](https://github.com/search?q=input-tokens:%3E10000&type=marketplace) matches models with an input token limit greater than 10,000.`input-tokens:VALUE`[**input-tokens:15000..20000**](https://github.com/search?q=input-tokens:15000..20000&type=marketplace) matches models with an input token limit between 15,000 and 20,000. ## [Search by output token limit](#search-by-output-token-limit)
 The `output-tokens` qualifier finds models with an output token limit above or below a particular value, or within a range.
 QualifierExample`output-tokens:VALUE`[**output-tokens:<8000**](https://github.com/search?q=output-tokens:%3C8000&type=marketplace) matches models with an output token limit less than 8,000.`output-tokens:VALUE`[**output-tokens:15000..20000**](https://github.com/search?q=output-tokens:15000..20000&type=marketplace) matches models with an output token limit between 15,000 and 20,000. ## [Search by rate limit tier](#search-by-rate-limit-tier)
 The `rate-limit-tier` qualifier finds models with a particular tier of rate limit. Possible tiers include `low`, `high`, and `custom`.
 QualifierExample`rate-limit-tier:TIER`[**rate-limit-tier:low**](https://github.com/search?q=rate-limit-tier:low&type=marketplace) matches models with a low rate limit tier. ## [Search by license type](#search-by-license-type)
 The `license` qualifier finds models that use a particular license.
 QualifierExample`license:LICENSE`[**license:mit**](https://github.com/search?q=license:mit&type=marketplace) matches models that use the MIT license.`license:LICENSE`[**license:custom**](https://github.com/search?q=license:custom&type=marketplace) matches models that use a custom license. ## [Sorting results](#sorting-results)
 The `sort` qualifier is used to sort results. It can be used alone or combined with other qualifiers and search text.
 QualifierExample`sort:FIELD`[**sort:created-desc publisher:meta**](https://github.com/search?q=sort:created-desc+publisher:meta&type=marketplace) matches models published by Meta, sorted with the most recently added first.`sort:FIELD`[**sort:name-asc in:task chat-completion**](https://github.com/search?q=sort:name-asc+in:task+chat-completion&type=marketplace) matches models that allow chat completion, sorted alphabetically. ## [Further reading](#further-reading)
 - [Sorting search results](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results)

*选择时间: 2026/5/12 13:38:49*

---

## 选择区域 4

**来源页面:** [Searching GitHub Models - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-github-models)

**选择器信息:**
- XPath: `//*[@id="_r_1d_--label"]`
- CSS Selector: `#_r_1d_--label`

Sorting search results

*选择时间: 2026/5/12 13:38:49*

---

## 选择区域 5

**来源页面:** [Searching GitHub Models - GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-github-models)

**选择器信息:**
- XPath: `//*[@id="_r_6_--label"]`
- CSS Selector: `#_r_6_--label`

Troubleshoot search queries

*选择时间: 2026/5/12 13:38:49*