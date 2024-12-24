# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .cluster import Cluster
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ClusteringSearchResponse(UniversalBaseModel):
    """
    ClusteringSearchResponse DTO class.
    """

    status: typing.Optional[str] = None
    total_hits: int
    page: int
    total_pages: int
    page_size: int
    clusters_count: int
    clusters: typing.List[Cluster]
    user_input: typing.Dict[str, typing.Optional[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
