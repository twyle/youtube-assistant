from youtube.models import Channel, Search
from youtube.schemas import (SearchOptionalParameters, SearchPart,
                             YouTubeListResponse, YouTubeRequest,
                             YouTubeResponse)

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


def get_my_channel_details() -> Channel:
    """Get my channel details"""
    response: YouTubeListResponse = youtube_client.find_my_channel()
    channel: channel = response.items[0]
    return channel


def get_favorite_channels(user_name: str = "Lyle") -> list[str]:
    """Get the users favorite channels."""
    return ["Ark Invest", "Real Engineering"]


def latest_video_search(channel_id: str) -> Search:
    """Get the latest video uploaded to a youtube channel."""
    search_part: SearchPart = SearchPart()
    optional_params: SearchOptionalParameters = SearchOptionalParameters(
        channelId=channel_id,
        q="",
        order="date",
        type=["video"],
    )
    search_schema: YouTubeRequest = YouTubeRequest(
        part=search_part, optional_parameters=optional_params
    )
    response: YouTubeResponse = youtube_client.search(search_schema)
    latest_video: Search = response.items[0]
    return latest_video


def get_channel_latest_video(channel_title: str) -> str:
    """Get the channels latest video."""
    channel_id: str = get_channel_id(channel_title)
    latest_video: Search = latest_video_search(channel_id)
    return latest_video.title


def get_favorite_channels_latest_videos(user_name: str = "Lyle") -> str:
    """Get the latest videos from your favorite channels."""
    daily_videos_str: str = "Here are the latest videos from your favorite channels: "
    favorite_channels: str = get_favorite_channels(user_name)
    for i, channel_title in enumerate(favorite_channels, start=1):
        latest_video: str = get_channel_latest_video(channel_title)
        daily_videos_str += f"\n{i}. {latest_video} from {channel_title}"
    return daily_videos_str


def find_my_youtube_username() -> str:
    """Find the authenticated users user name."""
    my_channel: Channel = get_my_channel_details()
    my_user_name: str = my_channel.snippet.custom_url
    return my_user_name
