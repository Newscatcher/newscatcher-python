# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .article_result import ArticleResult
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class FailedSearchResponse(UniversalBaseModel):
    """
    FailedSearchResponse DTO class.
    """

    status: typing.Optional[str] = None
    total_hits: typing.Optional[int] = None
    page: typing.Optional[int] = None
    total_pages: typing.Optional[int] = None
    page_size: typing.Optional[int] = None
    articles: typing.Optional[typing.List[ArticleResult]] = None
    user_input: typing.Dict[str, typing.Optional[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
