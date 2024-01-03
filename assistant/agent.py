import os

from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools.render import format_tool_to_openai_function
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from .tools import YouTubeSearchVideoTool
from .tools.playlist import ListUserPlaylistsTool, ListPlaylistVideosTool
from .tools.comment import ListVideoCommentsTool
from .tools.video import YouTubeVideoDetailsTool
from .tools.channel import YouTubeChannelDetailsTool


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL")  # "gpt-3.5-turbo-0613"
llm = ChatOpenAI(
    temperature=0, 
    model=OPENAI_MODEL, 
    api_key=OPENAI_API_KEY)
tools = [
    YouTubeSearchVideoTool(),
    ListUserPlaylistsTool(),
    ListPlaylistVideosTool(),
    ListVideoCommentsTool(),
    YouTubeVideoDetailsTool(),
    YouTubeChannelDetailsTool()
]

def get_tools(query: str) -> str:
    """Get the agent tools."""
    pass

def get_agent_executor(query: str):
    """Get the agent"""
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a funny and friendly youtube assistant. Your task is to help the user with tasks related to youtube..",
            ),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    functions = [format_tool_to_openai_function(t) for t in tools]

    llm_with_tools = llm.bind(functions=functions)

    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            ),
        }
        | prompt
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor