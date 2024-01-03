from youtube.models import Search, Video
from youtube.schemas import (
    SearchPart, SearchOptionalParameters, YouTubeRequest, YouTubeResponse,
    YouTubeListResponse
)
from ...extensions import youtube_client

def get_video_id(video_title: str) -> str:
    """Get video id given the title."""
    part: SearchPart = SearchPart()
    optional_parameters: SearchOptionalParameters = SearchOptionalParameters(
        q=video_title,
        maxResults=1,
        type=['video']
    )
    search_request: YouTubeRequest = YouTubeRequest(
        part=part, 
        optional_parameters=optional_parameters
    )
    search_results: YouTubeResponse = youtube_client.search(search_request)
    search_result: Search = search_results.items[0]
    return search_result.resource_id

def get_video_details(video_title: str) -> Video:
    """Get video details"""
    video_id: str = get_video_id(video_title)
    response: YouTubeListResponse = youtube_client.find_video_by_id(video_id)
    video: Video = response.items[0]
    return video