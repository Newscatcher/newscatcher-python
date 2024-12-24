# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AdditionalSourceInfo(UniversalBaseModel):
    """
    AdditionalSourceInfo DTO class.
    """

    nb_articles_for_7_d: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="nb_articles_for_7d")
    ] = None
    country: typing.Optional[str] = None
    rank: typing.Optional[int] = None
    is_news_domain: typing.Optional[bool] = None
    news_domain_type: typing.Optional[str] = None
    news_type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
