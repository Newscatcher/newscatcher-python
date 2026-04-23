# Reference
## Search
<details><summary><code>client.search.<a href="src/newscatcher/search/client.py">get</a>(...) -> GetSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for articles based on specified criteria such as keywords, language, country, source, and more.
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
from newscatcher.environment import NewscatcherApiEnvironment
import datetime

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.search.get(
    q="\"supply chain\" AND Amazon NOT China",
    search_in="title_content, title_content_translated",
    include_translation_fields=True,
    predefined_sources="top 50 US, top 20 GB",
    source_name="sport,tech",
    sources="nytimes.com,finance.yahoo.com",
    not_sources="cnn.com,wsj.com",
    lang="en,es",
    not_lang="fr,de",
    countries="US,CA",
    not_countries="UK,FR",
    not_author_name="John Doe, Jane Doe",
    from_=datetime.datetime.fromisoformat("1 day ago"),
    to=datetime.datetime.fromisoformat("1 day ago"),
    published_date_precision="full",
    by_parse_date=True,
    ranked_only=True,
    from_rank=100,
    to_rank=100,
    is_headline=True,
    is_opinion=True,
    is_paid_content=False,
    parent_url="wsj.com/politics,wsj.com/tech",
    all_links="https://aiindex.stanford.edu/report,https://www.stateof.ai",
    all_domain_links="who.int,nih.gov",
    all_links_text="Nvidia,Tesla",
    additional_domain_info=True,
    is_news_domain=True,
    news_type="General News Outlets,Tech News and Updates",
    word_count_min=300,
    word_count_max=1000,
    page=2,
    page_size=50,
    clustering_enabled=True,
    clustering_threshold=0.7,
    include_nlp_data=True,
    has_nlp=True,
    theme="Finance,Tech",
    not_theme="Crime,Sports",
    org_entity_name="\"Apple Inc\" OR Microsoft",
    per_entity_name="\"Elon Musk\" OR \"Jeff Bezos\"",
    loc_entity_name="\"San Francisco\" OR \"New York City\"",
    misc_entity_name="AWS OR \"Microsoft Azure\"",
    title_sentiment_min=-0.5,
    title_sentiment_max=0.5,
    content_sentiment_min=-0.5,
    content_sentiment_max=0.5,
    iptc_tags="20000199,20000209",
    not_iptc_tags="20000205,20000209",
    iab_tags="Business,Events",
    not_iab_tags="Agriculture,Metals",
    custom_tags="Tag1,Tag2",
    exclude_duplicates=True,
    robots_compliant=True,
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

**include_translation_fields:** `typing.Optional[IncludeTranslationFields]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). 

Multiple countries with the number of top sources can be specified as a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[str]` 

Word or phrase to search within the source names. To specify multiple values, use a comma-separated string.

**Note**: The search doesn't require an exact match and returns sources containing the specified terms in their names. You can use any word or phrase, like `"sport"` or `"new york times"`. For example, `"sport"` returns sources such as `"Motorsport"`, `"Dot Esport"`, and `"Tuttosport"`.
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[str]` — One or more news sources to narrow down the search. The format must be a domain URL. Subdomains, such as `finance.yahoo.com`, are also acceptable.To specify multiple sources, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[str]` — The news sources to exclude from the search. To exclude multiple sources, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` 

The language(s) of the search. The only accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To select multiple languages, use a comma-separated string.

To learn more, see [Enumerated parameters > Language](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[str]` 

The language(s) to exclude from the search. The accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To exclude multiple languages, use a comma-separated string. 

To learn more, see [Enumerated parameters > Language](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

To learn more, see [Enumerated parameters > Country](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[str]` 

The publisher location countries to exclude from the search. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To exclude multiple countries, use a comma-separated string. 

To learn more, see [Enumerated parameters > Country](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[str]` — The list of author names to exclude from your search. To exclude articles by specific authors, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[From]` 
    
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

**parent_url:** `typing.Optional[str]` — The categorical URL(s) to filter your search. To filter your search by multiple categorical URLs, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[str]` 

The complete URL(s) mentioned in the article. For multiple URLs, use a comma-separated string.

For more details, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[str]` 

The domain(s) mentioned in the article. For multiple domains, use a comma-separated string.

For more details, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_links_text:** `typing.Optional[str]` 

The text content of links mentioned in the article. Searches for links where the anchor text contains the specified terms. For multiple terms, use a comma-separated string.

**Note**: When this parameter is used, the response includes the `all_links_data` field with detailed link information.

To learn more, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
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

**news_type:** `typing.Optional[str]` 

Filters results based on the news type. Multiple types can be specified using a comma-separated string.

For a complete list of available news types, see [Enumerated parameters > News type](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#news-type-news-type).
    
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

**iptc_tags:** `typing.Optional[str]` 

Filters articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags, use a comma-separated string of tag IDs. 

**Note**: The `iptc_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[str]` 

Inverse of the `iptc_tags` parameter. Excludes articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags to exclude, use a comma-separated string of tag IDs.

**Note**: The `not_iptc_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[str]` 

Filters articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories, use a comma-separated string.

**Note**: The `iab_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[str]` 

Inverse of the `iab_tags` parameter. Excludes articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories to exclude, use a comma-separated string.

**Note**: The `not_iab_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[str]` 

Filters articles based on provided taxonomy that is tailored to your specific needs and is accessible only with your API key. To specify tags, use the following pattern: 

- `custom_tags.taxonomy=Tag1,Tag2`, where `taxonomy` is the taxonomy name and `Tag1,Tag2` is a comma-separated list of tag names.

Example: `custom_tags.industry="Manufacturing,Logistics"`

To learn more, see the [Custom tags](https://www.newscatcherapi.com/docs/news-api/guides-and-concepts/custom-tags).
    
</dd>
</dl>

<dl>
<dd>

**exclude_duplicates:** `typing.Optional[ExcludeDuplicates]` 
    
</dd>
</dl>

<dl>
<dd>

**robots_compliant:** `typing.Optional[RobotsCompliant]` 
    
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

<details><summary><code>client.search.<a href="src/newscatcher/search/client.py">post</a>(...) -> PostSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for articles based on specified criteria such as keywords, language, country, source, and more.
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
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.search.post(
    q="\"supply chain\" AND Amazon NOT China",
    page_size=1,
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

**include_translation_fields:** `typing.Optional[IncludeTranslationFields]` 
    
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

**from:** `typing.Optional[From]` 
    
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

**all_links_text:** `typing.Optional[AllLinksText]` 
    
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

**exclude_duplicates:** `typing.Optional[ExcludeDuplicates]` 
    
</dd>
</dl>

<dl>
<dd>

**robots_compliant:** `typing.Optional[RobotsCompliant]` 
    
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
<details><summary><code>client.latest_headlines.<a href="src/newscatcher/latest_headlines/client.py">get</a>(...) -> GetLatestHeadlinesResponse</code></summary>
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
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.latest_headlines.get(
    when="7d",
    by_parse_date=True,
    lang="en,es",
    not_lang="fr,de",
    countries="US,CA",
    not_countries="UK,FR",
    predefined_sources="top 50 US, top 20 GB",
    sources="nytimes.com,finance.yahoo.com",
    not_sources="cnn.com,wsj.com",
    not_author_name="John Doe, Jane Doe",
    ranked_only=True,
    is_headline=True,
    is_opinion=True,
    is_paid_content=False,
    parent_url="wsj.com/politics,wsj.com/tech",
    all_links="https://aiindex.stanford.edu/report,https://www.stateof.ai",
    all_domain_links="who.int,nih.gov",
    all_links_text="Nvidia,Tesla",
    word_count_min=300,
    word_count_max=1000,
    page=2,
    page_size=50,
    clustering_enabled=True,
    clustering_threshold=0.7,
    include_translation_fields=True,
    include_nlp_data=True,
    has_nlp=True,
    theme="Finance,Tech",
    not_theme="Crime,Sports",
    org_entity_name="\"Apple Inc\" OR Microsoft",
    per_entity_name="\"Elon Musk\" OR \"Jeff Bezos\"",
    loc_entity_name="\"San Francisco\" OR \"New York City\"",
    misc_entity_name="AWS OR \"Microsoft Azure\"",
    title_sentiment_min=-0.5,
    title_sentiment_max=0.5,
    content_sentiment_min=-0.5,
    content_sentiment_max=0.5,
    iptc_tags="20000199,20000209",
    not_iptc_tags="20000205,20000209",
    iab_tags="Business,Events",
    not_iab_tags="Agriculture,Metals",
    custom_tags="Tag1,Tag2",
    robots_compliant=True,
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

**sort_by:** `typing.Optional[SortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` 

The language(s) of the search. The only accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To select multiple languages, use a comma-separated string.

To learn more, see [Enumerated parameters > Language](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[str]` 

The language(s) to exclude from the search. The accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To exclude multiple languages, use a comma-separated string. 

To learn more, see [Enumerated parameters > Language](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

To learn more, see [Enumerated parameters > Country](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[str]` 

The publisher location countries to exclude from the search. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To exclude multiple countries, use a comma-separated string. 

To learn more, see [Enumerated parameters > Country](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). 

Multiple countries with the number of top sources can be specified as a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[str]` — One or more news sources to narrow down the search. The format must be a domain URL. Subdomains, such as `finance.yahoo.com`, are also acceptable.To specify multiple sources, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[str]` — The news sources to exclude from the search. To exclude multiple sources, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[str]` — The list of author names to exclude from your search. To exclude articles by specific authors, use a comma-separated string.
    
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

**parent_url:** `typing.Optional[str]` — The categorical URL(s) to filter your search. To filter your search by multiple categorical URLs, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[str]` 

The complete URL(s) mentioned in the article. For multiple URLs, use a comma-separated string.

For more details, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[str]` 

The domain(s) mentioned in the article. For multiple domains, use a comma-separated string.

For more details, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_links_text:** `typing.Optional[str]` 

The text content of links mentioned in the article. Searches for links where the anchor text contains the specified terms. For multiple terms, use a comma-separated string.

**Note**: When this parameter is used, the response includes the `all_links_data` field with detailed link information.

To learn more, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
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

**include_translation_fields:** `typing.Optional[IncludeTranslationFields]` 
    
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

**iptc_tags:** `typing.Optional[str]` 

Filters articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags, use a comma-separated string of tag IDs. 

**Note**: The `iptc_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[str]` 

Inverse of the `iptc_tags` parameter. Excludes articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags to exclude, use a comma-separated string of tag IDs.

**Note**: The `not_iptc_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[str]` 

Filters articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories, use a comma-separated string.

**Note**: The `iab_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[str]` 

Inverse of the `iab_tags` parameter. Excludes articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories to exclude, use a comma-separated string.

**Note**: The `not_iab_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[str]` 

Filters articles based on provided taxonomy that is tailored to your specific needs and is accessible only with your API key. To specify tags, use the following pattern: 

- `custom_tags.taxonomy=Tag1,Tag2`, where `taxonomy` is the taxonomy name and `Tag1,Tag2` is a comma-separated list of tag names.

Example: `custom_tags.industry="Manufacturing,Logistics"`

To learn more, see the [Custom tags](https://www.newscatcherapi.com/docs/news-api/guides-and-concepts/custom-tags).
    
</dd>
</dl>

<dl>
<dd>

**robots_compliant:** `typing.Optional[RobotsCompliant]` 
    
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

<details><summary><code>client.latest_headlines.<a href="src/newscatcher/latest_headlines/client.py">post</a>(...) -> PostLatestHeadlinesResponse</code></summary>
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
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.latest_headlines.post(
    when="7d",
    page_size=1,
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

**all_links_text:** `typing.Optional[AllLinksText]` 
    
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

**include_translation_fields:** `typing.Optional[IncludeTranslationFields]` 
    
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

**robots_compliant:** `typing.Optional[RobotsCompliant]` 
    
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

## BreakingNews
<details><summary><code>client.breaking_news.<a href="src/newscatcher/breaking_news/client.py">get</a>(...) -> BreakingNewsResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves breaking news articles and sorts them based on specified criteria.
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
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.breaking_news.get(
    ranked_only=True,
    from_rank=100,
    to_rank=100,
    page=2,
    page_size=50,
    top_n_articles=5,
    include_translation_fields=True,
    include_nlp_data=True,
    has_nlp=True,
    theme="Finance,Tech",
    not_theme="Crime,Sports",
    org_entity_name="\"Apple Inc\" OR Microsoft",
    per_entity_name="\"Elon Musk\" OR \"Jeff Bezos\"",
    loc_entity_name="\"San Francisco\" OR \"New York City\"",
    misc_entity_name="AWS OR \"Microsoft Azure\"",
    title_sentiment_min=-0.5,
    title_sentiment_max=0.5,
    content_sentiment_min=-0.5,
    content_sentiment_max=0.5,
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

**top_n_articles:** `typing.Optional[TopNArticles]` 
    
</dd>
</dl>

<dl>
<dd>

**include_translation_fields:** `typing.Optional[IncludeTranslationFields]` 
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.breaking_news.<a href="src/newscatcher/breaking_news/client.py">post</a>(...) -> BreakingNewsResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves breaking news articles and sorts them based on specified criteria.
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
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.breaking_news.post(
    sort_by="relevancy",
    ranked_only=True,
    top_n_articles=1,
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

**top_n_articles:** `typing.Optional[TopNArticles]` 
    
</dd>
</dl>

<dl>
<dd>

**include_translation_fields:** `typing.Optional[IncludeTranslationFields]` 
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Authors
<details><summary><code>client.authors.<a href="src/newscatcher/authors/client.py">get</a>(...) -> GetAuthorsResponse</code></summary>
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
from newscatcher import NewscatcherApi
from newscatcher.environment import NewscatcherApiEnvironment
import datetime

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.authors.get(
    author_name="Jane Smith",
    not_author_name="John Doe, Jane Doe",
    predefined_sources="top 50 US, top 20 GB",
    sources="nytimes.com,finance.yahoo.com",
    not_sources="cnn.com,wsj.com",
    lang="en,es",
    not_lang="fr,de",
    countries="US,CA",
    not_countries="UK,FR",
    from_=datetime.datetime.fromisoformat("1 day ago"),
    to=datetime.datetime.fromisoformat("1 day ago"),
    published_date_precision="full",
    by_parse_date=True,
    ranked_only=True,
    from_rank=100,
    to_rank=100,
    is_headline=True,
    is_opinion=True,
    is_paid_content=False,
    parent_url="wsj.com/politics,wsj.com/tech",
    all_links="https://aiindex.stanford.edu/report,https://www.stateof.ai",
    all_domain_links="who.int,nih.gov",
    all_links_text="Nvidia,Tesla",
    word_count_min=300,
    word_count_max=1000,
    page=2,
    page_size=50,
    include_translation_fields=True,
    include_nlp_data=True,
    has_nlp=True,
    theme="Finance,Tech",
    not_theme="Crime,Sports",
    ner_name="Tesla,Amazon",
    title_sentiment_min=-0.5,
    title_sentiment_max=0.5,
    content_sentiment_min=-0.5,
    content_sentiment_max=0.5,
    iptc_tags="20000199,20000209",
    not_iptc_tags="20000205,20000209",
    iab_tags="Business,Events",
    not_iab_tags="Agriculture,Metals",
    custom_tags="Tag1,Tag2",
    robots_compliant=True,
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

**not_author_name:** `typing.Optional[str]` — The list of author names to exclude from your search. To exclude articles by specific authors, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). 

Multiple countries with the number of top sources can be specified as a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[str]` — One or more news sources to narrow down the search. The format must be a domain URL. Subdomains, such as `finance.yahoo.com`, are also acceptable.To specify multiple sources, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[str]` — The news sources to exclude from the search. To exclude multiple sources, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` 

The language(s) of the search. The only accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To select multiple languages, use a comma-separated string.

To learn more, see [Enumerated parameters > Language](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[str]` 

The language(s) to exclude from the search. The accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To exclude multiple languages, use a comma-separated string. 

To learn more, see [Enumerated parameters > Language](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

To learn more, see [Enumerated parameters > Country](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[str]` 

The publisher location countries to exclude from the search. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To exclude multiple countries, use a comma-separated string. 

To learn more, see [Enumerated parameters > Country](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[From]` 
    
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

**parent_url:** `typing.Optional[str]` — The categorical URL(s) to filter your search. To filter your search by multiple categorical URLs, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[str]` 

The complete URL(s) mentioned in the article. For multiple URLs, use a comma-separated string.

For more details, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[str]` 

The domain(s) mentioned in the article. For multiple domains, use a comma-separated string.

For more details, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_links_text:** `typing.Optional[str]` 

The text content of links mentioned in the article. Searches for links where the anchor text contains the specified terms. For multiple terms, use a comma-separated string.

**Note**: When this parameter is used, the response includes the `all_links_data` field with detailed link information.

To learn more, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
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

**include_translation_fields:** `typing.Optional[IncludeTranslationFields]` 
    
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

**iptc_tags:** `typing.Optional[str]` 

Filters articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags, use a comma-separated string of tag IDs. 

**Note**: The `iptc_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[str]` 

Inverse of the `iptc_tags` parameter. Excludes articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags to exclude, use a comma-separated string of tag IDs.

**Note**: The `not_iptc_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[str]` 

Filters articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories, use a comma-separated string.

**Note**: The `iab_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[str]` 

Inverse of the `iab_tags` parameter. Excludes articles based on Interactive Advertising Bureau (IAB) content categories. These tags provide a standardized taxonomy for digital advertising content categorization. To specify multiple IAB categories to exclude, use a comma-separated string.

**Note**: The `not_iab_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see the [IAB Content taxonomy](https://iabtechlab.com/standards/content-taxonomy/).
    
</dd>
</dl>

<dl>
<dd>

**custom_tags:** `typing.Optional[str]` 

Filters articles based on provided taxonomy that is tailored to your specific needs and is accessible only with your API key. To specify tags, use the following pattern: 

- `custom_tags.taxonomy=Tag1,Tag2`, where `taxonomy` is the taxonomy name and `Tag1,Tag2` is a comma-separated list of tag names.

Example: `custom_tags.industry="Manufacturing,Logistics"`

To learn more, see the [Custom tags](https://www.newscatcherapi.com/docs/news-api/guides-and-concepts/custom-tags).
    
</dd>
</dl>

<dl>
<dd>

**robots_compliant:** `typing.Optional[RobotsCompliant]` 
    
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

<details><summary><code>client.authors.<a href="src/newscatcher/authors/client.py">post</a>(...) -> PostAuthorsResponse</code></summary>
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
from newscatcher import NewscatcherApi
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.authors.post(
    author_name="David Muir",
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

**from:** `typing.Optional[From]` 
    
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

**all_links_text:** `typing.Optional[AllLinksText]` 
    
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

**include_translation_fields:** `typing.Optional[IncludeTranslationFields]` 
    
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

**robots_compliant:** `typing.Optional[RobotsCompliant]` 
    
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

## SearchByLink
<details><summary><code>client.search_by_link.<a href="src/newscatcher/search_by_link/client.py">get</a>(...) -> SearchResponseDto</code></summary>
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
from newscatcher import NewscatcherApi
from newscatcher.environment import NewscatcherApiEnvironment
import datetime

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.search_by_link.get(
    ids="5f8d0d55b6e45e00179c6e7e",
    links="https://nytimes.com/article1,https://bbc.com/article2",
    from_=datetime.datetime.fromisoformat("1 day ago"),
    to=datetime.datetime.fromisoformat("1 day ago"),
    page=2,
    page_size=50,
    robots_compliant=True,
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

**Caution**: You can use either the `links` or the `ids` parameter, but not both at the same time.
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[str]` 

The article link or list of article links to search for. To specify multiple links, use a comma-separated string.

**Caution**: You can use either the `links` or the `ids` parameter, but not both at the same time.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[From]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[To]` 
    
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

**robots_compliant:** `typing.Optional[RobotsCompliant]` 
    
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

<details><summary><code>client.search_by_link.<a href="src/newscatcher/search_by_link/client.py">post</a>(...) -> SearchResponseDto</code></summary>
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
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.search_by_link.post(
    links="https://www.reuters.com/business/energy/oil-prices-up-after-israeli-attacks-oversupply-caps-gains-2025-09-10/",
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

**from:** `typing.Optional[From]` 

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
- English phrases: `1 day ago`, `now`
    
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

**robots_compliant:** `typing.Optional[RobotsCompliant]` 
    
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
<details><summary><code>client.sources.<a href="src/newscatcher/sources/client.py">get</a>(...) -> SourcesResponseDto</code></summary>
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
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.sources.get(
    lang="en,es",
    countries="US,CA",
    predefined_sources="top 50 US, top 20 GB",
    source_name="sport,tech",
    source_url="bbc.com",
    include_additional_info=True,
    is_news_domain=True,
    news_type="General News Outlets,Tech News and Updates",
    from_rank=100,
    to_rank=100,
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

To learn more, see [Enumerated parameters > Language](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

To learn more, see [Enumerated parameters > Country](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). 

Multiple countries with the number of top sources can be specified as a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[str]` 

Word or phrase to search within the source names. To specify multiple values, use a comma-separated string.

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

**news_type:** `typing.Optional[str]` 

Filters results based on the news type. Multiple types can be specified using a comma-separated string.

For a complete list of available news types, see [Enumerated parameters > News type](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#news-type-news-type).
    
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

<details><summary><code>client.sources.<a href="src/newscatcher/sources/client.py">post</a>(...) -> SourcesResponseDto</code></summary>
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
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.sources.post(
    predefined_sources="top 10 US",
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

## AggregationCount
<details><summary><code>client.aggregation_count.<a href="src/newscatcher/aggregation_count/client.py">get</a>(...) -> GetAggregationCountResponse</code></summary>
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
from newscatcher import NewscatcherApi
from newscatcher.environment import NewscatcherApiEnvironment
import datetime

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.aggregation_count.get(
    q="\"supply chain\" AND Amazon NOT China",
    search_in="title_content, title_content_translated",
    predefined_sources="top 50 US, top 20 GB",
    sources="nytimes.com,finance.yahoo.com",
    not_sources="cnn.com,wsj.com",
    lang="en,es",
    not_lang="fr,de",
    countries="US,CA",
    not_countries="UK,FR",
    not_author_name="John Doe, Jane Doe",
    from_=datetime.datetime.fromisoformat("1 day ago"),
    to=datetime.datetime.fromisoformat("1 day ago"),
    published_date_precision="full",
    by_parse_date=True,
    ranked_only=True,
    from_rank=100,
    to_rank=100,
    is_headline=True,
    is_opinion=True,
    is_paid_content=False,
    parent_url="wsj.com/politics,wsj.com/tech",
    all_links="https://aiindex.stanford.edu/report,https://www.stateof.ai",
    all_domain_links="who.int,nih.gov",
    all_links_text="Nvidia,Tesla",
    word_count_min=300,
    word_count_max=1000,
    page=2,
    page_size=50,
    include_nlp_data=True,
    has_nlp=True,
    theme="Finance,Tech",
    not_theme="Crime,Sports",
    org_entity_name="\"Apple Inc\" OR Microsoft",
    per_entity_name="\"Elon Musk\" OR \"Jeff Bezos\"",
    loc_entity_name="\"San Francisco\" OR \"New York City\"",
    misc_entity_name="AWS OR \"Microsoft Azure\"",
    title_sentiment_min=-0.5,
    title_sentiment_max=0.5,
    content_sentiment_min=-0.5,
    content_sentiment_max=0.5,
    iptc_tags="20000199,20000209",
    not_iptc_tags="20000205,20000209",
    robots_compliant=True,
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

**aggregation_by:** `typing.Optional[AggregationBy]` 
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[SearchIn]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[str]` 

Predefined top news sources per country. 

Format: start with the word `top`, followed by the number of desired sources, and then the two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). 

Multiple countries with the number of top sources can be specified as a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[str]` — One or more news sources to narrow down the search. The format must be a domain URL. Subdomains, such as `finance.yahoo.com`, are also acceptable.To specify multiple sources, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[str]` — The news sources to exclude from the search. To exclude multiple sources, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` 

The language(s) of the search. The only accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To select multiple languages, use a comma-separated string.

To learn more, see [Enumerated parameters > Language](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[str]` 

The language(s) to exclude from the search. The accepted format is the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code. To exclude multiple languages, use a comma-separated string. 

To learn more, see [Enumerated parameters > Language](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#language-lang-and-not-lang).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[str]` 

The countries where the news publisher is located. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To select multiple countries, use a comma-separated string.

To learn more, see [Enumerated parameters > Country](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[str]` 

The publisher location countries to exclude from the search. The accepted format is the two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. To exclude multiple countries, use a comma-separated string. 

To learn more, see [Enumerated parameters > Country](https://www.newscatcherapi.com/docs/news-api/api-reference/enumerated-parameters#country-country-and-not-country).
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[str]` — The list of author names to exclude from your search. To exclude articles by specific authors, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[From]` 
    
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

**parent_url:** `typing.Optional[str]` — The categorical URL(s) to filter your search. To filter your search by multiple categorical URLs, use a comma-separated string.
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[str]` 

The complete URL(s) mentioned in the article. For multiple URLs, use a comma-separated string.

For more details, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[str]` 

The domain(s) mentioned in the article. For multiple domains, use a comma-separated string.

For more details, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
</dd>
</dl>

<dl>
<dd>

**all_links_text:** `typing.Optional[str]` 

The text content of links mentioned in the article. Searches for links where the anchor text contains the specified terms. For multiple terms, use a comma-separated string.

**Note**: When this parameter is used, the response includes the `all_links_data` field with detailed link information.

To learn more, see [Search by URL](https://www.newscatcherapi.com/docs/news-api/how-to/search-by-url).
    
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

**content_sentiment_max:** `typing.Optional[ContentSentimentMax]` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[str]` 

Filters articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags, use a comma-separated string of tag IDs. 

**Note**: The `iptc_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[str]` 

Inverse of the `iptc_tags` parameter. Excludes articles based on International Press Telecommunications Council (IPTC) media topic tags. To specify multiple IPTC tags to exclude, use a comma-separated string of tag IDs.

**Note**: The `not_iptc_tags` parameter is only available in the `v3_nlp_iptc_tags` subscription plan.

To learn more, see [IPTC Media Topic NewsCodes](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
    
</dd>
</dl>

<dl>
<dd>

**robots_compliant:** `typing.Optional[RobotsCompliant]` 
    
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

<details><summary><code>client.aggregation_count.<a href="src/newscatcher/aggregation_count/client.py">post</a>(...) -> PostAggregationCountResponse</code></summary>
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
from newscatcher import NewscatcherApi
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
)

client.aggregation_count.post(
    q="\"supply chain\" AND Amazon NOT China",
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

**aggregation_by:** `typing.Optional[AggregationBy]` 
    
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

**from:** `typing.Optional[From]` 
    
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

**all_links_text:** `typing.Optional[AllLinksText]` 
    
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

**robots_compliant:** `typing.Optional[RobotsCompliant]` 
    
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
<details><summary><code>client.subscription.<a href="src/newscatcher/subscription/client.py">get</a>() -> SubscriptionResponseDto</code></summary>
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
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
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

<details><summary><code>client.subscription.<a href="src/newscatcher/subscription/client.py">post</a>() -> SubscriptionResponseDto</code></summary>
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
from newscatcher.environment import NewscatcherApiEnvironment

client = NewscatcherApi(
    api_key="<value>",
    environment=NewscatcherApiEnvironment.DEFAULT,
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

