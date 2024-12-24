# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .authors import Authors
from .journalists import Journalists
from .dto_responses_more_like_this_response_article_result_all_links import (
    DtoResponsesMoreLikeThisResponseArticleResultAllLinks,
)
from .dto_responses_more_like_this_response_article_result_all_domain_links import (
    DtoResponsesMoreLikeThisResponseArticleResultAllDomainLinks,
)
from .similar_document import SimilarDocument
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ArticleResult(UniversalBaseModel):
    """
    ArticleResult DTO class.
    """

    title: str
    author: typing.Optional[str] = None
    authors: typing.Optional[Authors] = None
    journalists: typing.Optional[Journalists] = None
    published_date: typing.Optional[str] = None
    published_date_precision: typing.Optional[str] = None
    updated_date: typing.Optional[str] = None
    updated_date_precision: typing.Optional[str] = None
    parse_date: typing.Optional[str] = None
    link: str
    domain_url: str
    full_domain_url: str
    name_source: typing.Optional[str] = None
    is_headline: typing.Optional[str] = None
    paid_content: typing.Optional[bool] = None
    extraction_data: str
    country: typing.Optional[str] = None
    rights: typing.Optional[str] = None
    rank: int
    media: typing.Optional[str] = None
    language: typing.Optional[str] = None
    description: typing.Optional[str] = None
    content: str
    title_translated_en: typing.Optional[str] = None
    content_translated_en: typing.Optional[str] = None
    word_count: typing.Optional[int] = None
    is_opinion: typing.Optional[bool] = None
    twitter_account: typing.Optional[str] = None
    all_links: typing.Optional[
        DtoResponsesMoreLikeThisResponseArticleResultAllLinks
    ] = None
    all_domain_links: typing.Optional[
        DtoResponsesMoreLikeThisResponseArticleResultAllDomainLinks
    ] = None
    nlp: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    id: str
    score: float
    similar_documents: typing.Optional[typing.List[SimilarDocument]] = None
    custom_tags: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
