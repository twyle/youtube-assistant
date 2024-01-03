from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from .helpers import delete_playlist


class DeleteYouTubePlaylist(BaseModel):
    title: str = Field(description='The playlist title.')


class DeleteYoutubePlaylistsTool(BaseTool):
    name = "delete_playlist"
    description = """
    useful when you need to delete a playlist on youtube.
    """
    args_schema: Type[BaseModel] = DeleteYouTubePlaylist

    def _run(
        self, 
        title: str,
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        delete_playlist(title)
        return {'title': title}

    async def _arun(
        self, 
        id: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")