from typing import Optional, Type

from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
from youtube.models import PlaylistItem

from .helpers import add_video_to_playlist


class InsertVideoIntoPlaylist(BaseModel):
    video_title: str = Field(description="The video title.")
    playlist_title: str = Field(description="The playlist title.")
    position: Optional[int] = Field(
        description="The position to insert the video into."
    )


class InsertVideoIntoPlaylistTool(StructuredTool):
    name = "video_insert"
    description = """
    useful when you need to add a youtube video into a youtube playlist. for example 
    Add the video 'He Quit Uber to Build a Trillion Dollar Company' to the playlist 
    'Web Development for beginners'
    """
    args_schema: Type[BaseModel] = InsertVideoIntoPlaylist

    def _run(
        self,
        video_title: str,
        playlist_title: str,
        position: Optional[int] = 0,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        playlist_item: PlaylistItem = add_video_to_playlist(video_title, playlist_title)
        return {
            "playlist title": playlist_title,
            "video title": video_title,
            "position": position,
        }

    async def _arun(
        self,
        video_id: str,
        playlist_id: str,
        position: Optional[int] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")
