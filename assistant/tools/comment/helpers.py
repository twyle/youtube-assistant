from collections.abc import Iterator
from typing import Optional

from youtube.models import Comment
from youtube.schemas import (
    CommentThreadFilter,
    CommentThreadOptionalParameters,
    CommentThreadPart,
    YouTubeRequest,
)

from ...extensions import youtube_client
from ..channel.helpers import find_my_youtube_username
from ..video.helpers import get_video_id


def list_video_comments(
    video_title: str, max_results: Optional[int] = 30
) -> list[Comment]:
    """List a given videos comments"""
    video_id: str = get_video_id(video_title)
    part: CommentThreadPart = CommentThreadPart()
    filter: CommentThreadFilter = CommentThreadFilter(videoId=video_id)
    optional: CommentThreadOptionalParameters = CommentThreadOptionalParameters(
        maxResults=min(max_results, 30)
    )
    request: YouTubeRequest = YouTubeRequest(
        part=part, filter=filter, optional_parameters=optional
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


def list_comment_replies(comment_author: str, video_title: str) -> list[Comment]:
    """List all the replies to a given comment by the given author"""
    comment_author = "@" + comment_author
    comment_ids: list[str] = list()
    video_id: str = get_video_id(video_title)
    part: CommentThreadPart = CommentThreadPart()
    filter: CommentThreadFilter = CommentThreadFilter(videoId=video_id)
    optional: CommentThreadOptionalParameters = CommentThreadOptionalParameters(
        maxResults=30
    )
    request: YouTubeRequest = YouTubeRequest(
        part=part, filter=filter, optional_parameters=optional
    )
    comment_iterator: Iterator = youtube_client.get_comments_iterator(request)
    video_comments: list[Comment] = list()
    for comment_threads in comment_iterator:
        for comment_thread in comment_threads:
            comment: Comment = comment_thread.snippet.top_level_comment
            if comment.snippet.author.display_name.lower() == comment_author.lower():
                comment_ids.append(comment.id)
    for comment_id in comment_ids:
        video_comments.append(youtube_client.get_comment_replies(comment_id).items[0])
    return video_comments


def comment_on_video(video_title: str, comment: str) -> Comment:
    """Comment on a video."""
    video_id: str = get_video_id(video_title)
    comment: Comment = youtube_client.insert_comment(video_id, comment)
    return comment


def reply_to_comment(comment_author: str, video_title: str, comment: str) -> Comment:
    """Reply to a comment by a given author."""
    comment_author = "@" + comment_author
    comment_id: str = None
    video_id: str = get_video_id(video_title)
    part: CommentThreadPart = CommentThreadPart()
    filter: CommentThreadFilter = CommentThreadFilter(videoId=video_id)
    optional: CommentThreadOptionalParameters = CommentThreadOptionalParameters(
        maxResults=30
    )
    request: YouTubeRequest = YouTubeRequest(
        part=part, filter=filter, optional_parameters=optional
    )
    comment_iterator: Iterator = youtube_client.get_comments_iterator(request)
    for comment_threads in comment_iterator:
        for comment_thread in comment_threads:
            comment: Comment = comment_thread.snippet.top_level_comment
            if comment.snippet.author.display_name.lower() == comment_author.lower():
                comment_id = comment.id
    comment_reply: Comment = youtube_client.reply_to_comment(comment_id, comment)
    return comment_reply


def find_my_comments(video_title: str) -> list[Comment]:
    """Find the authenticated users commenst."""
    my_user_name: str = find_my_youtube_username()
    video_id: str = get_video_id(video_title)
    part: CommentThreadPart = CommentThreadPart()
    filter: CommentThreadFilter = CommentThreadFilter(videoId=video_id)
    optional: CommentThreadOptionalParameters = CommentThreadOptionalParameters(
        maxResults=30
    )
    request: YouTubeRequest = YouTubeRequest(
        part=part, filter=filter, optional_parameters=optional
    )
    comment_iterator: Iterator = youtube_client.get_comments_iterator(request)
    video_comments: list[Comment] = list()
    for comment_threads in comment_iterator:
        for comment_thread in comment_threads:
            comment: Comment = comment_thread.snippet.top_level_comment
            if comment.snippet.author.display_name == my_user_name:
                video_comments.append(comment)
    return video_comments


def find_author_comments(video_title: str, author_name: str) -> list[Comment]:
    """Find the authenticated users commenst."""
    author_name = "@" + author_name
    video_id: str = get_video_id(video_title)
    part: CommentThreadPart = CommentThreadPart()
    filter: CommentThreadFilter = CommentThreadFilter(videoId=video_id)
    optional: CommentThreadOptionalParameters = CommentThreadOptionalParameters(
        maxResults=30
    )
    request: YouTubeRequest = YouTubeRequest(
        part=part, filter=filter, optional_parameters=optional
    )
    comment_iterator: Iterator = youtube_client.get_comments_iterator(request)
    video_comments: list[Comment] = list()
    for comment_threads in comment_iterator:
        for comment_thread in comment_threads:
            comment: Comment = comment_thread.snippet.top_level_comment
            if comment.snippet.author.display_name.lower() == author_name.lower():
                video_comments.append(comment)
    return video_comments
