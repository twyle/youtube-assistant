from datetime import datetime
from typing import Optional
from youtube.schemas import (
    SearchPart, SearchOptionalParameters, YouTubeResponse, YouTubeRequest, YouTubeListResponse
)
from youtube.models import Search, VideoCategory
from .extensions import youtube


def get_channel_id(channel_name: str) -> str:
    """Get the channel id."""
    response: YouTubeResponse = youtube.find_channel_by_name(channel_name)
    search_result: Search = response.items[0]
    return search_result.resource_id

def get_video_categories() -> str:
    """Get video categories."""
    response: YouTubeListResponse = youtube.get_video_categories()
    video_categories: list[VideoCategory] = response.items
    categories: list[dict[str, str]] = list()
    for category in video_categories:
        categories.append({
            'title': category.snippet.title,
            'id': category.id,
            'assignable': category.snippet.assignable
        })
    return categories
    

def get_latest_channel_videos(channel_id: str) -> str:
    """Find the latest videos by the given channel."""
    # channel_id: str = get_channel_id(channel_name)

def search_channel_videos(channel_name: str, query: str) -> str:
    """Search for videos matching the query in the given channel."""
    pass

def find_live_events(query: str) -> str:
    """Find live events on youtube."""
    pass

def search_location(query: str, location: str, location_radius: int) -> str:
    """Search for results in a given region."""
    pass

def advanced_video_search(
    channel_id: str, 
    query: str,
    max_results: Optional[int] = 10,
    order: Optional[str] = None,
    published_after: Optional[str] = None,
    published_before: Optional[str] = None,
    region_code: Optional[str] = None,
    relevance_language: Optional[str] = 'en',
    video_caption: Optional[str] = None,
    video_category_id: Optional[str] = None,
    video_definition: Optional[str] = None,
    video_dimension: Optional[str] = None,
    video_duration: Optional[str] = None,
    video_paid_product_placement: Optional[str] = None,
    video_syndicated: Optional[str] = None,
    video_type: Optional[str] = 'any'
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
        type=['video'],
        videoCaption=video_caption,
        videoCategoryId=video_category_id,
        videoDefinition=video_definition,
        videoDimension=video_dimension,
        videoDuration=video_duration,
        videoPaidProductPlacement=video_paid_product_placement,
        videoSyndicated=video_syndicated,
        videoType=video_type
    )
    search_schema: YouTubeRequest = YouTubeRequest(
        part=search_part, optional_parameters=optional_params
    )
    response: YouTubeResponse = youtube.search(search_schema)
    items: list[Search] = response.items
    return items

def advanced_channel_search(
    channel_name: str, 
    max_results: int,
    order: str,
    query: str,
    published_after: datetime,
    published_before: datetime,
    ) -> str:
    """Search the given channel for the given videos."""
    pass