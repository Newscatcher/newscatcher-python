# This file was auto-generated by Fern from our API Definition.

import typing
from ...types.search_similar_response_dto import SearchSimilarResponseDto
from ...types.failed_search_similar_response_dto import FailedSearchSimilarResponseDto

SearchSimilarGetResponse = typing.Union[SearchSimilarResponseDto, FailedSearchSimilarResponseDto]
