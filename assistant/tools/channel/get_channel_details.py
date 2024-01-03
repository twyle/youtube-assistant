from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from youtube.models import Channel
from .helpers import get_channel_details



class YouTubeChannelDetails(BaseModel):
    channel_title: str = Field(description='The channel title.')


class YouTubeChannelDetailsTool(BaseTool):
    name = "youtube_channel_details"
    description = """
    useful when you need to find out all the details about a youtube channel. This includes 
    the description, title, number of subscribers, number of playlists, the number of videos,
     when the channel was created or updated.
    """
    args_schema: Type[BaseModel] = YouTubeChannelDetails

    def _run(
        self, 
        channel_title: str, 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        channel: Channel = get_channel_details(channel_title)
        return {
            'id': channel.id,
            'title': channel.snippet.title,
            'description': channel.snippet.description,
            'subscribers_count': channel.statistics.subscribers_count,
            'videos_count': channel.statistics.videos_count,
            'date_created': channel.snippet.published_at,
            'views_count': channel.statistics.views_count,
        }

    async def _arun(
        self, 
        title: str, 
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError()