from typing import Optional

from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from youtube.models import Comment

from .helpers import reply_to_comment


class ReplyComment(BaseModel):
    video_title: str = Field(description="The title for the youtube video.")
    comment: str = Field(description="The comment text")
    author_name: str = Field(description="The name of the author ")


class ReplyCommentTool(BaseTool):
    name = "reply_comment"
    description = """
    useful when you need to reply to a comment on a video on youtube
    """

    def _run(
        self,
        video_title: str,
        comment: str,
        author_name: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        comment: Comment = reply_to_comment(author_name, video_title, comment)
        return {
            "Video Title": video_title,
            "Comment": comment.snippet.text_display,
        }

    async def _arun(
        self,
        query: Optional[str] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")
