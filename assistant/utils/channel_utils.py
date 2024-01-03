from ..extensions import youtube_client
from youtube.models import Search
from youtube.schemas import YouTubeResponse
from datetime import datetime
from .youtube_utils.search_utils import latest_video_search


channel_subscription: str = """
Is there Any other channels you would like to add? Here are other similar channels:

- Channel one - summary
- Channel Two - summary
"""

def get_channel_suggestions() -> str:
    """Get other channels to subscribe to."""
    return channel_subscription


def get_channel_id(channel_name: str) -> str:
    """Get the channel id."""
    response: YouTubeResponse = youtube_client.find_channel_by_name(channel_name)
    search_result: Search = response.items[0]
    return search_result.resource_id

def get_channel_latest_video(channel_title: str) -> str:
    """Get the channels latest video."""
    channel_id: str = get_channel_id(channel_title)
    latest_video: Search = latest_video_search(channel_id)
    return latest_video.title

def get_favorite_channels(user_name: str = 'Lyle') -> list[str]:
    """Get the users favorite channels."""
    return ['Ark Invest', 'Real Engineering']

def get_favorite_channels_latest_videos(user_name: str = 'Lyle') -> str:
    """Get the latest videos from your favorite channels."""
    daily_videos_str: str = "Here are the latest videos from your favorite channels: "
    favorite_channels: str = get_favorite_channels(user_name)
    for i, channel_title in enumerate(favorite_channels, start=1):
        latest_video: str = get_channel_latest_video(channel_title)
        daily_videos_str += f'\n{i}. {latest_video} from {channel_title}'
    daily_videos_url: str = 'https://www.youtube.com/playlist?list=PL_26vmg8W_AcEEl_Bo2AhziS-93r6b8bu'
    daily_videos_str += f"\n. You can watch them over at {daily_videos_url}"
    return daily_videos_str