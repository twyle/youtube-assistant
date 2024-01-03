from youtube.models import CommentThread, Comment
from typing import Optional
from youtube.schemas import (
    CommentThreadPart, CommentThreadOptionalParameters, CommentThreadFilter, 
    YouTubeRequest
)
from ..video.helpers import get_video_id
from collections.abc import Iterator
from ...extensions import youtube_client


def list_video_comments(video_title: str, max_results: Optional[int] = 30) -> list[Comment]:
    """List a given videos comments"""
    video_id: str = get_video_id(video_title)
    part: CommentThreadPart = CommentThreadPart()
    filter: CommentThreadFilter = CommentThreadFilter(
        videoId=video_id
    )
    optional: CommentThreadOptionalParameters = CommentThreadOptionalParameters(
        maxResults=min(max_results, 30)
    )
    request:YouTubeRequest = YouTubeRequest(
        part=part,
        filter=filter,
        optional_parameters=optional
    )
    comment_iterator: Iterator = youtube_client.get_comments_iterator(request)
    video_comments: list[Comment] = list()
    done: bool = False
    comment_count: int = 0
    for comment_threads in comment_iterator:
        if done:
            break
        for comment_thread in comment_threads:
            comment: Comment = comment_thread.snippet.top_level_comment
            video_comments.append(comment)
            comment_count += 1
            if comment_count > min(max_results, 30):
                done = True
                break
    return video_comments

def list_comment_replies(comment_author: str) -> list[Comment]:
    """List all the replies to a given comment by the given author"""
    pass

def get_author_comments(comment_author: str, video_title: str) -> list[Comment]:
    """List all the comments by the given author on the given video."""
    pass

def comment_on_video(video_title: str, comment: str) -> Comment:
    """Comment on a video."""
    video_id: str = get_video_id(video_title)
    comment: Comment = youtube_client.insert_comment(video_id, comment)
    return comment