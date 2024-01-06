from typing import Optional

from youtube.models import Playlist, PlaylistItem
from youtube.schemas import CreatePlaylist, CreatePlaylistSnippet, CreateStatus

from ..extensions import youtube_client


def check_if_playlist_exists(playlist_name: str) -> bool:
    """Check if the given playlist exists."""
    return (
        f'The playlist called "{playlist_name}" already exists in your youtube channel.'
    )


def create_playlist(
    playlist_name: str,
    privacy_status: Optional[str] = "private",
    description: Optional[str] = None,
) -> str:
    """Create a playlist on youtube."""
    status: CreateStatus = CreateStatus(privacyStatus=privacy_status)
    snippet: CreatePlaylistSnippet = CreatePlaylistSnippet(
        title=playlist_name,
        description=description,
    )
    req: CreatePlaylist = CreatePlaylist(snippet=snippet, status=status)
    playlist: Playlist = youtube_client.insert_playlist(req)
    return playlist


def delete_playlist(playlist_name: str) -> bool:
    """Delete a playlist."""
    pass


def add_video_to_youtube_playlist(video_title: str, playlist_name: str) -> str:
    """Add a video to a playlist."""
    playlist_item: PlaylistItem = add_video_to_playlist(video_title, playlist_name)
    return playlist_item


def remove_video_from_playlist(video_name: str, playlist_name: str) -> bool:
    """Remove a video from a playlist."""
    pass


def check_video_in_playlist(video_name: str, playlist_name: str) -> bool:
    """Check if video is in playlist."""
    return False


daily_videos: str = """
Here are the latest videos from your favorite channels:

- Video One
- Video two

You can watch them over at http://localhost:8000.
"""


def get_daily_videos() -> str:
    """Get the videos in the Daily Videos playlist."""
    return daily_videos


add_channel_response: str = """
I have added the channle 'Channel Title' to your favorite channels. Here are some of the most 
recent videos uploaded to 'Channel Title':
    - Video Title - summary
    - Video Title - summary

Here are some of the most popular videos from 'Channel Title':
    - Video Title - summary
    - Video Title - summary
"""


def add_channel_to_favorites(channel_title: str = "") -> str:
    """Add a new channel to favorites."""
    return add_channel_response


remove_channel_response: str = """
I have removed the chanel 'Channel Title' from your favorites. Would you like to replace it 
perhaps with one of the following:
    - Channel title
"""


def remove_channel_from_favorites(channel_title: str = "") -> str:
    """Remove a channel from favorites."""
    return remove_channel_response
