from langchain.tools import BaseTool
from typing import Optional
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
) 
from youtube.models import Playlist
from pydantic import BaseModel, Field
from ...utils.playlist_utils import create_playlist


class CreatePlaylist(BaseModel):
    title: str = Field(description='The title for the youtube playlist.')
    description: Optional[str] = Field(description='What this playlist is used for.')
    privacy_status: Optional[str] = Field(description='The playlist should be private or public.')


class CreatePlaylistTool(BaseTool):
    name = "create_playlist"
    description = """
    useful when you need to create a playlist on youtube.
    """

    def _run(
        self, 
        title: str,
        description: Optional[str] = None,
        privacy_status: Optional[str] = 'private',
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        playlist: Playlist = create_playlist(title, privacy_status, description)
        return {
            'title': playlist.snippet.title,
            'privacy status': playlist.status.privacy_status,
            'id': playlist.id
        }

    async def _arun(
        self, 
        query: Optional[str] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")