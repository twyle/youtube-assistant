from youtube.models import VideoCategory
from youtube.schemas import YouTubeListResponse

from ...extensions import youtube_client


def get_video_categories() -> str:
    """Get video categories."""
    response: YouTubeListResponse = youtube_client.get_video_categories()
    video_categories: list[VideoCategory] = response.items
    categories: list[dict[str, str]] = list()
    for category in video_categories:
        categories.append(
            {
                "title": category.snippet.title,
                "id": category.id,
                "assignable": category.snippet.assignable,
            }
        )
    return categories
