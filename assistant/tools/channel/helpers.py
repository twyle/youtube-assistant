from youtube.models import Channel, Search
from youtube.schemas import YouTubeResponse, YouTubeListResponse
from ...extensions import youtube_client



def get_channel_id(channel_name: str) -> str:
    """Get the channel id."""
    response: YouTubeResponse = youtube_client.find_channel_by_name(channel_name)
    search_result: Search = response.items[0]
    return search_result.resource_id

def get_channel_details(channel_title: str) -> Channel:
    """Get channel details"""
    channel_id: str = get_channel_id(channel_title)
    response: YouTubeListResponse = youtube_client.find_channel_by_id(channel_id)
    channel: channel = response.items[0]
    return channel