from typing import Optional, Type

from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from youtube.models import Playlist

from .helpers import list_channel_playlists


class ListChannelPlaylists(BaseModel):
    title: str = Field(description="The title for the youtube channel.")
    max_results: Optional[int] = Field(
        description="Max search results to return.", default=25
    )


class ListChannelPlaylistsTool(BaseTool):
    name = "list_channel_playlists"
    description = """
    useful when you need to find the playlists for a given youtube channel.
    """
    args_schema: Type[BaseModel] = ListChannelPlaylists

    def parse_playlists(self, playlists: list[Playlist]) -> dict:
        """Parse playlists."""
        return [playlist.snippet.title for playlist in playlists]

    def _run(
        self,
        title: str,
        max_results: Optional[int] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        playlists: list[str] = list_channel_playlists(title)
        return playlists

    async def _arun(
        self,
        query: Optional[str] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")
