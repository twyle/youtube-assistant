from langchain.tools import BaseTool
from typing import Optional
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
) 
from youtube.models import Comment
from pydantic import BaseModel, Field
from .helpers import list_video_comments


class ListVideoComments(BaseModel):
    video_title: str = Field(description='The title for the youtube video.')
    max_results: Optional[int] = Field(description='Max search results to return.')


class ListVideoCommentsTool(BaseTool):
    name = "list_video_comments"
    description = """
    useful when you need to find all the comments for a given youtube video. You must 
    provide the video title.
    """
    
    def parse_comments(self, comments: list[Comment]) -> list[dict]:
        return [
            {
                'author': comment.snippet.author.display_name,
                'comment': comment.snippet.text_display
            }
            for comment in comments
        ]

    def _run(
        self, 
        video_title: str,
        max_results: Optional[int] = 50,
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        video_comments: list[dict] = list_video_comments(video_title, max_results)
        return self.parse_comments(video_comments)

    async def _arun(
        self, 
        query: Optional[str] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")