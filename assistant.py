import chainlit as cl
from assistant.utils.assistant_utils import welcome_user
from assistant.agent import get_agent_executor


@cl.on_chat_start
async def start():
    res = await cl.AskUserMessage(content="What is your name?", timeout=30).send()
    if res:
        msg = cl.Message(content="")
        await msg.send()
        msg.content = welcome_user(user_name=res['content'])
        await msg.update()
        

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()
    query: str = message.content
    agent_executor = get_agent_executor(query)
    msg.content = agent_executor.invoke({"input": query})['output']
    await msg.update()