from youtube.models import PlaylistItem, Playlist, Search
from typing import Optional, Iterator
from youtube.schemas import (
    CreateStatus, CreatePlaylistSnippet, CreatePlaylist, YouTubeResponse, 
    VideoResourceId, CreatePlaylistItemSnippet, CreatePlaylistItem
)
from thefuzz import process, fuzz
from ...extensions import youtube_client
from ..video.helpers import get_video_id


def get_playlist_id(playlist_title: str) -> str:
    """Get a playlist's id given it's title."""
    playlist_iterator: Iterator = youtube_client.get_my_playlists_iterator()
    for playlists in playlist_iterator:
        for playlist in playlists:
            if playlist.snippet.title == playlist_title:
                return playlist.id


def check_if_playlist_exists(playlist_name: str) -> bool:
    """Check if the given playlist exists."""
    return f'The playlist called "{playlist_name}" already exists in your youtube channel.'

def create_playlist(playlist_name: str, privacy_status: Optional[str] = 'private', description: Optional[str] = None) -> str:
    """Create a playlist on youtube."""
    status: CreateStatus = CreateStatus(
        privacyStatus=privacy_status
    )
    snippet: CreatePlaylistSnippet = CreatePlaylistSnippet(
        title=playlist_name,
        description=description,
    )
    req: CreatePlaylist = CreatePlaylist(
        snippet=snippet,
        status=status
    )
    playlist: Playlist = youtube_client.insert_playlist(req)
    return playlist

def delete_playlist(playlist_name: str) -> bool:
    """Delete a playlist."""
    playlist_id: str = get_playlist_id(playlist_name)
    youtube_client.delete_playlist(playlist_id)
    
def add_video_to_playlist(video_title: str, playlist_title: str) -> PlaylistItem:
    """Add a video to a playlist."""
    video_id: str = get_video_id(video_title)
    playlist_id: str = get_playlist_id(playlist_title)
    resource_id: VideoResourceId = VideoResourceId(
        videoId=video_id
    )
    snippet: CreatePlaylistItemSnippet = CreatePlaylistItemSnippet(
        playlistId=playlist_id, resourceId=resource_id
    )
    create: CreatePlaylistItem = CreatePlaylistItem(snippet=snippet)
    playlist_item: PlaylistItem = youtube_client.insert_playlist_item(
        create_item=create
    )
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
def add_channel_to_favorites(channel_title: str = '') -> str:
    """Add a new channel to favorites."""
    return add_channel_response

remove_channel_response: str = """
I have removed the chanel 'Channel Title' from your favorites. Would you like to replace it 
perhaps with one of the following:
    - Channel title
"""
def remove_channel_from_favorites(channel_title: str = '') -> str:
    """Remove a channel from favorites."""
    return remove_channel_response


def list_channel_playlists(channel_title: str) -> list[Playlist]:
    """List a channels playlists."""        
    youtube_response: YouTubeResponse = youtube_client.find_channel_by_name(channel_title)
    search_result: Search = youtube_response.items[0]
    channel_id: str = search_result.channel_id
    response: YouTubeResponse = youtube_client.find_channel_playlists(
        channel_id=channel_id
    )
    playlists: list[Playlist] = response.items
    return playlists

def list_my_channel_playlists() -> list[Playlist]:
    """List a channels playlists."""        
    my_playlists: list[Playlist] = list()
    my_playlists_it: Iterator = youtube_client.get_my_playlists_iterator()
    for playlists in my_playlists_it:
        for playlist in playlists:
            my_playlists.append(playlist)
    return my_playlists
    
    
def list_playlist_videos(channel_title: str, playlist_title: str, max_results: Optional[int] = 10) -> list[PlaylistItem]:
    """List a playlist videos."""
    channel_playlists: list[Playlist] = list_channel_playlists(channel_title)
    playlists: dict[str, str] = {
        playlist.snippet.title: playlist.id for playlist in channel_playlists
    }
    playlist: str = process.extract(playlist_title, list(playlists.keys()), scorer=fuzz.ratio)[0][0]
    playlist_id: str = playlists[playlist]
    response: YouTubeResponse = youtube_client.find_playlist_items(
        playlist_id=playlist_id
    )
    playlist_items: list[PlaylistItem] = response.items
    return playlist_items