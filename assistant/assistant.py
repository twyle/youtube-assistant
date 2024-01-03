from utils import (
    get_channel_id, advanced_video_search, get_video_categories
)
from youtube.models import Search
from datetime import datetime

# Get favorite channels
# Find the latest video
# Add them to the playlist, first check if playlist exists
# Delete watched videos

channel_name: str = 'Ark Invest'
channel_id: str = 'UCK-zlnUfoDHzUwXcbddtnkg'
query: str = 'investing in blockchain'
max_results: int = 10
order: str = 'date'
january_2023 = datetime(year=2023, month=1, day=1)
january_2023 = str(january_2023.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

# search_results: list[Search] = advanced_video_search(
#     channel_id=channel_id,
#     query=query,
#     max_results=max_results,
#     published_after=january_2023,
#     order=order
# )
# print(search_results)
print(get_video_categories())