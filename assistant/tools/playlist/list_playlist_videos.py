from langchain.tools import BaseTool
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
) 
from youtube.models import PlaylistItem
from .helpers import list_playlist_videos
from pydantic import Field, BaseModel


class ListPlaylistVideos(BaseModel):
    playlist_title: str = Field(description='The title for the youtube playlist.')
    channel_title: str = Field(description='The title for the youtube channel.')


class ListPlaylistVideosTool(BaseTool):
    name = "find_playlist_videos"
    description = """
    useful when you need to find the videos for a given youtube playlist.
    """
    args_schema: Type[BaseModel] = ListPlaylistVideos

    def _run(
        self, 
        playlist_title: str,
        channel_title: str,
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        playlist_items: list[PlaylistItem] = list_playlist_videos(channel_title, playlist_title)
        playlist_items: list[str] = [playlist_item.snippet.title for playlist_item in playlist_items]
        return playlist_items

    async def _arun(
        self, 
        query: Optional[str] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")