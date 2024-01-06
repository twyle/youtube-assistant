from typing import Optional, Type

from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from youtube.models import Video

from .helpers import get_video_details


class YouTubeVideoDetails(BaseModel):
    video_title: str = Field(description="The video title.")


class YouTubeVideoDetailsTool(BaseTool):
    name = "youtube_video_details"
    description = """
    useful when you need to find out all the details about a youtube video. This includes 
    the description, title, number of views, number of likes, the number of comments and
     when the video was created or updated.
    """
    args_schema: Type[BaseModel] = YouTubeVideoDetails

    def _run(
        self, video_title: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        video: Video = get_video_details(video_title)
        return {
            "id": video.id,
            "title": video.snippet.title,
            "description": video.snippet.description,
            "likes_count": video.statistics.likes_count,
            "comments_count": video.statistics.comments_count,
            "date_created": video.snippet.published_at,
            "views_count": video.statistics.views_count,
        }

    async def _arun(
        self, title: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError()
