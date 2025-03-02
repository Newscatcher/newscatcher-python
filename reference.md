# Reference
## Search
<details><summary><code>client.search.<a href="src/newscatcher/search/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for articles based on specified criteria such as keyword, language, country, source, and more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.search.get(
    q="technology AND (Apple OR Microsoft) NOT Google",
    predefined_sources="top 100 US, top 5 GB",
    from_=datetime.datetime.fromisoformat(
        "2024-07-01 00:00:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-07-01 00:00:00+00:00",
    ),
    theme="Business,Finance",
    not_theme="Crime",
    iptc_tags="20000199,20000209",
    not_iptc_tags="20000205,20000209",
    iab_tags="Business,Events",
    not_iab_tags="Agriculture,Metals",
    custom_tags="Tag1,Tag2,Tag3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` 

The keyword(s) to search for in articles. Query syntax supports logical operators (`AND`, `OR`, `NOT`) and wildcards:

- For an exact match, use double quotes. For example, `"technology news"`.
- Use `*` to search for any keyword.
- Use `+` to include and `-` to exclude specific words or phrases. 
  For example, `+Apple`, `-Google`.
- Use `AND`, `OR`, and `NOT` to refine search results. 
  For example, `technology AND (Apple OR Microsoft) NOT Google`.

For more details, see [Advanced querying](/docs/v3/documentation/guides-and-concepts/advanced-querying).
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[str]` 

The article fields to search in. To search in multiple fields, use a comma-separated string. 

Example: `"title, summary"`

**Note**: The `summary` option is available if NLP is enabled in your plan.

Available options: `title`, `summary`, `content`.
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Multiple countries with the number of top sources can be specified as a comma-separated string.

Examples: 
- `"top 100 US"`
- `"top 33 AT"`
- `"top 50 US, top 20 GB"`
- `"top 33 AT, top 50 IT"`
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[str]` 

Word or phrase to search within the source names. To specify multiple values, use a comma-separated string.

Example: `"sport, tech"`

**Note**: The search doesn't require an exact match and returns sources containing the specified terms in their names. You can use any word or phrase, like `"sport"` or `"new york times"`. For example, `"sport"` returns sources such as `"Motorsport"`, `"Dot Esport"`, and `"Tuttosport"`.
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[str]` 

One or more news sources to narrow down the search. The format must be a domain URL. Subdomains, such as `finance.yahoo.com`, are also acceptable.To specify multiple sources, use a comma-separated string.

Examples:
- `"nytimes.com"`
- `"theguardian.com, finance.yahoo.com"`
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[str]` 

The news sources to exclude from the search. To exclude multiple sources, use a comma-separated string. 

Example: `"cnn.com, wsj.com"`
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` 

The language(s) of the search. The only accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To select multiple languages, use a comma-separated string. 

Example: `"en, es"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[str]` 

The language(s) to exclude from the search. The accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To exclude multiple languages, use a comma-separated string. 

Example: `"fr, de"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

Example: `"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[str]` 

The publisher location countries to exclude from the search. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To exclude multiple countries, use a comma-separated string. 

Example:`"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[str]` 

The list of author names to exclude from your search. To exclude articles by specific authors, use a comma-separated string.

Example: `"John Doe, Jane Doe"`
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[dt.datetime]` 

The starting point in time to search from. Accepts date-time strings in ISO 8601 format and plain text. The default time zone is UTC. 

Formats with examples:
- YYYY-mm-ddTHH:MM:SS: `2024-07-01T00:00:00`
- YYYY-MM-dd: `2024-07-01`
- YYYY/mm/dd HH:MM:SS: `2024/07/01 00:00:00`
- YYYY/mm/dd: `2024/07/01`
- English phrases: `1 day ago`, `today`

**Note**: By default, applied to the publication date of the article. To use the article's parse date instead, set the `by_parse_date` parameter to `true`.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[dt.datetime]` 

The ending point in time to search up to. Accepts date-time strings in ISO 8601 format and plain text. The default time zone is UTC. 

Formats with examples:
- YYYY-mm-ddTHH:MM:SS: `2024-07-01T00:00:00`
- YYYY-MM-dd: `2024-07-01`
- YYYY/mm/dd HH:MM:SS: `2024/07/01 00:00:00`
- YYYY/mm/dd: `2024/07/01`
- English phrases: `1 day ago`, `today`

**Note**: By default, applied to the publication date of the article. To use the article's parse date instead, set the `by_parse_date` parameter to `true`.
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[SearchGetRequestPublishedDatePrecision]` 

The precision of the published date. There are three types:
- `full`: The day and time of an article is correctly identified with the appropriate timezone.
- `timezone unknown`: The day and time of an article is correctly identified without timezone.
- `date`: Only the day is identified without an exact time.
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[bool]` — If true, the `from_` and `to_` parameters use article parse dates instead of published dates. Additionally, the `parse_date` variable is added to the output for each article object.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[SearchGetRequestSortBy]` 

The sorting order of the results. Possible values are:
- `relevancy`: The most relevant results first.
- `date`: The most recently published results first.
- `rank`: The results from the highest-ranked sources first.
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[bool]` — If true, limits the search to sources ranked in the top 1 million online websites. If false, includes unranked sources which are assigned a rank of 999999.
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` — The lowest boundary of the rank of a news website to filter by. A lower rank indicates a more popular source.
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` — The highest boundary of the rank of a news website to filter by. A lower rank indicates a more popular source.
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[bool]` — If true, only returns articles that were posted on the home page of a given news domain.
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[bool]` — If true, returns only opinion pieces. If false, excludes opinion-based articles and returns news only.
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[bool]` — If false, returns only articles that have publicly available complete content. Some publishers partially block content, so this setting ensures that only full articles are retrieved.
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[str]` 

The categorical URL(s) to filter your search. To filter your search by multiple categorical URLs, use a comma-separated string.

Example: `"wsj.com/politics, wsj.com/tech"`
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[str]` 

The complete URL(s) mentioned in the article. For multiple URLs, use a comma-separated string.

Example: `"https://aiindex.stanford.edu/report, https://www.stateof.ai"`

For more details, see [Search by URL](/docs/v3/documentation/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[str]` 

The domain(s) mentioned in the article. For multiple domains, use a comma-separated string.

Example: `"who.int, nih.gov"`

