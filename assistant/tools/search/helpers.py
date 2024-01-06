from typing import Optional

from youtube.models import Search
from youtube.schemas import SearchOptionalParameters, SearchPart, YouTubeRequest, YouTubeResponse

from ...extensions import youtube_client


def advanced_video_search(
    query: str,
    channel_id: Optional[str] = None,
    max_results: Optional[int] = 10,
    order: Optional[str] = None,
    published_after: Optional[str] = None,
    published_before: Optional[str] = None,
    region_code: Optional[str] = None,
    relevance_language: Optional[str] = "en",
    video_caption: Optional[str] = None,
    video_category_id: Optional[str] = None,
    video_definition: Optional[str] = None,
    video_dimension: Optional[str] = None,
    video_duration: Optional[str] = None,
    video_paid_product_placement: Optional[str] = None,
    video_syndicated: Optional[str] = None,
    video_type: Optional[str] = "any",
) -> str:
    """Search the given channel for the given videos."""
    search_part: SearchPart = SearchPart()
    optional_params: SearchOptionalParameters = SearchOptionalParameters(
        channelId=channel_id,
        q=query,
        maxResults=max_results,
        order=order,
        publishedAfter=published_after,
        publishedBefore=published_before,
        regionCode=region_code,
        relevanceLanguage=relevance_language,
        type=["video"],
        videoCaption=video_caption,
        videoCategoryId=video_category_id,
        videoDefinition=video_definition,
        videoDimension=video_dimension,
        videoDuration=video_duration,
        videoPaidProductPlacement=video_paid_product_placement,
        videoSyndicated=video_syndicated,
        videoType=video_type,
    )
    search_schema: YouTubeRequest = YouTubeRequest(
        part=search_part, optional_parameters=optional_params
    )
    response: YouTubeResponse = youtube_client.search(search_schema)
    items: list[Search] = response.items
    return items
