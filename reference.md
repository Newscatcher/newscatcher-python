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

This endpoint allows you to search for articles. You can search for articles by keyword, language, country, source, and more.
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
    api_token="YOUR_API_TOKEN",
)
client.search.get(
    q="q",
    predefined_sources="predefined_sources",
    sources="sources",
    not_sources="not_sources",
    lang="lang",
    not_lang="not_lang",
    countries="countries",
    not_countries="not_countries",
    not_author_name="not_author_name",
    parent_url="parent_url",
    all_links="all_links",
    all_domain_links="all_domain_links",
    iptc_tags="iptc_tags",
    not_iptc_tags="not_iptc_tags",
    source_name="source_name",
    iab_tags="iab_tags",
    not_iab_tags="not_iab_tags",
    news_domain_type="news_domain_type",
    news_type="news_type",
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
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**news_domain_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**news_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_variable:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_enabled:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_threshold:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**org_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**per_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loc_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**misc_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**exclude_duplicates:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_domain_info:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_news_domain:** `typing.Optional[bool]` 
    
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

This endpoint allows you to search for articles. You can search for articles by keyword, language, country, source, and more.
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
    api_token="YOUR_API_TOKEN",
)
client.search.post(
    q="q",
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
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[SearchRequestFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[SearchRequestTo]` 
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[SearchRequestByParseDate]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[SearchRequestRankedOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[SearchRequestFromRank]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[SearchRequestToRank]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[SearchRequestIsHeadline]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[SearchRequestIsOpinion]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[SearchRequestIsPaidContent]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[SearchRequestWordCountMin]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[SearchRequestWordCountMax]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[SearchRequestPage]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[SearchRequestPageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_variable:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_enabled:** `typing.Optional[SearchRequestClusteringEnabled]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_threshold:** `typing.Optional[SearchRequestClusteringThreshold]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[SearchRequestIncludeNlpData]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**org_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**per_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loc_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**misc_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**exclude_duplicates:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_domain_info:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_news_domain:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**news_domain_type:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**news_type:** `typing.Optional[typing.Optional[typing.Any]]` 
    
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

## Latestheadlines
<details><summary><code>client.latestheadlines.<a href="src/newscatcher/latestheadlines/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows you to get latest headlines. You need to specify since when you want to get the latest headlines. You can also filter by language, country, source, and more.
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
    api_token="YOUR_API_TOKEN",
)
client.latestheadlines.get(
    lang="lang",
    not_lang="not_lang",
    countries="countries",
    not_countries="not_countries",
    sources="sources",
    predefined_sources="predefined_sources",
    not_sources="not_sources",
    not_author_name="not_author_name",
    parent_url="parent_url",
    all_links="all_links",
    all_domain_links="all_domain_links",
    iptc_tags="iptc_tags",
    not_iptc_tags="not_iptc_tags",
    iab_tags="iab_tags",
    not_iab_tags="not_iab_tags",
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

**lang:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**when:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_variable:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_enabled:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_threshold:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**org_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**per_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loc_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**misc_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 
    
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

This endpoint allows you to get latest headlines. You need to specify since when you want to get the latest headlines. You can also filter by language, country, source, and more.
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
    api_token="YOUR_API_TOKEN",
)
client.latestheadlines.post()

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
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[LatestHeadlinesRequestByParseDate]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[LatestHeadlinesRequestRankedOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[LatestHeadlinesRequestIsHeadline]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[LatestHeadlinesRequestIsOpinion]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[LatestHeadlinesRequestIsPaidContent]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[LatestHeadlinesRequestWordCountMin]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[LatestHeadlinesRequestWordCountMax]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[LatestHeadlinesRequestPage]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[LatestHeadlinesRequestPageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_variable:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_enabled:** `typing.Optional[LatestHeadlinesRequestClusteringEnabled]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering_threshold:** `typing.Optional[LatestHeadlinesRequestClusteringThreshold]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**org_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**per_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loc_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**misc_entity_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
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

This endpoint allows you to search for articles by author. You need to specify the author name. You can also filter by language, country, source, and more.
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
    api_token="YOUR_API_TOKEN",
)
client.authors.get(
    author_name="author_name",
    sources="sources",
    predefined_sources="predefined_sources",
    not_sources="not_sources",
    lang="lang",
    not_lang="not_lang",
    countries="countries",
    not_countries="not_countries",
    parent_url="parent_url",
    all_links="all_links",
    all_domain_links="all_domain_links",
    iptc_tags="iptc_tags",
    not_iptc_tags="not_iptc_tags",
    iab_tags="iab_tags",
    not_iab_tags="not_iab_tags",
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

**author_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 
    
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

This endpoint allows you to search for articles by author. You need to specify the author name. You can also filter by language, country, source, and more.
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
    api_token="YOUR_API_TOKEN",
)
client.authors.post(
    author_name="author_name",
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

**author_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_author_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[AuthorSearchRequestFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[AuthorSearchRequestTo]` 
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[AuthorSearchRequestRankedOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**iab_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iab_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
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

This endpoint allows you to search for articles. You can search for articles by id(s) or link(s).
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
    api_token="YOUR_API_TOKEN",
)
client.search_link.search_url_get(
    ids="ids",
    links="links",
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

**ids:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**links:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
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

This endpoint allows you to search for articles. You can search for articles by id(s) or link(s).
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
    api_token="YOUR_API_TOKEN",
)
client.search_link.search_url_post()

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

**ids:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[SearchUrlRequestFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[SearchUrlRequestTo]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
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

## Searchsimilar
<details><summary><code>client.searchsimilar.<a href="src/newscatcher/searchsimilar/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns a list of articles that are similar to the query provided. You also have the option to get similar articles for the results of a search.
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
    api_token="YOUR_API_TOKEN",
)
client.searchsimilar.get(
    q="q",
    predefined_sources="predefined_sources",
    sources="sources",
    not_sources="not_sources",
    lang="lang",
    not_lang="not_lang",
    countries="countries",
    not_countries="not_countries",
    parent_url="parent_url",
    all_links="all_links",
    all_domain_links="all_domain_links",
    iptc_tags="iptc_tags",
    not_iptc_tags="not_iptc_tags",
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
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include_similar_documents:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**similar_documents_number:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**similar_documents_fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 
    
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

This endpoint returns a list of articles that are similar to the query provided. You also have the option to get similar articles for the results of a search.
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
    api_token="YOUR_API_TOKEN",
)
client.searchsimilar.post(
    q="q",
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
    
</dd>
</dl>

<dl>
<dd>

**search_in:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include_similar_documents:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**similar_documents_number:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**similar_documents_fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_lang:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[MoreLikeThisRequestFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[MoreLikeThisRequestTo]` 
    
</dd>
</dl>

<dl>
<dd>

**by_parse_date:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**published_date_precision:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ranked_only:** `typing.Optional[MoreLikeThisRequestRankedOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**is_headline:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_opinion:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_paid_content:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_url:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**all_links:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**all_domain_links:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_min:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**word_count_max:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**include_nlp_data:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**has_nlp:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**not_theme:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content_sentiment_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**iptc_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**not_iptc_tags:** `typing.Optional[typing.Optional[typing.Any]]` 
    
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

This endpoint allows you to get the list of sources that are available in the database. You can filter the sources by language and country. The maximum number of sources displayed is set according to your plan. You can find the list of plans and their features here: https://newscatcherapi.com/news-api#news-api-pricing
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
    api_token="YOUR_API_TOKEN",
)
client.sources.get(
    lang="lang",
    countries="countries",
    predefined_sources="predefined_sources",
    source_name="source_name",
    source_url="source_url",
    news_domain_type="news_domain_type",
    news_type="news_type",
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

**lang:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**news_domain_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**news_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**include_additional_info:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**is_news_domain:** `typing.Optional[bool]` 
    
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

This endpoint allows you to get the list of sources that are available in the database. You can filter the sources by language and country. The maximum number of sources displayed is set according to your plan. You can find the list of plans and their features here: https://newscatcherapi.com/news-api#news-api-pricing
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
    api_token="YOUR_API_TOKEN",
)
client.sources.post()

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

**lang:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**predefined_sources:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**include_additional_info:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**from_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**to_rank:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_url:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_news_domain:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**news_domain_type:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**news_type:** `typing.Optional[typing.Optional[typing.Any]]` 
    
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

This endpoint allows you to get info about your subscription plan.
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
    api_token="YOUR_API_TOKEN",
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

This endpoint allows you to get info about your subscription plan.
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
    api_token="YOUR_API_TOKEN",
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

