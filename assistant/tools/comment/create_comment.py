from langchain.tools import BaseTool
from typing import Optional
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
) 
from youtube.models import Comment
from pydantic import BaseModel, Field
from .helpers import comment_on_video


class CreateComment(BaseModel):
    video_title: str = Field(description='The title for the youtube video.')
    comment: str = Field(description='The comment text')


class CreateCommentTool(BaseTool):
    name = "create_comment"
    description = """
    useful when you need to comment on a video on youtube
    """

    def _run(
        self, 
        video_title: str,
        comment: str,
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        video_comment: Comment = comment_on_video(video_title, comment)
        return {
            'Video Title': video_title,
            'Comment': video_comment.snippet.text_display
        }

    async def _arun(
        self, 
        query: Optional[str] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")