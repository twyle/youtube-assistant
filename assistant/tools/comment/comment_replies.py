from typing import Optional, Type

from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from youtube.models import Comment

from .helpers import list_comment_replies


class ListVideoCommentReplies(BaseModel):
    video_title: str = Field(description="The title for the youtube video.")
    author_name: str = Field(description="The name of the author ")
    max_results: Optional[int] = Field(description="Max search results to return.")


class ListVideoCommentRepliesTool(BaseTool):
    name = "list_video_comment_replies"
    description = """
    useful when you need to find all the replies to a comment made by a particular user..
    """
    args_schema: Type[BaseModel] = ListVideoCommentReplies

    def parse_comments(self, comments: list[Comment]) -> list[dict]:
        return [
            {
                "author": comment.snippet.author.display_name,
                "comment": comment.snippet.text_display,
            }
            for comment in comments
        ]

    def _run(
        self,
        video_title: str,
        author_name: str,
        max_results: Optional[int] = 20,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        video_comments: list[dict] = list_comment_replies(author_name, video_title)
        return self.parse_comments(video_comments)

    async def _arun(
        self,
        query: Optional[str] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")
