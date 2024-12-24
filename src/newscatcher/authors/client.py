# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from .types.authors_get_response import AuthorsGetResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.author_search_request_from import AuthorSearchRequestFrom
from .types.author_search_request_to import AuthorSearchRequestTo
from .types.author_search_request_ranked_only import AuthorSearchRequestRankedOnly
from .types.authors_post_response import AuthorsPostResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AuthorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        author_name: str,
        sources: str,
        predefined_sources: str,
        not_sources: str,
        lang: str,
        not_lang: str,
        countries: str,
        not_countries: str,
        parent_url: str,
        all_links: str,
        all_domain_links: str,
        iptc_tags: str,
        not_iptc_tags: str,
        iab_tags: str,
        not_iab_tags: str,
        not_author_name: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        to: typing.Optional[str] = None,
        published_date_precision: typing.Optional[str] = None,
        by_parse_date: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        ranked_only: typing.Optional[str] = None,
        from_rank: typing.Optional[int] = None,
        to_rank: typing.Optional[int] = None,
        is_headline: typing.Optional[bool] = None,
        is_opinion: typing.Optional[bool] = None,
        is_paid_content: typing.Optional[bool] = None,
        word_count_min: typing.Optional[int] = None,
        word_count_max: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        include_nlp_data: typing.Optional[bool] = None,
        has_nlp: typing.Optional[bool] = None,
        theme: typing.Optional[str] = None,
        not_theme: typing.Optional[str] = None,
        title_sentiment_min: typing.Optional[float] = None,
        title_sentiment_max: typing.Optional[float] = None,
        content_sentiment_min: typing.Optional[float] = None,
        content_sentiment_max: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorsGetResponse:
        """
        This endpoint allows you to search for articles by author. You need to specify the author name. You can also filter by language, country, source, and more.

        Parameters
        ----------
        author_name : str

        sources : str

        predefined_sources : str

        not_sources : str

        lang : str

        not_lang : str

        countries : str

        not_countries : str

        parent_url : str

        all_links : str

        all_domain_links : str

        iptc_tags : str

        not_iptc_tags : str

        iab_tags : str

        not_iab_tags : str

        not_author_name : typing.Optional[str]

        from_ : typing.Optional[str]

        to : typing.Optional[str]

        published_date_precision : typing.Optional[str]

        by_parse_date : typing.Optional[bool]

        sort_by : typing.Optional[str]

        ranked_only : typing.Optional[str]

        from_rank : typing.Optional[int]

        to_rank : typing.Optional[int]

        is_headline : typing.Optional[bool]

        is_opinion : typing.Optional[bool]

        is_paid_content : typing.Optional[bool]

        word_count_min : typing.Optional[int]

        word_count_max : typing.Optional[int]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        include_nlp_data : typing.Optional[bool]

        has_nlp : typing.Optional[bool]

        theme : typing.Optional[str]

        not_theme : typing.Optional[str]

        title_sentiment_min : typing.Optional[float]

        title_sentiment_max : typing.Optional[float]

        content_sentiment_min : typing.Optional[float]

        content_sentiment_max : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorsGetResponse
            Successful Response

        Examples
        --------
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
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/authors",
            method="GET",
            params={
                "author_name": author_name,
                "not_author_name": not_author_name,
                "sources": sources,
                "predefined_sources": predefined_sources,
                "not_sources": not_sources,
                "lang": lang,
                "not_lang": not_lang,
                "countries": countries,
                "not_countries": not_countries,
                "from_": from_,
                "to_": to,
                "published_date_precision": published_date_precision,
                "by_parse_date": by_parse_date,
                "sort_by": sort_by,
                "ranked_only": ranked_only,
                "from_rank": from_rank,
                "to_rank": to_rank,
                "is_headline": is_headline,
                "is_opinion": is_opinion,
                "is_paid_content": is_paid_content,
                "parent_url": parent_url,
                "all_links": all_links,
                "all_domain_links": all_domain_links,
                "word_count_min": word_count_min,
                "word_count_max": word_count_max,
                "page": page,
                "page_size": page_size,
                "include_nlp_data": include_nlp_data,
                "has_nlp": has_nlp,
                "theme": theme,
                "not_theme": not_theme,
                "title_sentiment_min": title_sentiment_min,
                "title_sentiment_max": title_sentiment_max,
                "content_sentiment_min": content_sentiment_min,
                "content_sentiment_max": content_sentiment_max,
                "iptc_tags": iptc_tags,
                "not_iptc_tags": not_iptc_tags,
                "iab_tags": iab_tags,
                "not_iab_tags": not_iab_tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AuthorsGetResponse,
                    parse_obj_as(
                        type_=AuthorsGetResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def post(
        self,
        *,
        author_name: str,
        not_author_name: typing.Optional[str] = OMIT,
        sources: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        predefined_sources: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        not_sources: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        lang: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        not_lang: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        countries: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        not_countries: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        from_: typing.Optional[AuthorSearchRequestFrom] = OMIT,
        to: typing.Optional[AuthorSearchRequestTo] = OMIT,
        published_date_precision: typing.Optional[str] = OMIT,
        by_parse_date: typing.Optional[bool] = OMIT,
        sort_by: typing.Optional[str] = OMIT,
        ranked_only: typing.Optional[AuthorSearchRequestRankedOnly] = OMIT,
        from_rank: typing.Optional[int] = OMIT,
        to_rank: typing.Optional[int] = OMIT,
        is_headline: typing.Optional[bool] = OMIT,
        is_opinion: typing.Optional[bool] = OMIT,
        is_paid_content: typing.Optional[bool] = OMIT,
        parent_url: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        all_links: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        all_domain_links: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        word_count_min: typing.Optional[int] = OMIT,
        word_count_max: typing.Optional[int] = OMIT,
        page: typing.Optional[int] = OMIT,
        page_size: typing.Optional[int] = OMIT,
        include_nlp_data: typing.Optional[bool] = OMIT,
        has_nlp: typing.Optional[bool] = OMIT,
        theme: typing.Optional[str] = OMIT,
        not_theme: typing.Optional[str] = OMIT,
        title_sentiment_min: typing.Optional[float] = OMIT,
        title_sentiment_max: typing.Optional[float] = OMIT,
        content_sentiment_min: typing.Optional[float] = OMIT,
        content_sentiment_max: typing.Optional[float] = OMIT,
        iptc_tags: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        not_iptc_tags: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        iab_tags: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        not_iab_tags: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorsPostResponse:
        """
        This endpoint allows you to search for articles by author. You need to specify the author name. You can also filter by language, country, source, and more.

        Parameters
        ----------
        author_name : str

        not_author_name : typing.Optional[str]

        sources : typing.Optional[typing.Optional[typing.Any]]

        predefined_sources : typing.Optional[typing.Optional[typing.Any]]

        not_sources : typing.Optional[typing.Optional[typing.Any]]

        lang : typing.Optional[typing.Optional[typing.Any]]

        not_lang : typing.Optional[typing.Optional[typing.Any]]

        countries : typing.Optional[typing.Optional[typing.Any]]

        not_countries : typing.Optional[typing.Optional[typing.Any]]

        from_ : typing.Optional[AuthorSearchRequestFrom]

        to : typing.Optional[AuthorSearchRequestTo]

        published_date_precision : typing.Optional[str]

        by_parse_date : typing.Optional[bool]

        sort_by : typing.Optional[str]

        ranked_only : typing.Optional[AuthorSearchRequestRankedOnly]

        from_rank : typing.Optional[int]

        to_rank : typing.Optional[int]

        is_headline : typing.Optional[bool]

        is_opinion : typing.Optional[bool]

        is_paid_content : typing.Optional[bool]

        parent_url : typing.Optional[typing.Optional[typing.Any]]

        all_links : typing.Optional[typing.Optional[typing.Any]]

        all_domain_links : typing.Optional[typing.Optional[typing.Any]]

        word_count_min : typing.Optional[int]

        word_count_max : typing.Optional[int]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        include_nlp_data : typing.Optional[bool]

        has_nlp : typing.Optional[bool]

        theme : typing.Optional[str]

        not_theme : typing.Optional[str]

        title_sentiment_min : typing.Optional[float]

        title_sentiment_max : typing.Optional[float]

        content_sentiment_min : typing.Optional[float]

        content_sentiment_max : typing.Optional[float]

        iptc_tags : typing.Optional[typing.Optional[typing.Any]]

        not_iptc_tags : typing.Optional[typing.Optional[typing.Any]]

        iab_tags : typing.Optional[typing.Optional[typing.Any]]

        not_iab_tags : typing.Optional[typing.Optional[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorsPostResponse
            Successful Response

        Examples
        --------
        from newscatcher import NewscatcherApi

        client = NewscatcherApi(
            api_token="YOUR_API_TOKEN",
        )
        client.authors.post(
            author_name="author_name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/authors",
            method="POST",
            json={
                "author_name": author_name,
                "not_author_name": not_author_name,
                "sources": sources,
                "predefined_sources": predefined_sources,
                "not_sources": not_sources,
                "lang": lang,
                "not_lang": not_lang,
                "countries": countries,
                "not_countries": not_countries,
                "from_": convert_and_respect_annotation_metadata(
                    object_=from_, annotation=AuthorSearchRequestFrom, direction="write"
                ),
                "to_": convert_and_respect_annotation_metadata(
                    object_=to, annotation=AuthorSearchRequestTo, direction="write"
                ),
                "published_date_precision": published_date_precision,
                "by_parse_date": by_parse_date,
                "sort_by": sort_by,
                "ranked_only": convert_and_respect_annotation_metadata(
                    object_=ranked_only,
                    annotation=AuthorSearchRequestRankedOnly,
                    direction="write",
                ),
                "from_rank": from_rank,
                "to_rank": to_rank,
                "is_headline": is_headline,
                "is_opinion": is_opinion,
                "is_paid_content": is_paid_content,
                "parent_url": parent_url,
                "all_links": all_links,
                "all_domain_links": all_domain_links,
                "word_count_min": word_count_min,
                "word_count_max": word_count_max,
                "page": page,
                "page_size": page_size,
                "include_nlp_data": include_nlp_data,
                "has_nlp": has_nlp,
                "theme": theme,
                "not_theme": not_theme,
                "title_sentiment_min": title_sentiment_min,
                "title_sentiment_max": title_sentiment_max,
                "content_sentiment_min": content_sentiment_min,
                "content_sentiment_max": content_sentiment_max,
                "iptc_tags": iptc_tags,
                "not_iptc_tags": not_iptc_tags,
                "iab_tags": iab_tags,
                "not_iab_tags": not_iab_tags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AuthorsPostResponse,
                    parse_obj_as(
                        type_=AuthorsPostResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAuthorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        author_name: str,
        sources: str,
        predefined_sources: str,
        not_sources: str,
        lang: str,
        not_lang: str,
        countries: str,
        not_countries: str,
        parent_url: str,
        all_links: str,
        all_domain_links: str,
        iptc_tags: str,
        not_iptc_tags: str,
        iab_tags: str,
        not_iab_tags: str,
        not_author_name: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        to: typing.Optional[str] = None,
        published_date_precision: typing.Optional[str] = None,
        by_parse_date: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        ranked_only: typing.Optional[str] = None,
        from_rank: typing.Optional[int] = None,
        to_rank: typing.Optional[int] = None,
        is_headline: typing.Optional[bool] = None,
        is_opinion: typing.Optional[bool] = None,
        is_paid_content: typing.Optional[bool] = None,
        word_count_min: typing.Optional[int] = None,
        word_count_max: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        include_nlp_data: typing.Optional[bool] = None,
        has_nlp: typing.Optional[bool] = None,
        theme: typing.Optional[str] = None,
        not_theme: typing.Optional[str] = None,
        title_sentiment_min: typing.Optional[float] = None,
        title_sentiment_max: typing.Optional[float] = None,
        content_sentiment_min: typing.Optional[float] = None,
        content_sentiment_max: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorsGetResponse:
        """
        This endpoint allows you to search for articles by author. You need to specify the author name. You can also filter by language, country, source, and more.

        Parameters
        ----------
        author_name : str

        sources : str

        predefined_sources : str

        not_sources : str

        lang : str

        not_lang : str

        countries : str

        not_countries : str

        parent_url : str

        all_links : str

        all_domain_links : str

        iptc_tags : str

        not_iptc_tags : str

        iab_tags : str

        not_iab_tags : str

        not_author_name : typing.Optional[str]

        from_ : typing.Optional[str]

        to : typing.Optional[str]

        published_date_precision : typing.Optional[str]

        by_parse_date : typing.Optional[bool]

        sort_by : typing.Optional[str]

        ranked_only : typing.Optional[str]

        from_rank : typing.Optional[int]

        to_rank : typing.Optional[int]

        is_headline : typing.Optional[bool]

        is_opinion : typing.Optional[bool]

        is_paid_content : typing.Optional[bool]

        word_count_min : typing.Optional[int]

        word_count_max : typing.Optional[int]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        include_nlp_data : typing.Optional[bool]

        has_nlp : typing.Optional[bool]

        theme : typing.Optional[str]

        not_theme : typing.Optional[str]

        title_sentiment_min : typing.Optional[float]

        title_sentiment_max : typing.Optional[float]

        content_sentiment_min : typing.Optional[float]

        content_sentiment_max : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorsGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from newscatcher import AsyncNewscatcherApi

        client = AsyncNewscatcherApi(
            api_token="YOUR_API_TOKEN",
        )


        async def main() -> None:
            await client.authors.get(
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


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/authors",
            method="GET",
            params={
                "author_name": author_name,
                "not_author_name": not_author_name,
                "sources": sources,
                "predefined_sources": predefined_sources,
                "not_sources": not_sources,
                "lang": lang,
                "not_lang": not_lang,
                "countries": countries,
                "not_countries": not_countries,
                "from_": from_,
                "to_": to,
                "published_date_precision": published_date_precision,
                "by_parse_date": by_parse_date,
                "sort_by": sort_by,
                "ranked_only": ranked_only,
                "from_rank": from_rank,
                "to_rank": to_rank,
                "is_headline": is_headline,
                "is_opinion": is_opinion,
                "is_paid_content": is_paid_content,
                "parent_url": parent_url,
                "all_links": all_links,
                "all_domain_links": all_domain_links,
                "word_count_min": word_count_min,
                "word_count_max": word_count_max,
                "page": page,
                "page_size": page_size,
                "include_nlp_data": include_nlp_data,
                "has_nlp": has_nlp,
                "theme": theme,
                "not_theme": not_theme,
                "title_sentiment_min": title_sentiment_min,
                "title_sentiment_max": title_sentiment_max,
                "content_sentiment_min": content_sentiment_min,
                "content_sentiment_max": content_sentiment_max,
                "iptc_tags": iptc_tags,
                "not_iptc_tags": not_iptc_tags,
                "iab_tags": iab_tags,
                "not_iab_tags": not_iab_tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AuthorsGetResponse,
                    parse_obj_as(
                        type_=AuthorsGetResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def post(
        self,
        *,
        author_name: str,
        not_author_name: typing.Optional[str] = OMIT,
        sources: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        predefined_sources: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        not_sources: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        lang: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        not_lang: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        countries: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        not_countries: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        from_: typing.Optional[AuthorSearchRequestFrom] = OMIT,
        to: typing.Optional[AuthorSearchRequestTo] = OMIT,
        published_date_precision: typing.Optional[str] = OMIT,
        by_parse_date: typing.Optional[bool] = OMIT,
        sort_by: typing.Optional[str] = OMIT,
        ranked_only: typing.Optional[AuthorSearchRequestRankedOnly] = OMIT,
        from_rank: typing.Optional[int] = OMIT,
        to_rank: typing.Optional[int] = OMIT,
        is_headline: typing.Optional[bool] = OMIT,
        is_opinion: typing.Optional[bool] = OMIT,
        is_paid_content: typing.Optional[bool] = OMIT,
        parent_url: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        all_links: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        all_domain_links: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        word_count_min: typing.Optional[int] = OMIT,
        word_count_max: typing.Optional[int] = OMIT,
        page: typing.Optional[int] = OMIT,
        page_size: typing.Optional[int] = OMIT,
        include_nlp_data: typing.Optional[bool] = OMIT,
        has_nlp: typing.Optional[bool] = OMIT,
        theme: typing.Optional[str] = OMIT,
        not_theme: typing.Optional[str] = OMIT,
        title_sentiment_min: typing.Optional[float] = OMIT,
        title_sentiment_max: typing.Optional[float] = OMIT,
        content_sentiment_min: typing.Optional[float] = OMIT,
        content_sentiment_max: typing.Optional[float] = OMIT,
        iptc_tags: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        not_iptc_tags: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        iab_tags: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        not_iab_tags: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorsPostResponse:
        """
        This endpoint allows you to search for articles by author. You need to specify the author name. You can also filter by language, country, source, and more.

        Parameters
        ----------
        author_name : str

        not_author_name : typing.Optional[str]

        sources : typing.Optional[typing.Optional[typing.Any]]

        predefined_sources : typing.Optional[typing.Optional[typing.Any]]

        not_sources : typing.Optional[typing.Optional[typing.Any]]

        lang : typing.Optional[typing.Optional[typing.Any]]

        not_lang : typing.Optional[typing.Optional[typing.Any]]

        countries : typing.Optional[typing.Optional[typing.Any]]

        not_countries : typing.Optional[typing.Optional[typing.Any]]

        from_ : typing.Optional[AuthorSearchRequestFrom]

        to : typing.Optional[AuthorSearchRequestTo]

        published_date_precision : typing.Optional[str]

        by_parse_date : typing.Optional[bool]

        sort_by : typing.Optional[str]

        ranked_only : typing.Optional[AuthorSearchRequestRankedOnly]

        from_rank : typing.Optional[int]

        to_rank : typing.Optional[int]

        is_headline : typing.Optional[bool]

        is_opinion : typing.Optional[bool]

        is_paid_content : typing.Optional[bool]

        parent_url : typing.Optional[typing.Optional[typing.Any]]

        all_links : typing.Optional[typing.Optional[typing.Any]]

        all_domain_links : typing.Optional[typing.Optional[typing.Any]]

        word_count_min : typing.Optional[int]

        word_count_max : typing.Optional[int]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        include_nlp_data : typing.Optional[bool]

        has_nlp : typing.Optional[bool]

        theme : typing.Optional[str]

        not_theme : typing.Optional[str]

        title_sentiment_min : typing.Optional[float]

        title_sentiment_max : typing.Optional[float]

        content_sentiment_min : typing.Optional[float]

        content_sentiment_max : typing.Optional[float]

        iptc_tags : typing.Optional[typing.Optional[typing.Any]]

        not_iptc_tags : typing.Optional[typing.Optional[typing.Any]]

        iab_tags : typing.Optional[typing.Optional[typing.Any]]

        not_iab_tags : typing.Optional[typing.Optional[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorsPostResponse
            Successful Response

        Examples
        --------
        import asyncio

        from newscatcher import AsyncNewscatcherApi

        client = AsyncNewscatcherApi(
            api_token="YOUR_API_TOKEN",
        )


        async def main() -> None:
            await client.authors.post(
                author_name="author_name",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/authors",
            method="POST",
            json={
                "author_name": author_name,
                "not_author_name": not_author_name,
                "sources": sources,
                "predefined_sources": predefined_sources,
                "not_sources": not_sources,
                "lang": lang,
                "not_lang": not_lang,
                "countries": countries,
                "not_countries": not_countries,
                "from_": convert_and_respect_annotation_metadata(
                    object_=from_, annotation=AuthorSearchRequestFrom, direction="write"
                ),
                "to_": convert_and_respect_annotation_metadata(
                    object_=to, annotation=AuthorSearchRequestTo, direction="write"
                ),
                "published_date_precision": published_date_precision,
                "by_parse_date": by_parse_date,
                "sort_by": sort_by,
                "ranked_only": convert_and_respect_annotation_metadata(
                    object_=ranked_only,
                    annotation=AuthorSearchRequestRankedOnly,
                    direction="write",
                ),
                "from_rank": from_rank,
                "to_rank": to_rank,
                "is_headline": is_headline,
                "is_opinion": is_opinion,
                "is_paid_content": is_paid_content,
                "parent_url": parent_url,
                "all_links": all_links,
                "all_domain_links": all_domain_links,
                "word_count_min": word_count_min,
                "word_count_max": word_count_max,
                "page": page,
                "page_size": page_size,
                "include_nlp_data": include_nlp_data,
                "has_nlp": has_nlp,
                "theme": theme,
                "not_theme": not_theme,
                "title_sentiment_min": title_sentiment_min,
                "title_sentiment_max": title_sentiment_max,
                "content_sentiment_min": content_sentiment_min,
                "content_sentiment_max": content_sentiment_max,
                "iptc_tags": iptc_tags,
                "not_iptc_tags": not_iptc_tags,
                "iab_tags": iab_tags,
                "not_iab_tags": not_iab_tags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AuthorsPostResponse,
                    parse_obj_as(
                        type_=AuthorsPostResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)