For more details, see [Search by URL](/docs/v3/documentation/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**additional_domain_info:** `typing.Optional[bool]` 

If true, includes additional domain information in the response for each article:
- `is_news_domain`: Boolean indicating if the source is a news domain.
- `news_domain_type`: Type of news domain (e.g., `"Original Content"`).
- `news_type`: Category of news (e.g., `"News and Blogs"`).
    
</dd>
</dl>

<dl>
<dd>

**is_news_domain:** `typing.Optional[bool]` — If true, filters results to include only news domains.
    
</dd>
</dl>

<dl>
<dd>

**news_domain_type:** `typing.Optional[SearchGetRequestNewsDomainType]` 

Filters results based on the news domain type. Possible values are:
- `Original Content`: Sources that produce their own content.
- `Aggregator`: Sources that collect content from various other sources.
- `Press Releases`: Sources primarily publishing press releases.
- `Republisher`: Sources that republish content from other sources.
- `Other`: Sources that don't fit into main categories.
    
</dd>
</dl>

<dl>
<dd>

**news_type:** `typing.Optional[str]` 

Filters results based on the news type. Multiple types can be specified using a comma-separated string.

Example: `"General News Outlets,Tech News and Updates"`

For a complete list of available news types, see [Enumerated parameters > News type](/docs/v3/api-reference/overview/enumerated-parameters#news-type-news-type).
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[int]` — The minimum number of words an article must contain. To be used for avoiding articles with small content.
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[int]` — The maximum number of words an article can contain. To be used for avoiding articles with large content.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

The page number to scroll through the results. Use for pagination, as a single API response can return up to 1,000 articles. 

For details, see [How to paginate large datasets](https://www.newscatcherapi.com/docs/v3/documentation/how-to/paginate-large-datasets).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of articles to return per page.
    
</dd>
</dl>

<dl>
<dd>

**clustering_enabled:** `typing.Optional[bool]` 

Determines whether to group similar articles into clusters. If true, the API returns clustered results.

To learn more, see [Clustering news articles](/docs/v3/documentation/guides-and-concepts/clustering-news-articles).
    
</dd>
</dl>

<dl>
<dd>

**clustering_variable:** `typing.Optional[SearchGetRequestClusteringVariable]` 

Specifies which part of the article to use for determining similarity when clustering.

Possible values are:
- `content`: Uses the full article content (default).
- `title`: Uses only the article title.
- `summary`: Uses the article summary.

To learn more, see [Clustering news articles](/docs/v3/documentation/guides-and-concepts/clustering-news-articles).
    
</dd>
</dl>

<dl>
<dd>

**clustering_threshold:** `typing.Optional[float]` 

Sets the similarity threshold for grouping articles into clusters. A lower value creates more inclusive clusters, while a higher value requires greater similarity between articles.

Examples:
- `0.3`: Results in larger, more diverse clusters.
- `0.6`: Balances cluster size and article similarity (default).
- `0.9`: Creates smaller, tightly related clusters.

To learn more, see [Clustering news articles](/docs/v3/documentation/guides-and-concepts/clustering-news-articles).
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 

If true, includes an NLP layer with each article in the response. This layer provides enhanced information such as theme classification, article summary, sentiment analysis, tags, and named entity recognition.

The NLP layer includes:
- Theme: General topic of the article.
- Summary: A concise overview of the article content.
- Sentiment: Separate scores for title and content (range: -1 to 1).
- Named entities: Identified persons (PER), organizations (ORG), locations (LOC), and miscellaneous entities (MISC).
- IPTC tags: Standardized news category tags.
- IAB tags: Content categories for digital advertising.

**Note**: The `include_nlp_data` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 

If true, filters the results to include only articles with an NLP layer. This allows you to focus on articles that have been processed with advanced NLP techniques.

**Note**: The `has_nlp` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 

Filters articles based on their general topic, as determined by NLP analysis. To select multiple themes, use a comma-separated string.

Example: `"Finance, Tech"`

**Note**: The `theme` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).

Available options: `Business`, `Economics`, `Entertainment`, `Finance`, `Health`, `Politics`, `Science`, `Sports`, `Tech`, `Crime`, `Financial Crime`, `Lifestyle`, `Automotive`, `Travel`, `Weather`, `General`.
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 

Inverse of the `theme` parameter. Excludes articles based on their general topic, as determined by NLP analysis. To exclude multiple themes, use a comma-separated string. 

Example: `"Crime, Tech"`

**Note**: The `not_theme` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**org_entity_name:** `typing.Optional[str]` 

Filters articles that mention specific organization names, as identified by NLP analysis. To specify multiple organizations, use a comma-separated string. 

Example: `"Apple, Microsoft"`

**Note**: The `ORG_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**per_entity_name:** `typing.Optional[str]` 

Filters articles that mention specific person names, as identified by NLP analysis. To specify multiple names, use a comma-separated string. 

Example: `"Elon Musk, Jeff Bezos"`

**Note**: The `PER_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**loc_entity_name:** `typing.Optional[str]` 

Filters articles that mention specific location names, as identified by NLP analysis. To specify multiple locations, use a comma-separated string. 

Example: `"California, New York"`

**Note**: The `LOC_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**misc_entity_name:** `typing.Optional[str]` 

Filters articles that mention other named entities not falling under person, organization, or location categories. Includes events, nationalities, products, works of art, and more. To specify multiple entities, use a comma-separated string. 

Example: `"Bitcoin, Blockchain"`

**Note**: The `MISC_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 

Filters articles based on the minimum sentiment score of their titles.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `title_sentiment_min` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 

Filters articles based on the maximum sentiment score of their titles.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `title_sentiment_max` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 

Filters articles based on the minimum sentiment score of their content.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `content_sentiment_min` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 

Filters articles based on the maximum sentiment score of their content.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `content_sentiment_max` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[str]` 

Filters articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags, use a comma-separated string of tag IDs. 

Example: `"20000199, 20000209"`

**Note**: The `iptc_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[str]` 

Inverse of the `iptc_tags` parameter. Excludes articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags to exclude, use a comma-separated string of tag IDs. 

Example: `"20000205, 20000209"`

**Note**: The `not_iptc_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[str]` 

Filters articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories, use a comma-separated string. 

Example: `"Business, Events"`

**Note**: The `iab_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[str]` 

Inverse of the `iab_tags` parameter. Excludes articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories to exclude, use a comma-separated string. 

Example: `"Agriculture, Metals"`

**Note**: The `not_iab_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[str]` 

Filters articles based on provided taxonomy that is tailored to your specific needs and is accessible only with your API key. To specify tags, use the following pattern: 

- `custom_tags.taxonomy=Tag1,Tag2,Tag3`, where `taxonomy` is the taxonomy name and `Tag1,Tag2,Tag3` is a comma-separated list of tags.

Example: `custom_tags.industry="Manufacturing, Supply Chain, Logistics"`

To learn more, see the [Custom tags](/docs/v3/documentation/guides-and-concepts/custom-tags).
    
</dd>
</dl>

<dl>
<dd>

**exclude_duplicates:** `typing.Optional[bool]` 

If true, excludes duplicate and highly similar articles from the search results. If false, returns all relevant articles, including duplicates. 

To learn more, see [Articles deduplication](/docs/v3/documentation/guides-and-concepts/articles-deduplication).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.search.<a href="src/newscatcher/search/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for articles based on specified criteria such as keyword, language, country, source, and more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.search.post(
    q="renewable energy",
    predefined_sources=["top 50 US"],
    lang=["en"],
    from_=datetime.datetime.fromisoformat(
        "2024-01-01 00:00:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-06-30 00:00:00+00:00",
    ),
    additional_domain_info=True,
    is_news_domain=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `Q` 
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[SearchIn]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[PredefinedSources]` 
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[SourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[Sources]` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[NotSources]` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[Lang]` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[NotLang]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[Countries]` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[NotCountries]` 
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[NotAuthorName]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[From]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[To]` 
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[PublishedDatePrecision]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[ByParseDate]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[SortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[RankedOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[FromRank]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[ToRank]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[IsHeadline]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[IsOpinion]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[IsPaidContent]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[ParentUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[AllLinks]` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[AllDomainLinks]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_domain_info:** `typing.Optional[AdditionalDomainInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**is_news_domain:** `typing.Optional[IsNewsDomain]` 
    
</dd>
</dl>

<dl>
<dd>

**news_domain_type:** `typing.Optional[NewsDomainType]` 
    
</dd>
</dl>

<dl>
<dd>

**news_type:** `typing.Optional[NewsType]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[WordCountMin]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[WordCountMax]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[Page]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_enabled:** `typing.Optional[ClusteringEnabled]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_variable:** `typing.Optional[ClusteringVariable]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_threshold:** `typing.Optional[ClusteringThreshold]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[IncludeNlpData]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[HasNlp]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[Theme]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[NotTheme]` 
    
</dd>
</dl>

<dl>
<dd>

**org_entity_name:** `typing.Optional[OrgEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**per_entity_name:** `typing.Optional[PerEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**loc_entity_name:** `typing.Optional[LocEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**misc_entity_name:** `typing.Optional[MiscEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[TitleSentimentMin]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[TitleSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[ContentSentimentMin]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentient_max:** `typing.Optional[ContentSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[IptcTags]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[NotIptcTags]` 
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[IabTags]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[NotIabTags]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[CustomTags]` 
    
</dd>
</dl>

<dl>
<dd>

**exclude_duplicates:** `typing.Optional[ExcludeDuplicates]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LatestHeadlines
<details><summary><code>client.latestheadlines.<a href="src/newscatcher/latestheadlines/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the latest headlines for the specified time period. You can filter results by language, country, source, and more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.latestheadlines.get(
    predefined_sources="top 100 US, top 5 GB",
    theme="Business,Finance",
    not_theme="Crime",
    iptc_tags="20000199,20000209",
    not_iptc_tags="20000205,20000209",
    iab_tags="Business,Events",
    not_iab_tags="Agriculture,Metals",
    custom_tags="Tag1,Tag2,Tag3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**when:** `typing.Optional[str]` 

The time period for which you want to get the latest headlines.

Format examples:
- `7d`: Last seven days
- `30d`: Last 30 days
- `1h`: Last hour
- `24h`: Last 24 hours
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[bool]` — If true, the `from_` and `to_` parameters use article parse dates instead of published dates. Additionally, the `parse_date` variable is added to the output for each article object.
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` 

The language(s) of the search. The only accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To select multiple languages, use a comma-separated string. 

Example: `"en, es"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[str]` 

The language(s) to exclude from the search. The accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To exclude multiple languages, use a comma-separated string. 

Example: `"fr, de"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

Example: `"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[str]` 

The publisher location countries to exclude from the search. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To exclude multiple countries, use a comma-separated string. 

Example:`"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Multiple countries with the number of top sources can be specified as a comma-separated string.

Examples: 
- `"top 100 US"`
- `"top 33 AT"`
- `"top 50 US, top 20 GB"`
- `"top 33 AT, top 50 IT"`
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[str]` 

One or more news sources to narrow down the search. The format must be a domain URL. Subdomains, such as `finance.yahoo.com`, are also acceptable.To specify multiple sources, use a comma-separated string.

Examples:
- `"nytimes.com"`
- `"theguardian.com, finance.yahoo.com"`
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[str]` 

The news sources to exclude from the search. To exclude multiple sources, use a comma-separated string. 

Example: `"cnn.com, wsj.com"`
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[str]` 

The list of author names to exclude from your search. To exclude articles by specific authors, use a comma-separated string.

Example: `"John Doe, Jane Doe"`
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[bool]` — If true, limits the search to sources ranked in the top 1 million online websites. If false, includes unranked sources which are assigned a rank of 999999.
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[bool]` — If true, only returns articles that were posted on the home page of a given news domain.
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[bool]` — If true, returns only opinion pieces. If false, excludes opinion-based articles and returns news only.
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[bool]` — If false, returns only articles that have publicly available complete content. Some publishers partially block content, so this setting ensures that only full articles are retrieved.
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[str]` 

The categorical URL(s) to filter your search. To filter your search by multiple categorical URLs, use a comma-separated string.

Example: `"wsj.com/politics, wsj.com/tech"`
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[str]` 

The complete URL(s) mentioned in the article. For multiple URLs, use a comma-separated string.

Example: `"https://aiindex.stanford.edu/report, https://www.stateof.ai"`

For more details, see [Search by URL](/docs/v3/documentation/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[str]` 

The domain(s) mentioned in the article. For multiple domains, use a comma-separated string.

Example: `"who.int, nih.gov"`

For more details, see [Search by URL](/docs/v3/documentation/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[int]` — The minimum number of words an article must contain. To be used for avoiding articles with small content.
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[int]` — The maximum number of words an article can contain. To be used for avoiding articles with large content.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

The page number to scroll through the results. Use for pagination, as a single API response can return up to 1,000 articles. 

For details, see [How to paginate large datasets](https://www.newscatcherapi.com/docs/v3/documentation/how-to/paginate-large-datasets).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of articles to return per page.
    
</dd>
</dl>

<dl>
<dd>

**clustering_enabled:** `typing.Optional[bool]` 

Determines whether to group similar articles into clusters. If true, the API returns clustered results.

To learn more, see [Clustering news articles](/docs/v3/documentation/guides-and-concepts/clustering-news-articles).
    
</dd>
</dl>

<dl>
<dd>

**clustering_variable:** `typing.Optional[LatestHeadlinesGetRequestClusteringVariable]` 

Specifies which part of the article to use for determining similarity when clustering.

Possible values are:
- `content`: Uses the full article content (default).
- `title`: Uses only the article title.
- `summary`: Uses the article summary.

To learn more, see [Clustering news articles](/docs/v3/documentation/guides-and-concepts/clustering-news-articles).
    
</dd>
</dl>

<dl>
<dd>

**clustering_threshold:** `typing.Optional[float]` 

Sets the similarity threshold for grouping articles into clusters. A lower value creates more inclusive clusters, while a higher value requires greater similarity between articles.

Examples:
- `0.3`: Results in larger, more diverse clusters.
- `0.6`: Balances cluster size and article similarity (default).
- `0.9`: Creates smaller, tightly related clusters.

To learn more, see [Clustering news articles](/docs/v3/documentation/guides-and-concepts/clustering-news-articles).
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 

If true, includes an NLP layer with each article in the response. This layer provides enhanced information such as theme classification, article summary, sentiment analysis, tags, and named entity recognition.

The NLP layer includes:
- Theme: General topic of the article.
- Summary: A concise overview of the article content.
- Sentiment: Separate scores for title and content (range: -1 to 1).
- Named entities: Identified persons (PER), organizations (ORG), locations (LOC), and miscellaneous entities (MISC).
- IPTC tags: Standardized news category tags.
- IAB tags: Content categories for digital advertising.

**Note**: The `include_nlp_data` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 

If true, filters the results to include only articles with an NLP layer. This allows you to focus on articles that have been processed with advanced NLP techniques.

**Note**: The `has_nlp` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 

Filters articles based on their general topic, as determined by NLP analysis. To select multiple themes, use a comma-separated string.

Example: `"Finance, Tech"`

**Note**: The `theme` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).

Available options: `Business`, `Economics`, `Entertainment`, `Finance`, `Health`, `Politics`, `Science`, `Sports`, `Tech`, `Crime`, `Financial Crime`, `Lifestyle`, `Automotive`, `Travel`, `Weather`, `General`.
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 

Inverse of the `theme` parameter. Excludes articles based on their general topic, as determined by NLP analysis. To exclude multiple themes, use a comma-separated string. 

Example: `"Crime, Tech"`

**Note**: The `not_theme` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**org_entity_name:** `typing.Optional[str]` 

Filters articles that mention specific organization names, as identified by NLP analysis. To specify multiple organizations, use a comma-separated string. 

Example: `"Apple, Microsoft"`

**Note**: The `ORG_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**per_entity_name:** `typing.Optional[str]` 

Filters articles that mention specific person names, as identified by NLP analysis. To specify multiple names, use a comma-separated string. 

Example: `"Elon Musk, Jeff Bezos"`

**Note**: The `PER_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**loc_entity_name:** `typing.Optional[str]` 

Filters articles that mention specific location names, as identified by NLP analysis. To specify multiple locations, use a comma-separated string. 

Example: `"California, New York"`

**Note**: The `LOC_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**misc_entity_name:** `typing.Optional[str]` 

Filters articles that mention other named entities not falling under person, organization, or location categories. Includes events, nationalities, products, works of art, and more. To specify multiple entities, use a comma-separated string. 

Example: `"Bitcoin, Blockchain"`

**Note**: The `MISC_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 

Filters articles based on the minimum sentiment score of their titles.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `title_sentiment_min` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 

Filters articles based on the maximum sentiment score of their titles.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `title_sentiment_max` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 

Filters articles based on the minimum sentiment score of their content.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `content_sentiment_min` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 

Filters articles based on the maximum sentiment score of their content.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `content_sentiment_max` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[str]` 

Filters articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags, use a comma-separated string of tag IDs. 

Example: `"20000199, 20000209"`

**Note**: The `iptc_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[str]` 

Inverse of the `iptc_tags` parameter. Excludes articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags to exclude, use a comma-separated string of tag IDs. 

Example: `"20000205, 20000209"`

**Note**: The `not_iptc_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[str]` 

Filters articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories, use a comma-separated string. 

Example: `"Business, Events"`

**Note**: The `iab_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[str]` 

Inverse of the `iab_tags` parameter. Excludes articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories to exclude, use a comma-separated string. 

Example: `"Agriculture, Metals"`

**Note**: The `not_iab_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[str]` 

Filters articles based on provided taxonomy that is tailored to your specific needs and is accessible only with your API key. To specify tags, use the following pattern: 

- `custom_tags.taxonomy=Tag1,Tag2,Tag3`, where `taxonomy` is the taxonomy name and `Tag1,Tag2,Tag3` is a comma-separated list of tags.

Example: `custom_tags.industry="Manufacturing, Supply Chain, Logistics"`

To learn more, see the [Custom tags](/docs/v3/documentation/guides-and-concepts/custom-tags).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.latestheadlines.<a href="src/newscatcher/latestheadlines/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the latest headlines for the specified time period. You can filter results by language, country, source, and more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.latestheadlines.post(
    lang="en",
    predefined_sources=["top 50 US", "top 20 GB"],
    is_opinion=False,
    page_size=10,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**when:** `typing.Optional[When]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[ByParseDate]` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[Lang]` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[NotLang]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[Countries]` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[NotCountries]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[PredefinedSources]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[Sources]` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[NotSources]` 
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[NotAuthorName]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[RankedOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[IsHeadline]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[IsOpinion]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[IsPaidContent]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[ParentUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[AllLinks]` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[AllDomainLinks]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[WordCountMin]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[WordCountMax]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[Page]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_enabled:** `typing.Optional[ClusteringEnabled]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_variable:** `typing.Optional[ClusteringVariable]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_threshold:** `typing.Optional[ClusteringThreshold]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[IncludeNlpData]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[HasNlp]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[Theme]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[NotTheme]` 
    
</dd>
</dl>

<dl>
<dd>

**org_entity_name:** `typing.Optional[OrgEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**per_entity_name:** `typing.Optional[PerEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**loc_entity_name:** `typing.Optional[LocEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**misc_entity_name:** `typing.Optional[MiscEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[TitleSentimentMin]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[TitleSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[ContentSentimentMin]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[ContentSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[IptcTags]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[NotIptcTags]` 
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[IabTags]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[NotIabTags]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[CustomTags]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Authors
<details><summary><code>client.authors.<a href="src/newscatcher/authors/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for articles written by a specified author. You can filter results by language, country, source, and more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.authors.get(
    author_name="Jane Smith",
    predefined_sources="top 100 US, top 5 GB",
    from_=datetime.datetime.fromisoformat(
        "2024-07-01 00:00:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-07-01 00:00:00+00:00",
    ),
    theme="Business,Finance",
    not_theme="Crime",
    ner_name="Tesla",
    iptc_tags="20000199,20000209",
    not_iptc_tags="20000205,20000209",
    iab_tags="Business,Events",
    not_iab_tags="Agriculture,Metals",
    custom_tags="Tag1,Tag2,Tag3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**author_name:** `str` — The name of the author to search for. This parameter returns exact matches only.
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[str]` 

The list of author names to exclude from your search. To exclude articles by specific authors, use a comma-separated string.

Example: `"John Doe, Jane Doe"`
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Multiple countries with the number of top sources can be specified as a comma-separated string.

Examples: 
- `"top 100 US"`
- `"top 33 AT"`
- `"top 50 US, top 20 GB"`
- `"top 33 AT, top 50 IT"`
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[str]` 

One or more news sources to narrow down the search. The format must be a domain URL. Subdomains, such as `finance.yahoo.com`, are also acceptable.To specify multiple sources, use a comma-separated string.

Examples:
- `"nytimes.com"`
- `"theguardian.com, finance.yahoo.com"`
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[str]` 

The news sources to exclude from the search. To exclude multiple sources, use a comma-separated string. 

Example: `"cnn.com, wsj.com"`
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` 

The language(s) of the search. The only accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To select multiple languages, use a comma-separated string. 

Example: `"en, es"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[str]` 

The language(s) to exclude from the search. The accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To exclude multiple languages, use a comma-separated string. 

Example: `"fr, de"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

Example: `"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[str]` 

The publisher location countries to exclude from the search. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To exclude multiple countries, use a comma-separated string. 

Example:`"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[dt.datetime]` 

The starting point in time to search from. Accepts date-time strings in ISO 8601 format and plain text. The default time zone is UTC. 

Formats with examples:
- YYYY-mm-ddTHH:MM:SS: `2024-07-01T00:00:00`
- YYYY-MM-dd: `2024-07-01`
- YYYY/mm/dd HH:MM:SS: `2024/07/01 00:00:00`
- YYYY/mm/dd: `2024/07/01`
- English phrases: `1 day ago`, `today`

**Note**: By default, applied to the publication date of the article. To use the article's parse date instead, set the `by_parse_date` parameter to `true`.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[dt.datetime]` 

The ending point in time to search up to. Accepts date-time strings in ISO 8601 format and plain text. The default time zone is UTC. 

Formats with examples:
- YYYY-mm-ddTHH:MM:SS: `2024-07-01T00:00:00`
- YYYY-MM-dd: `2024-07-01`
- YYYY/mm/dd HH:MM:SS: `2024/07/01 00:00:00`
- YYYY/mm/dd: `2024/07/01`
- English phrases: `1 day ago`, `today`

**Note**: By default, applied to the publication date of the article. To use the article's parse date instead, set the `by_parse_date` parameter to `true`.
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[AuthorsGetRequestPublishedDatePrecision]` 

The precision of the published date. There are three types:
- `full`: The day and time of an article is correctly identified with the appropriate timezone.
- `timezone unknown`: The day and time of an article is correctly identified without timezone.
- `date`: Only the day is identified without an exact time.
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[bool]` — If true, the `from_` and `to_` parameters use article parse dates instead of published dates. Additionally, the `parse_date` variable is added to the output for each article object.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[AuthorsGetRequestSortBy]` 

The sorting order of the results. Possible values are:
- `relevancy`: The most relevant results first.
- `date`: The most recently published results first.
- `rank`: The results from the highest-ranked sources first.
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[bool]` — If true, limits the search to sources ranked in the top 1 million online websites. If false, includes unranked sources which are assigned a rank of 999999.
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` — The lowest boundary of the rank of a news website to filter by. A lower rank indicates a more popular source.
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` — The highest boundary of the rank of a news website to filter by. A lower rank indicates a more popular source.
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[bool]` — If true, only returns articles that were posted on the home page of a given news domain.
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[bool]` — If true, returns only opinion pieces. If false, excludes opinion-based articles and returns news only.
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[bool]` — If false, returns only articles that have publicly available complete content. Some publishers partially block content, so this setting ensures that only full articles are retrieved.
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[str]` 

The categorical URL(s) to filter your search. To filter your search by multiple categorical URLs, use a comma-separated string.

Example: `"wsj.com/politics, wsj.com/tech"`
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[str]` 

The complete URL(s) mentioned in the article. For multiple URLs, use a comma-separated string.

Example: `"https://aiindex.stanford.edu/report, https://www.stateof.ai"`

For more details, see [Search by URL](/docs/v3/documentation/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[str]` 

The domain(s) mentioned in the article. For multiple domains, use a comma-separated string.

Example: `"who.int, nih.gov"`

For more details, see [Search by URL](/docs/v3/documentation/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[int]` — The minimum number of words an article must contain. To be used for avoiding articles with small content.
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[int]` — The maximum number of words an article can contain. To be used for avoiding articles with large content.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

The page number to scroll through the results. Use for pagination, as a single API response can return up to 1,000 articles. 

For details, see [How to paginate large datasets](https://www.newscatcherapi.com/docs/v3/documentation/how-to/paginate-large-datasets).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of articles to return per page.
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 

If true, includes an NLP layer with each article in the response. This layer provides enhanced information such as theme classification, article summary, sentiment analysis, tags, and named entity recognition.

The NLP layer includes:
- Theme: General topic of the article.
- Summary: A concise overview of the article content.
- Sentiment: Separate scores for title and content (range: -1 to 1).
- Named entities: Identified persons (PER), organizations (ORG), locations (LOC), and miscellaneous entities (MISC).
- IPTC tags: Standardized news category tags.
- IAB tags: Content categories for digital advertising.

**Note**: The `include_nlp_data` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 

If true, filters the results to include only articles with an NLP layer. This allows you to focus on articles that have been processed with advanced NLP techniques.

**Note**: The `has_nlp` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 

Filters articles based on their general topic, as determined by NLP analysis. To select multiple themes, use a comma-separated string.

Example: `"Finance, Tech"`

**Note**: The `theme` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).

Available options: `Business`, `Economics`, `Entertainment`, `Finance`, `Health`, `Politics`, `Science`, `Sports`, `Tech`, `Crime`, `Financial Crime`, `Lifestyle`, `Automotive`, `Travel`, `Weather`, `General`.
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 

Inverse of the `theme` parameter. Excludes articles based on their general topic, as determined by NLP analysis. To exclude multiple themes, use a comma-separated string. 

Example: `"Crime, Tech"`

**Note**: The `not_theme` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**ner_name:** `typing.Optional[str]` 

The name of person, organization, location, product or other named entity to search for. To specify multiple names use a comma-separated string. 

Example: `"Tesla, Amazon"`
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 

Filters articles based on the minimum sentiment score of their titles.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `title_sentiment_min` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 

Filters articles based on the maximum sentiment score of their titles.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `title_sentiment_max` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 

Filters articles based on the minimum sentiment score of their content.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `content_sentiment_min` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 

Filters articles based on the maximum sentiment score of their content.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `content_sentiment_max` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[str]` 

Filters articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags, use a comma-separated string of tag IDs. 

Example: `"20000199, 20000209"`

**Note**: The `iptc_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[str]` 

Inverse of the `iptc_tags` parameter. Excludes articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags to exclude, use a comma-separated string of tag IDs. 

Example: `"20000205, 20000209"`

**Note**: The `not_iptc_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[str]` 

Filters articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories, use a comma-separated string. 

Example: `"Business, Events"`

**Note**: The `iab_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[str]` 

Inverse of the `iab_tags` parameter. Excludes articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories to exclude, use a comma-separated string. 

Example: `"Agriculture, Metals"`

**Note**: The `not_iab_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[str]` 

Filters articles based on provided taxonomy that is tailored to your specific needs and is accessible only with your API key. To specify tags, use the following pattern: 

- `custom_tags.taxonomy=Tag1,Tag2,Tag3`, where `taxonomy` is the taxonomy name and `Tag1,Tag2,Tag3` is a comma-separated list of tags.

Example: `custom_tags.industry="Manufacturing, Supply Chain, Logistics"`

To learn more, see the [Custom tags](/docs/v3/documentation/guides-and-concepts/custom-tags).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authors.<a href="src/newscatcher/authors/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for articles by author. You can filter results by language, country, source, and more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.authors.post(
    author_name="Joanna Stern",
    sources=["wsj.com", "nytimes.com"],
    lang="en",
    from_=datetime.datetime.fromisoformat(
        "2024-01-01 00:00:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-06-30 00:00:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**author_name:** `AuthorName` 
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[NotAuthorName]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[PredefinedSources]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[Sources]` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[NotSources]` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[Lang]` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[NotLang]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[Countries]` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[NotCountries]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[From]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[To]` 
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[PublishedDatePrecision]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[ByParseDate]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[SortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[RankedOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[FromRank]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[ToRank]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[IsHeadline]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[IsOpinion]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[IsPaidContent]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[ParentUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[AllLinks]` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[AllDomainLinks]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[WordCountMin]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[WordCountMax]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[Page]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[IncludeNlpData]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[HasNlp]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[Theme]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[NotTheme]` 
    
</dd>
</dl>

<dl>
<dd>

**ner_name:** `typing.Optional[NerName]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[TitleSentimentMin]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[TitleSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[ContentSentimentMin]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[ContentSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[IptcTags]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[NotIptcTags]` 
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[IabTags]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[NotIabTags]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[CustomTags]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SearchLink
<details><summary><code>client.search_link.<a href="src/newscatcher/search_link/client.py">search_url_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for articles based on specified links or IDs. You can filter results by date range.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.search_link.search_url_get(
    from_=datetime.datetime.fromisoformat(
        "2024-07-01 00:00:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-01-01 00:00:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[str]` 

The Newscatcher article ID (corresponds to the `_id` field in API response) or a list of article IDs to search for. To specify multiple IDs, use a comma-separated string. 

Example: `"1234567890abcdef, abcdef1234567890"`

**Caution**: You can use either the `links` or the `ids` parameter, but not both at the same time.
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[str]` 

The article link or list of article links to search for. To specify multiple links, use a comma-separated string. 

Example: `"https://example.com/article1, https://example.com/article2"`

**Caution**: You can use either the `links` or the `ids` parameter, but not both at the same time.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[From]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[To]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

The page number to scroll through the results. Use for pagination, as a single API response can return up to 1,000 articles. 

For details, see [How to paginate large datasets](https://www.newscatcherapi.com/docs/v3/documentation/how-to/paginate-large-datasets).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of articles to return per page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.search_link.<a href="src/newscatcher/search_link/client.py">search_url_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for articles using their ID(s) or link(s).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.search_link.search_url_post(
    ids=[
        "8ea8a784568ffaa05cb6d1ab2d2e84dd",
        "0146a551ef05ab1c494a55e806e3ce64",
    ],
    links=[
        "https://www.nytimes.com/2024/08/30/technology/ai-chatbot-chatgpt-manipulation.html",
        "https://www.bbc.com/news/articles/c39k379grzlo",
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` 
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[Links]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[From]` 

The starting point in time to search from. Accepts date-time strings in ISO 8601 format and plain text strings. The default time zone is UTC. 

Formats with examples:
- YYYY-mm-ddTHH:MM:SS: `2024-07-01T00:00:00`
- YYYY-MM-dd: `2024-07-01`
- YYYY/mm/dd HH:MM:SS: `2024/07/01 00:00:00`
- YYYY/mm/dd: `2024/07/01`
- English phrases: `1 day ago`, `today`
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[To]` 

The ending point in time to search up to. Accepts date-time strings in ISO 8601 format and plain text strings. The default time zone is UTC. 

Formats with examples:
- YYYY-mm-ddTHH:MM:SS: `2024-07-01T00:00:00`
- YYYY-MM-dd: `2024-07-01`
- YYYY/mm/dd HH:MM:SS: `2024/07/01 00:00:00`
- YYYY/mm/dd: `2024/07/01`
- English phrases: `1 day ago`, `today`
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[Page]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SearchSimilar
<details><summary><code>client.searchsimilar.<a href="src/newscatcher/searchsimilar/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for articles similar to a specified query.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.searchsimilar.get(
    q="technology AND (Apple OR Microsoft) NOT Google",
    similar_documents_fields="title,summary",
    predefined_sources="top 100 US, top 5 GB",
    from_=datetime.datetime.fromisoformat(
        "2024-07-01 00:00:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-07-01 00:00:00+00:00",
    ),
    theme="Business,Finance",
    not_theme="Crime",
    ner_name="Tesla",
    iptc_tags="20000199,20000209",
    not_iptc_tags="20000205,20000209",
    custom_tags="Tag1,Tag2,Tag3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` 

The keyword(s) to search for in articles. Query syntax supports logical operators (`AND`, `OR`, `NOT`) and wildcards:

- For an exact match, use double quotes. For example, `"technology news"`.
- Use `*` to search for any keyword.
- Use `+` to include and `-` to exclude specific words or phrases. 
  For example, `+Apple`, `-Google`.
- Use `AND`, `OR`, and `NOT` to refine search results. 
  For example, `technology AND (Apple OR Microsoft) NOT Google`.

For more details, see [Advanced querying](/docs/v3/documentation/guides-and-concepts/advanced-querying).
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[str]` 

The article fields to search in. To search in multiple fields, use a comma-separated string. 

Example: `"title, summary"`

**Note**: The `summary` option is available if NLP is enabled in your plan.

Available options: `title`, `summary`, `content`.
    
</dd>
</dl>

<dl>
<dd>

**include_similar_documents:** `typing.Optional[bool]` — If true, includes similar documents in the response.
    
</dd>
</dl>

<dl>
<dd>

**similar_documents_number:** `typing.Optional[int]` — The number of similar documents to return.
    
</dd>
</dl>

<dl>
<dd>

**similar_documents_fields:** `typing.Optional[str]` — The fields to consider for finding similar documents.
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Multiple countries with the number of top sources can be specified as a comma-separated string.

Examples: 
- `"top 100 US"`
- `"top 33 AT"`
- `"top 50 US, top 20 GB"`
- `"top 33 AT, top 50 IT"`
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[str]` 

One or more news sources to narrow down the search. The format must be a domain URL. Subdomains, such as `finance.yahoo.com`, are also acceptable.To specify multiple sources, use a comma-separated string.

Examples:
- `"nytimes.com"`
- `"theguardian.com, finance.yahoo.com"`
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[str]` 

The news sources to exclude from the search. To exclude multiple sources, use a comma-separated string. 

Example: `"cnn.com, wsj.com"`
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` 

The language(s) of the search. The only accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To select multiple languages, use a comma-separated string. 

Example: `"en, es"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[str]` 

The language(s) to exclude from the search. The accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To exclude multiple languages, use a comma-separated string. 

Example: `"fr, de"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

Example: `"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[str]` 

The publisher location countries to exclude from the search. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To exclude multiple countries, use a comma-separated string. 

Example:`"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[dt.datetime]` 

The starting point in time to search from. Accepts date-time strings in ISO 8601 format and plain text. The default time zone is UTC. 

Formats with examples:
- YYYY-mm-ddTHH:MM:SS: `2024-07-01T00:00:00`
- YYYY-MM-dd: `2024-07-01`
- YYYY/mm/dd HH:MM:SS: `2024/07/01 00:00:00`
- YYYY/mm/dd: `2024/07/01`
- English phrases: `1 day ago`, `today`

**Note**: By default, applied to the publication date of the article. To use the article's parse date instead, set the `by_parse_date` parameter to `true`.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[dt.datetime]` 

The ending point in time to search up to. Accepts date-time strings in ISO 8601 format and plain text. The default time zone is UTC. 

Formats with examples:
- YYYY-mm-ddTHH:MM:SS: `2024-07-01T00:00:00`
- YYYY-MM-dd: `2024-07-01`
- YYYY/mm/dd HH:MM:SS: `2024/07/01 00:00:00`
- YYYY/mm/dd: `2024/07/01`
- English phrases: `1 day ago`, `today`

**Note**: By default, applied to the publication date of the article. To use the article's parse date instead, set the `by_parse_date` parameter to `true`.
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[bool]` — If true, the `from_` and `to_` parameters use article parse dates instead of published dates. Additionally, the `parse_date` variable is added to the output for each article object.
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[SearchSimilarGetRequestPublishedDatePrecision]` 

The precision of the published date. There are three types:
- `full`: The day and time of an article is correctly identified with the appropriate timezone.
- `timezone unknown`: The day and time of an article is correctly identified without timezone.
- `date`: Only the day is identified without an exact time.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[SearchSimilarGetRequestSortBy]` 

The sorting order of the results. Possible values are:
- `relevancy`: The most relevant results first.
- `date`: The most recently published results first.
- `rank`: The results from the highest-ranked sources first.
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[bool]` — If true, limits the search to sources ranked in the top 1 million online websites. If false, includes unranked sources which are assigned a rank of 999999.
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` — The lowest boundary of the rank of a news website to filter by. A lower rank indicates a more popular source.
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` — The highest boundary of the rank of a news website to filter by. A lower rank indicates a more popular source.
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[bool]` — If true, only returns articles that were posted on the home page of a given news domain.
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[bool]` — If true, returns only opinion pieces. If false, excludes opinion-based articles and returns news only.
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[bool]` — If false, returns only articles that have publicly available complete content. Some publishers partially block content, so this setting ensures that only full articles are retrieved.
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[str]` 

The categorical URL(s) to filter your search. To filter your search by multiple categorical URLs, use a comma-separated string.

Example: `"wsj.com/politics, wsj.com/tech"`
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[str]` 

The complete URL(s) mentioned in the article. For multiple URLs, use a comma-separated string.

Example: `"https://aiindex.stanford.edu/report, https://www.stateof.ai"`

For more details, see [Search by URL](/docs/v3/documentation/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[str]` 

The domain(s) mentioned in the article. For multiple domains, use a comma-separated string.

Example: `"who.int, nih.gov"`

For more details, see [Search by URL](/docs/v3/documentation/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[int]` — The minimum number of words an article must contain. To be used for avoiding articles with small content.
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[int]` — The maximum number of words an article can contain. To be used for avoiding articles with large content.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

The page number to scroll through the results. Use for pagination, as a single API response can return up to 1,000 articles. 

For details, see [How to paginate large datasets](https://www.newscatcherapi.com/docs/v3/documentation/how-to/paginate-large-datasets).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of articles to return per page.
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 

If true, includes an NLP layer with each article in the response. This layer provides enhanced information such as theme classification, article summary, sentiment analysis, tags, and named entity recognition.

The NLP layer includes:
- Theme: General topic of the article.
- Summary: A concise overview of the article content.
- Sentiment: Separate scores for title and content (range: -1 to 1).
- Named entities: Identified persons (PER), organizations (ORG), locations (LOC), and miscellaneous entities (MISC).
- IPTC tags: Standardized news category tags.
- IAB tags: Content categories for digital advertising.

**Note**: The `include_nlp_data` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 

If true, filters the results to include only articles with an NLP layer. This allows you to focus on articles that have been processed with advanced NLP techniques.

**Note**: The `has_nlp` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 

Filters articles based on their general topic, as determined by NLP analysis. To select multiple themes, use a comma-separated string.

Example: `"Finance, Tech"`

**Note**: The `theme` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).

Available options: `Business`, `Economics`, `Entertainment`, `Finance`, `Health`, `Politics`, `Science`, `Sports`, `Tech`, `Crime`, `Financial Crime`, `Lifestyle`, `Automotive`, `Travel`, `Weather`, `General`.
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 

Inverse of the `theme` parameter. Excludes articles based on their general topic, as determined by NLP analysis. To exclude multiple themes, use a comma-separated string. 

Example: `"Crime, Tech"`

**Note**: The `not_theme` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**ner_name:** `typing.Optional[str]` 

The name of person, organization, location, product or other named entity to search for. To specify multiple names use a comma-separated string. 

Example: `"Tesla, Amazon"`
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 

Filters articles based on the minimum sentiment score of their titles.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `title_sentiment_min` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 

Filters articles based on the maximum sentiment score of their titles.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `title_sentiment_max` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 

Filters articles based on the minimum sentiment score of their content.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `content_sentiment_min` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 

Filters articles based on the maximum sentiment score of their content.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `content_sentiment_max` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[str]` 

Filters articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags, use a comma-separated string of tag IDs. 

Example: `"20000199, 20000209"`

**Note**: The `iptc_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[str]` 

Inverse of the `iptc_tags` parameter. Excludes articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags to exclude, use a comma-separated string of tag IDs. 

Example: `"20000205, 20000209"`

**Note**: The `not_iptc_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[str]` 

Filters articles based on provided taxonomy that is tailored to your specific needs and is accessible only with your API key. To specify tags, use the following pattern: 

- `custom_tags.taxonomy=Tag1,Tag2,Tag3`, where `taxonomy` is the taxonomy name and `Tag1,Tag2,Tag3` is a comma-separated list of tags.

Example: `custom_tags.industry="Manufacturing, Supply Chain, Logistics"`

To learn more, see the [Custom tags](/docs/v3/documentation/guides-and-concepts/custom-tags).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.searchsimilar.<a href="src/newscatcher/searchsimilar/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for articles similar to the specified query. You can filter results by language, country, source, and more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.searchsimilar.post(
    q="artificial intelligence",
    include_similar_documents=True,
    similar_documents_number=5,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `Q` 
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[SearchIn]` 
    
</dd>
</dl>

<dl>
<dd>

**include_similar_documents:** `typing.Optional[IncludeSimilarDocuments]` 
    
</dd>
</dl>

<dl>
<dd>

**similar_documents_number:** `typing.Optional[SimilarDocumentsNumber]` 
    
</dd>
</dl>

<dl>
<dd>

**similar_documents_fields:** `typing.Optional[SimilarDocumentsFields]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[PredefinedSources]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[Sources]` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[NotSources]` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[Lang]` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[NotLang]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[Countries]` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[NotCountries]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[From]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[To]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[ByParseDate]` 
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[PublishedDatePrecision]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[SortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[RankedOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[FromRank]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[ToRank]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[IsHeadline]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[IsOpinion]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[IsPaidContent]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[ParentUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[AllLinks]` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[AllDomainLinks]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[WordCountMin]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[WordCountMax]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[Page]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[IncludeNlpData]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[HasNlp]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[Theme]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[NotTheme]` 
    
</dd>
</dl>

<dl>
<dd>

**ner_name:** `typing.Optional[NerName]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[TitleSentimentMin]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[TitleSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[ContentSentimentMin]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[ContentSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[IptcTags]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[NotIptcTags]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[CustomTags]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sources
<details><summary><code>client.sources.<a href="src/newscatcher/sources/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of sources based on specified criteria such as language, country, rank, and more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.sources.get(
    predefined_sources="top 100 US, top 5 GB",
    source_url="bbc.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**lang:** `typing.Optional[str]` 

The language(s) of the search. The only accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To select multiple languages, use a comma-separated string. 

Example: `"en, es"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

Example: `"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Multiple countries with the number of top sources can be specified as a comma-separated string.

Examples: 
- `"top 100 US"`
- `"top 33 AT"`
- `"top 50 US, top 20 GB"`
- `"top 33 AT, top 50 IT"`
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[str]` 

Word or phrase to search within the source names. To specify multiple values, use a comma-separated string.

Example: `"sport, tech"`

**Note**: The search doesn't require an exact match and returns sources containing the specified terms in their names. You can use any word or phrase, like `"sport"` or `"new york times"`. For example, `"sport"` returns sources such as `"Motorsport"`, `"Dot Esport"`, and `"Tuttosport"`.
    
</dd>
</dl>

<dl>
<dd>

**source_url:** `typing.Optional[str]` 

The domain(s) of the news publication to search for. 

**Caution**:  When specifying the `source_url` parameter, 
you can only use `include_additional_info` as an extra parameter.
    
</dd>
</dl>

<dl>
<dd>

**include_additional_info:** `typing.Optional[bool]` 

If true, returns the following additional datapoints about each news source:
- `nb_articles_for_7d`: The number of articles published by the source in the last week.
- `country`: Source country of origin.
- `rank`: SEO rank.
- `is_news_domain`: Boolean indicating if the source is a news domain.
- `news_domain_type`: Type of news domain (e.g., "Original Content").
- `news_type`: Category of news (e.g., "General News Outlets").
    
</dd>
</dl>

<dl>
<dd>

**is_news_domain:** `typing.Optional[bool]` — If true, filters results to include only news domains.
    
</dd>
</dl>

<dl>
<dd>

**news_domain_type:** `typing.Optional[SourcesGetRequestNewsDomainType]` 

Filters results based on the news domain type. Possible values are:
- `Original Content`: Sources that produce their own content.
- `Aggregator`: Sources that collect content from various other sources.
- `Press Releases`: Sources primarily publishing press releases.
- `Republisher`: Sources that republish content from other sources.
- `Other`: Sources that don't fit into main categories.
    
</dd>
</dl>

<dl>
<dd>

**news_type:** `typing.Optional[str]` 

Filters results based on the news type. Multiple types can be specified using a comma-separated string.

Example: `"General News Outlets,Tech News and Updates"`

For a complete list of available news types, see [Enumerated parameters > News type](/docs/v3/api-reference/overview/enumerated-parameters#news-type-news-type).
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` — The lowest boundary of the rank of a news website to filter by. A lower rank indicates a more popular source.
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` — The highest boundary of the rank of a news website to filter by. A lower rank indicates a more popular source.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.<a href="src/newscatcher/sources/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the list of sources available in the database. You can filter the sources by language, country, and more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.sources.post(
    predefined_sources=["top 50 US"],
    include_additional_info=True,
    is_news_domain=True,
    news_domain_type="Original Content",
    news_type="General News Outlets",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**lang:** `typing.Optional[Lang]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[Countries]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[PredefinedSources]` 
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[SourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**source_url:** `typing.Optional[SourceUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**include_additional_info:** `typing.Optional[IncludeAdditionalInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**is_news_domain:** `typing.Optional[IsNewsDomain]` 
    
</dd>
</dl>

<dl>
<dd>

**news_domain_type:** `typing.Optional[NewsDomainType]` 
    
</dd>
</dl>

<dl>
<dd>

**news_type:** `typing.Optional[NewsType]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[FromRank]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[ToRank]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Aggregation
<details><summary><code>client.aggregation.<a href="src/newscatcher/aggregation/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the count of articles aggregated by day or hour based on various search criteria, such as keyword, language, country, and source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.aggregation.get(
    q="technology AND (Apple OR Microsoft) NOT Google",
    predefined_sources="top 100 US, top 5 GB",
    from_=datetime.datetime.fromisoformat(
        "2024-07-01 00:00:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-07-01 00:00:00+00:00",
    ),
    theme="Business,Finance",
    not_theme="Crime",
    iptc_tags="20000199,20000209",
    not_iptc_tags="20000205,20000209",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` 

The keyword(s) to search for in articles. Query syntax supports logical operators (`AND`, `OR`, `NOT`) and wildcards:

- For an exact match, use double quotes. For example, `"technology news"`.
- Use `*` to search for any keyword.
- Use `+` to include and `-` to exclude specific words or phrases. 
  For example, `+Apple`, `-Google`.
- Use `AND`, `OR`, and `NOT` to refine search results. 
  For example, `technology AND (Apple OR Microsoft) NOT Google`.

For more details, see [Advanced querying](/docs/v3/documentation/guides-and-concepts/advanced-querying).
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[str]` 

The article fields to search in. To search in multiple fields, use a comma-separated string. 

Example: `"title, summary"`

**Note**: The `summary` option is available if NLP is enabled in your plan.

Available options: `title`, `summary`, `content`.
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Multiple countries with the number of top sources can be specified as a comma-separated string.

Examples: 
- `"top 100 US"`
- `"top 33 AT"`
- `"top 50 US, top 20 GB"`
- `"top 33 AT, top 50 IT"`
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[str]` 

One or more news sources to narrow down the search. The format must be a domain URL. Subdomains, such as `finance.yahoo.com`, are also acceptable.To specify multiple sources, use a comma-separated string.

Examples:
- `"nytimes.com"`
- `"theguardian.com, finance.yahoo.com"`
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[str]` 

The news sources to exclude from the search. To exclude multiple sources, use a comma-separated string. 

Example: `"cnn.com, wsj.com"`
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` 

The language(s) of the search. The only accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To select multiple languages, use a comma-separated string. 

Example: `"en, es"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[str]` 

The language(s) to exclude from the search. The accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To exclude multiple languages, use a comma-separated string. 

Example: `"fr, de"`

To learn more, see [Enumerated parameters > Language](/docs/v3/api-reference/overview/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

Example: `"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[str]` 

The publisher location countries to exclude from the search. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To exclude multiple countries, use a comma-separated string. 

Example:`"US, CA"`

To learn more, see [Enumerated parameters > Country](/docs/v3/api-reference/overview/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[str]` 

The list of author names to exclude from your search. To exclude articles by specific authors, use a comma-separated string.

Example: `"John Doe, Jane Doe"`
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[dt.datetime]` 

The starting point in time to search from. Accepts date-time strings in ISO 8601 format and plain text. The default time zone is UTC. 

Formats with examples:
- YYYY-mm-ddTHH:MM:SS: `2024-07-01T00:00:00`
- YYYY-MM-dd: `2024-07-01`
- YYYY/mm/dd HH:MM:SS: `2024/07/01 00:00:00`
- YYYY/mm/dd: `2024/07/01`
- English phrases: `1 day ago`, `today`

**Note**: By default, applied to the publication date of the article. To use the article's parse date instead, set the `by_parse_date` parameter to `true`.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[dt.datetime]` 

The ending point in time to search up to. Accepts date-time strings in ISO 8601 format and plain text. The default time zone is UTC. 

Formats with examples:
- YYYY-mm-ddTHH:MM:SS: `2024-07-01T00:00:00`
- YYYY-MM-dd: `2024-07-01`
- YYYY/mm/dd HH:MM:SS: `2024/07/01 00:00:00`
- YYYY/mm/dd: `2024/07/01`
- English phrases: `1 day ago`, `today`

**Note**: By default, applied to the publication date of the article. To use the article's parse date instead, set the `by_parse_date` parameter to `true`.
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[AggregationGetRequestPublishedDatePrecision]` 

The precision of the published date. There are three types:
- `full`: The day and time of an article is correctly identified with the appropriate timezone.
- `timezone unknown`: The day and time of an article is correctly identified without timezone.
- `date`: Only the day is identified without an exact time.
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[bool]` — If true, the `from_` and `to_` parameters use article parse dates instead of published dates. Additionally, the `parse_date` variable is added to the output for each article object.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[AggregationGetRequestSortBy]` 

The sorting order of the results. Possible values are:
- `relevancy`: The most relevant results first.
- `date`: The most recently published results first.
- `rank`: The results from the highest-ranked sources first.
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[bool]` — If true, limits the search to sources ranked in the top 1 million online websites. If false, includes unranked sources which are assigned a rank of 999999.
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` — The lowest boundary of the rank of a news website to filter by. A lower rank indicates a more popular source.
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` — The highest boundary of the rank of a news website to filter by. A lower rank indicates a more popular source.
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[bool]` — If true, only returns articles that were posted on the home page of a given news domain.
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[bool]` — If true, returns only opinion pieces. If false, excludes opinion-based articles and returns news only.
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[bool]` — If false, returns only articles that have publicly available complete content. Some publishers partially block content, so this setting ensures that only full articles are retrieved.
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[str]` 

The categorical URL(s) to filter your search. To filter your search by multiple categorical URLs, use a comma-separated string.

Example: `"wsj.com/politics, wsj.com/tech"`
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[str]` 

The complete URL(s) mentioned in the article. For multiple URLs, use a comma-separated string.

Example: `"https://aiindex.stanford.edu/report, https://www.stateof.ai"`

For more details, see [Search by URL](/docs/v3/documentation/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[str]` 

The domain(s) mentioned in the article. For multiple domains, use a comma-separated string.

Example: `"who.int, nih.gov"`

For more details, see [Search by URL](/docs/v3/documentation/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[int]` — The minimum number of words an article must contain. To be used for avoiding articles with small content.
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[int]` — The maximum number of words an article can contain. To be used for avoiding articles with large content.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

The page number to scroll through the results. Use for pagination, as a single API response can return up to 1,000 articles. 

For details, see [How to paginate large datasets](https://www.newscatcherapi.com/docs/v3/documentation/how-to/paginate-large-datasets).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of articles to return per page.
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 

If true, includes an NLP layer with each article in the response. This layer provides enhanced information such as theme classification, article summary, sentiment analysis, tags, and named entity recognition.

The NLP layer includes:
- Theme: General topic of the article.
- Summary: A concise overview of the article content.
- Sentiment: Separate scores for title and content (range: -1 to 1).
- Named entities: Identified persons (PER), organizations (ORG), locations (LOC), and miscellaneous entities (MISC).
- IPTC tags: Standardized news category tags.
- IAB tags: Content categories for digital advertising.

**Note**: The `include_nlp_data` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 

If true, filters the results to include only articles with an NLP layer. This allows you to focus on articles that have been processed with advanced NLP techniques.

**Note**: The `has_nlp` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 

Filters articles based on their general topic, as determined by NLP analysis. To select multiple themes, use a comma-separated string.

Example: `"Finance, Tech"`

**Note**: The `theme` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).

Available options: `Business`, `Economics`, `Entertainment`, `Finance`, `Health`, `Politics`, `Science`, `Sports`, `Tech`, `Crime`, `Financial Crime`, `Lifestyle`, `Automotive`, `Travel`, `Weather`, `General`.
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 

Inverse of the `theme` parameter. Excludes articles based on their general topic, as determined by NLP analysis. To exclude multiple themes, use a comma-separated string. 

Example: `"Crime, Tech"`

**Note**: The `not_theme` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**org_entity_name:** `typing.Optional[str]` 

Filters articles that mention specific organization names, as identified by NLP analysis. To specify multiple organizations, use a comma-separated string. 

Example: `"Apple, Microsoft"`

**Note**: The `ORG_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**per_entity_name:** `typing.Optional[str]` 

Filters articles that mention specific person names, as identified by NLP analysis. To specify multiple names, use a comma-separated string. 

Example: `"Elon Musk, Jeff Bezos"`

**Note**: The `PER_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**loc_entity_name:** `typing.Optional[str]` 

Filters articles that mention specific location names, as identified by NLP analysis. To specify multiple locations, use a comma-separated string. 

Example: `"California, New York"`

**Note**: The `LOC_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**misc_entity_name:** `typing.Optional[str]` 

Filters articles that mention other named entities not falling under person, organization, or location categories. Includes events, nationalities, products, works of art, and more. To specify multiple entities, use a comma-separated string. 

Example: `"Bitcoin, Blockchain"`

**Note**: The `MISC_entity_name` parameter is only available if NLP is included in your subscription plan.

To learn more, see [Search by entity](/docs/v3/documentation/how-to/search-by-entity).
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 

Filters articles based on the minimum sentiment score of their titles.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `title_sentiment_min` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 

Filters articles based on the maximum sentiment score of their titles.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `title_sentiment_max` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 

Filters articles based on the minimum sentiment score of their content.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `content_sentiment_min` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 

Filters articles based on the maximum sentiment score of their content.

Range is `-1.0` to `1.0`, where:
- Negative values indicate negative sentiment.
- Positive values indicate positive sentiment.
- Values close to 0 indicate neutral sentiment.

**Note**: The `content_sentiment_max` parameter is only available if NLP is included in your subscription plan.

To learn more, see [NLP features](/docs/v3/documentation/guides-and-concepts/nlp-features).
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[str]` 

Filters articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags, use a comma-separated string of tag IDs. 

Example: `"20000199, 20000209"`

**Note**: The `iptc_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[str]` 

Inverse of the `iptc_tags` parameter. Excludes articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags to exclude, use a comma-separated string of tag IDs. 

Example: `"20000205, 20000209"`

**Note**: The `not_iptc_tags` parameter is only available if tags are included in your subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**aggregation_by:** `typing.Optional[AggregationGetRequestAggregationBy]` 

The aggregation interval for the results. Possible values are:
- `day`: Aggregates results by day.
- `hour`: Aggregates results by hour.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.aggregation.<a href="src/newscatcher/aggregation/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the count of articles aggregated by day or hour based on various search criteria, such as keyword, language, country, and source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.aggregation.post(
    q="renewable energy",
    predefined_sources="top 50 US",
    from_=datetime.datetime.fromisoformat(
        "2024-01-01 00:00:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-06-30 00:00:00+00:00",
    ),
    aggregation_by="day",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `Q` 
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[SearchIn]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[PredefinedSources]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[Sources]` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[NotSources]` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[Lang]` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[NotLang]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[Countries]` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[NotCountries]` 
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[NotAuthorName]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[From]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[To]` 
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[PublishedDatePrecision]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[ByParseDate]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[SortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[RankedOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[FromRank]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[ToRank]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[IsHeadline]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[IsOpinion]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[IsPaidContent]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[ParentUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[AllLinks]` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[AllDomainLinks]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[WordCountMin]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[WordCountMax]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[Page]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[IncludeNlpData]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[HasNlp]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[Theme]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[NotTheme]` 
    
</dd>
</dl>

<dl>
<dd>

**org_entity_name:** `typing.Optional[OrgEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**per_entity_name:** `typing.Optional[PerEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**loc_entity_name:** `typing.Optional[LocEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**misc_entity_name:** `typing.Optional[MiscEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[TitleSentimentMin]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[TitleSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[ContentSentimentMin]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentient_max:** `typing.Optional[ContentSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[IptcTags]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[NotIptcTags]` 
    
</dd>
</dl>

<dl>
<dd>

**aggregation_by:** `typing.Optional[AggregationBy]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscription
<details><summary><code>client.subscription.<a href="src/newscatcher/subscription/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves information about your subscription plan.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.subscription.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription.<a href="src/newscatcher/subscription/client.py">post</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves information about your subscription plan.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.subscription.post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

