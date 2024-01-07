from youtube.models import Activity


def list_channel_activities(self, channel_title: str) -> list[Activity]:
    """List all the activities of the given channel, such as uploads."""
    pass


def list_my_activities(self) -> list[Activity]:
    """List all the activities for your channel, such as creating a playlist."""
    pass
