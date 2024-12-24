# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.source_response import SourceResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        lang: str,
        countries: str,
        predefined_sources: str,
        source_name: str,
        source_url: str,
        news_domain_type: str,
        news_type: str,
        include_additional_info: typing.Optional[bool] = None,
        from_rank: typing.Optional[int] = None,
        to_rank: typing.Optional[int] = None,
        is_news_domain: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceResponse:
        """
        This endpoint allows you to get the list of sources that are available in the database. You can filter the sources by language and country. The maximum number of sources displayed is set according to your plan. You can find the list of plans and their features here: https://newscatcherapi.com/news-api#news-api-pricing

        Parameters
        ----------
        lang : str

        countries : str

        predefined_sources : str

        source_name : str

        source_url : str

        news_domain_type : str

        news_type : str

        include_additional_info : typing.Optional[bool]

        from_rank : typing.Optional[int]

        to_rank : typing.Optional[int]

        is_news_domain : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceResponse
            Successful Response

        Examples
        --------
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
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/sources",
            method="GET",
            params={
                "lang": lang,
                "countries": countries,
                "predefined_sources": predefined_sources,
                "include_additional_info": include_additional_info,
                "from_rank": from_rank,
                "to_rank": to_rank,
                "source_name": source_name,
                "source_url": source_url,
                "is_news_domain": is_news_domain,
                "news_domain_type": news_domain_type,
                "news_type": news_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SourceResponse,
                    parse_obj_as(
                        type_=SourceResponse,  # type: ignore
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
        lang: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        countries: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        predefined_sources: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        include_additional_info: typing.Optional[bool] = OMIT,
        from_rank: typing.Optional[int] = OMIT,
        to_rank: typing.Optional[int] = OMIT,
        source_name: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        source_url: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        is_news_domain: typing.Optional[bool] = OMIT,
        news_domain_type: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        news_type: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceResponse:
        """
        This endpoint allows you to get the list of sources that are available in the database. You can filter the sources by language and country. The maximum number of sources displayed is set according to your plan. You can find the list of plans and their features here: https://newscatcherapi.com/news-api#news-api-pricing

        Parameters
        ----------
        lang : typing.Optional[typing.Optional[typing.Any]]

        countries : typing.Optional[typing.Optional[typing.Any]]

        predefined_sources : typing.Optional[typing.Optional[typing.Any]]

        include_additional_info : typing.Optional[bool]

        from_rank : typing.Optional[int]

        to_rank : typing.Optional[int]

        source_name : typing.Optional[typing.Optional[typing.Any]]

        source_url : typing.Optional[typing.Optional[typing.Any]]

        is_news_domain : typing.Optional[bool]

        news_domain_type : typing.Optional[typing.Optional[typing.Any]]

        news_type : typing.Optional[typing.Optional[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceResponse
            Successful Response

        Examples
        --------
        from newscatcher import NewscatcherApi

        client = NewscatcherApi(
            api_token="YOUR_API_TOKEN",
        )
        client.sources.post()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/sources",
            method="POST",
            json={
                "lang": lang,
                "countries": countries,
                "predefined_sources": predefined_sources,
                "include_additional_info": include_additional_info,
                "from_rank": from_rank,
                "to_rank": to_rank,
                "source_name": source_name,
                "source_url": source_url,
                "is_news_domain": is_news_domain,
                "news_domain_type": news_domain_type,
                "news_type": news_type,
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
                    SourceResponse,
                    parse_obj_as(
                        type_=SourceResponse,  # type: ignore
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


class AsyncSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        lang: str,
        countries: str,
        predefined_sources: str,
        source_name: str,
        source_url: str,
        news_domain_type: str,
        news_type: str,
        include_additional_info: typing.Optional[bool] = None,
        from_rank: typing.Optional[int] = None,
        to_rank: typing.Optional[int] = None,
        is_news_domain: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceResponse:
        """
        This endpoint allows you to get the list of sources that are available in the database. You can filter the sources by language and country. The maximum number of sources displayed is set according to your plan. You can find the list of plans and their features here: https://newscatcherapi.com/news-api#news-api-pricing

        Parameters
        ----------
        lang : str

        countries : str

        predefined_sources : str

        source_name : str

        source_url : str

        news_domain_type : str

        news_type : str

        include_additional_info : typing.Optional[bool]

        from_rank : typing.Optional[int]

        to_rank : typing.Optional[int]

        is_news_domain : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceResponse
            Successful Response

        Examples
        --------
        import asyncio

        from newscatcher import AsyncNewscatcherApi

        client = AsyncNewscatcherApi(
            api_token="YOUR_API_TOKEN",
        )


        async def main() -> None:
            await client.sources.get(
                lang="lang",
                countries="countries",
                predefined_sources="predefined_sources",
                source_name="source_name",
                source_url="source_url",
                news_domain_type="news_domain_type",
                news_type="news_type",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/sources",
            method="GET",
            params={
                "lang": lang,
                "countries": countries,
                "predefined_sources": predefined_sources,
                "include_additional_info": include_additional_info,
                "from_rank": from_rank,
                "to_rank": to_rank,
                "source_name": source_name,
                "source_url": source_url,
                "is_news_domain": is_news_domain,
                "news_domain_type": news_domain_type,
                "news_type": news_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SourceResponse,
                    parse_obj_as(
                        type_=SourceResponse,  # type: ignore
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
        lang: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        countries: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        predefined_sources: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        include_additional_info: typing.Optional[bool] = OMIT,
        from_rank: typing.Optional[int] = OMIT,
        to_rank: typing.Optional[int] = OMIT,
        source_name: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        source_url: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        is_news_domain: typing.Optional[bool] = OMIT,
        news_domain_type: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        news_type: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceResponse:
        """
        This endpoint allows you to get the list of sources that are available in the database. You can filter the sources by language and country. The maximum number of sources displayed is set according to your plan. You can find the list of plans and their features here: https://newscatcherapi.com/news-api#news-api-pricing

        Parameters
        ----------
        lang : typing.Optional[typing.Optional[typing.Any]]

        countries : typing.Optional[typing.Optional[typing.Any]]

        predefined_sources : typing.Optional[typing.Optional[typing.Any]]

        include_additional_info : typing.Optional[bool]

        from_rank : typing.Optional[int]

        to_rank : typing.Optional[int]

        source_name : typing.Optional[typing.Optional[typing.Any]]

        source_url : typing.Optional[typing.Optional[typing.Any]]

        is_news_domain : typing.Optional[bool]

        news_domain_type : typing.Optional[typing.Optional[typing.Any]]

        news_type : typing.Optional[typing.Optional[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceResponse
            Successful Response

        Examples
        --------
        import asyncio

        from newscatcher import AsyncNewscatcherApi

        client = AsyncNewscatcherApi(
            api_token="YOUR_API_TOKEN",
        )


        async def main() -> None:
            await client.sources.post()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/sources",
            method="POST",
            json={
                "lang": lang,
                "countries": countries,
                "predefined_sources": predefined_sources,
                "include_additional_info": include_additional_info,
                "from_rank": from_rank,
                "to_rank": to_rank,
                "source_name": source_name,
                "source_url": source_url,
                "is_news_domain": is_news_domain,
                "news_domain_type": news_domain_type,
                "news_type": news_type,
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
                    SourceResponse,
                    parse_obj_as(
                        type_=SourceResponse,  # type: ignore
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
