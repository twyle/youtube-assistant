from dotenv import load_dotenv
load_dotenv()
# from assistant.utils.channel_utils import get_channel_latest_video, get_favorite_channels_latest_videos
# from assistant.utils.playlist_utils import add_video_to_youtube_playlist
from assistant.agent import get_agent_executor
# from assistant.tools.playlist.helpers import list_playlist_videos
# from assistant.tools.comment.helpers import list_video_comments
from assistant.agent import get_tools
from assistant.tools.comment.helpers import (
    list_video_comments, find_my_comments, find_author_comments
)
from assistant.tools.channel.helpers import find_my_youtube_username

title: str = 'Real Engineering'
# print(get_favorite_channels_latest_videos())
# title: str = 'How Nebula Works from Real Engineering'
# playlist: str = 'Daily Videos'
# add_video_to_youtube_playlist(title, playlist)
# query = 'When was the youtube channel Ark Invest created?'
# print(agent_executor.invoke({"input": query})['output'])
# print(list_playlist_videos(title, title))
#PLx7ERghZ6LoOKkmL4oeLoqWousfkKpdM_
# print(list_video_comments('How Nebula Works', max_results=10))
# query = 'When was my youtube channel created?'
# agent_executor = get_agent_executor()
# print(agent_executor.invoke({"input": query})['output'])
# tools = get_tools(query)
# print(len(tools))
# t = [tool.description for tool in tools]
# print(t)
# print(find_author_comments('Trapping Rain Water - Google Interview Question - Leetcode 42', '@NeetCode'))

query = "Find neetcode comment for the video titled 'Trapping Rain Water - Google Interview Question - Leetcode 42'"
agent_executor = get_agent_executor()
print(agent_executor.invoke({"input": query})['output'])