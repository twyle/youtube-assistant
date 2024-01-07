from youtube.models import Subscription


def list_my_subscriptions() -> list[Subscription]:
    """List all the channels that I subscribe to."""
    pass


def list_channel_subscriptions(channel_title: str) -> list[Subscription]:
    """List all the channels that this channel subscribes to."""
    pass


def do_i_subscribe(channel_id: str) -> bool:
    """Check if I subscribe to the given channel."""
    pass


def is_subscribed(channel_id: str, user_channel: str) -> bool:
    """Check if one channel subscribes to another channel."""
    pass


def subscribe_to_channel(channel_id: str) -> Subscription:
    """Subscribe to a youtube channel."""
    pass


def unsubscribe_from_channel(subscription_id: str) -> None:
    """Unsubscribe from a youtube channel."""
    pass
