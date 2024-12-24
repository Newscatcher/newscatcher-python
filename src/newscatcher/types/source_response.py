# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .source_response_sources_item import SourceResponseSourcesItem
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SourceResponse(UniversalBaseModel):
    """
    SourceResponse DTO class.
    """

    message: str
    sources: typing.List[SourceResponseSourcesItem]
    user_input: typing.Dict[str, typing.Optional[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
