# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .authors import Authors
from .journalists import Journalists
from .article_entity_all_links import ArticleEntityAllLinks
from .article_entity_all_domain_links import ArticleEntityAllDomainLinks
from .nlp_data_entity import NlpDataEntity
from .additional_domain_info_entity import AdditionalDomainInfoEntity
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ArticleEntity(UniversalBaseModel):
    """
    The data model representing a single article in the search results.
    """

    title: str = pydantic.Field()
    """
    The title of the article.
    """

    author: typing.Optional[str] = pydantic.Field(default=None)
    """
    The primary author of the article.
    """

    authors: typing.Optional[Authors] = pydantic.Field(default=None)
    """
    A list of authors of the article.
    """

    journalists: typing.Optional[Journalists] = pydantic.Field(default=None)
    """
    A list of journalists associated with the article.
    """

    published_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the article was published.
    """

    published_date_precision: typing.Optional[str] = pydantic.Field(default=None)
    """
    The precision of the published date.
    """

    updated_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the article was last updated.
    """

    updated_date_precision: typing.Optional[str] = pydantic.Field(default=None)
    """
    The precision of the updated date.
    """

    parse_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the article was parsed.
    """

    link: str = pydantic.Field()
    """
    The URL link to the article.
    """

    domain_url: str = pydantic.Field()
    """
    The domain URL of the article.
    """

    full_domain_url: str = pydantic.Field()
    """
    The full domain URL of the article.
    """

    name_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the source where the article was published.
    """

    is_headline: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the article is a headline.
    """

    paid_content: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the article is paid content.
    """

    parent_url: str = pydantic.Field()
    """
    The categorical URL of the article.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country where the article was published.
    """

    rights: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rights information for the article.
    """

    rank: int = pydantic.Field()
    """
    The rank of the article's source.
    """

    media: typing.Optional[str] = pydantic.Field(default=None)
    """
    The media associated with the article.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The language in which the article is written.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A brief description of the article.
    """

    content: str = pydantic.Field()
    """
    The content of the article.
    """

    word_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The word count of the article.
    """

    is_opinion: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the article is an opinion piece.
    """

    twitter_account: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Twitter account associated with the article.
    """

    all_links: typing.Optional[ArticleEntityAllLinks] = pydantic.Field(default=None)
    """
    A list of all URLs mentioned in the article.
    """

    all_domain_links: typing.Optional[ArticleEntityAllDomainLinks] = pydantic.Field(default=None)
    """
    A list of all domain URLs mentioned in the article.
    """

    nlp: typing.Optional[NlpDataEntity] = None
    id: str = pydantic.Field()
    """
    The unique identifier for the article.
    """

    score: float = pydantic.Field()
    """
    The relevance score of the article.
    """

    custom_tags: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic.Field(default=None)
    """
    An object that contains custom tags associated with an article, where each key is a taxonomy name, and the value is an array of tags.
    """

    additional_domain_info: typing.Optional[AdditionalDomainInfoEntity] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
