from typing import Optional, Type

from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools import BaseTool
from youtube.models import Playlist

from .helpers import list_my_channel_playlists


class ListUserPlaylistsTool(BaseTool):
    name = "list_user_playlists"
    description = """
    useful when you need to find all the playlists for a given user. for example 
    find all my youtube playlists.
    """

    def parse_playlists(self, playlists: list[Playlist]) -> dict:
        """Parse playlists."""
        return [playlist.snippet.title for playlist in playlists]

    def _run(
        self,
        query: Optional[str] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        my_playlists: list[Playlist] = list_my_channel_playlists()
        return self.parse_playlists(my_playlists)

    async def _arun(
        self,
        query: Optional[str] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")
