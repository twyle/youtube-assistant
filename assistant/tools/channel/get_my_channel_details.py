from typing import Optional

from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools import BaseTool
from youtube.models import Channel

from .helpers import get_my_channel_details


class MyYouTubeChannelDetailsTool(BaseTool):
    name = "my_youtube_channel_details"
    description = """
    useful when you need to find out all the details about this users youtube channel channel. 
    For example 'Get the details for my youtube channel". Use this when the channel_title is not provided This includes 
    the description, title, number of subscribers, number of playlists, the number of videos,
     when the channel was created or updated.
    """

    def _run(
        self,
        query: Optional[str] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        channel: Channel = get_my_channel_details()
        return {
            "id": channel.id,
            "title": channel.snippet.title,
            "description": channel.snippet.description,
            "subscribers_count": channel.statistics.subscribers_count,
            "videos_count": channel.statistics.videos_count,
            "date_created": channel.snippet.published_at,
            "views_count": channel.statistics.views_count,
        }

    async def _arun(
        self, title: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError()
