def welcome_user(user_name: str = "Lyle") -> str:
    """Welcome the user to the application."""
    welcome_text: str = f"""
    Hello {user_name}. I am Oryks, your youtube assistant. My main task is to help you perform 
    different tasks on youtube. These include:
    - Searching for the videos, playlists and channels that interest you.
    - Creating, updating and deleting playlists on your youtube channel.
    - Adding and removing videos to various playlists on your youtube channel.
    - Helping you get the details of youtube channels and videos such as when they were created, number of views and likes e.tc
    - Helping you comment on videos and answer comments as well as find and reply to comments.
    - Helping you find live events both upcoming and those that already happened.
    - Helping you upload videos to your youtube channel as well as update your videos and channel details.
    - Find your recent activities on youtube such as the videos you liked, channels you subscribed to, 
    videos you recently uploaded ...
    To get started, just ask me to perform any task...
    """
    return welcome_text
