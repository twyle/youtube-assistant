from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from youtube.models import Search
from .helpers import advanced_video_search



class YouTubeSearchVideo(BaseModel):
    query: str = Field(description='What to search for')
    channel_id: Optional[str] = Field(description='The channel id')
    max_results: Optional[int] = Field(description='The number of videos to search for', default=10)
    order: Optional[str] = Field(description='How to order the search results')
    published_after: Optional[str] = Field(description='')
    published_before: Optional[str] = Field(description='')
    region_code: Optional[str] = Field(description='The region code')
    relevance_language: Optional[str] = Field(description='The language code to use', default='en')
    video_caption: Optional[str] = Field(description='')
    video_category_id: Optional[str] = Field(description='')
    video_definition: Optional[str] = Field(description='')
    video_dimension: Optional[str] = Field(description='')
    video_duration: Optional[str] = Field(description='')
    video_paid_product_placement: Optional[str] = Field(description='')
    video_syndicated: Optional[str] = Field(description='')
    video_type: Optional[str] = Field(description='', default='any')


class YouTubeSearchVideoTool(StructuredTool):
    name = "youtube_search_video"
    description = """
    Useful when you need to search youtube for videos.
    """
    args_schema: Type[BaseModel] = YouTubeSearchVideo
    
    def _parse_search(self, search: Search) -> dict:
        return {
            'title': search.title,
            'description': search.description,
            'url': f'https://www.youtube.com/watch?v={search.resource_id}'
        }

    def _run(
        self, 
        query: str,
        channel_id: Optional[str] = None,
        max_results: Optional[int] = 10,
        order: Optional[str] = None,
        published_after: Optional[str] = None,
        published_before: Optional[str] = None,
        region_code: Optional[str] = None,
        relevance_language: Optional[str] = 'en',
        video_caption: Optional[str] = None,
        video_category_id: Optional[str] = None,
        video_definition: Optional[str] = None,
        video_dimension: Optional[str] = None,
        video_duration: Optional[str] = None,
        video_paid_product_placement: Optional[str] = None,
        video_syndicated: Optional[str] = None,
        video_type: Optional[str] = 'any',
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        search_results: list[Search] = advanced_video_search(
            query=query,
            channel_id=channel_id,
            max_results=max_results
        )
        search_results: list[dict] = [self._parse_search(search) for search in search_results]
        return search_results

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("YouTubeVideoSearchTool does not support async")