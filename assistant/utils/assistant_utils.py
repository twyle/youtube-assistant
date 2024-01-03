welcome_text: str = """
Good morning Lyle. I am Oryks, your youtube assistant. My main task is to help you perform 
different tasks on youtube. These include:
- Searching for the latest videos for your favorite channels and adding them to the Daily Videos playlist
- Creating playlists and adding videos to those playlists.
- Summarizing news from your favorite news channels
- Helping you find videos, playlists and channels
- Helping you comment on videos and answer comments as well as find and analyze comments for various videos and channels.
- Helping you find live events both upcoming and those that already happened.
- Helping you upload videos to your youtube channel as well as update your video and channel details.
"""

def welcome_user(user_name: str = 'Lyle') -> str:
    """Welcome the user to the application."""
    return welcome_text