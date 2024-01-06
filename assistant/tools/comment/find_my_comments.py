from typing import Optional

from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from youtube.models import Comment

from .helpers import find_my_comments


class FindMyComments(BaseModel):
    video_title: str = Field(description="The title for the youtube video.")


class FindMyCommentsTool(BaseTool):
    name = "find_my_comments"
    description = """
    useful when you need to find this users comments on a video on youtube for example find my comments 
    on the video 'Trapping Rain Water - Google Interview Question - Leetcode 42'
    """

    def _run(
        self,
        video_title: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        video_comments: list[Comment] = find_my_comments(video_title)
        return [
            {
                "Video Title": video_title,
                "Comment": video_comment.snippet.text_display,
            }
            for video_comment in video_comments
        ]

    async def _arun(
        self,
        query: Optional[str] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")
