import chainlit as cl
from assistant.utils.assistant_utils import welcome_user
from assistant.utils.playlist_utils import add_channel_to_favorites
from assistant.utils.channel_utils import get_favorite_channels_latest_videos
from assistant.agent import get_agent_executor


@cl.on_chat_start
async def start():
    msg = cl.Message(content="")
    await msg.send()
    msg.content = welcome_user()
    await msg.update()
    # msg = cl.Message(content="")
    # await msg.send()
    # msg.content = get_favorite_channels_latest_videos()
    # await msg.update()
    # msg = cl.Message(content="")
    # await msg.send()
    # msg.content = add_channel_to_favorites()
    # await msg.update()
        

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()
    query: str = message.content
    agent_executor = get_agent_executor(query)
    msg.content = agent_executor.invoke({"input": query})['output']
    await msg.update()