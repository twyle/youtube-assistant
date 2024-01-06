from typing import Optional

from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from youtube.models import Comment

from .helpers import find_author_comments


class FindUserComments(BaseModel):
    video_title: str = Field(description="The title for the youtube video.")
    author_name: str = Field(description="The name of the author ")


class FindUserCommentsTool(BaseTool):
    name = "find_user_comments"
    description = """
    useful when you need to find a given user's comments on a video on youtube 
    """

    def _run(
        self,
        video_title: str,
        author_name: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        video_comments: list[Comment] = find_author_comments(video_title, author_name)
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
