import os

from langchain.agents import AgentExecutor, Tool
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.document import Document
from langchain.tools.render import format_tool_to_openai_function
from langchain.vectorstores.faiss import FAISS

from .tools import YouTubeSearchVideoTool
from .tools.channel import MyYouTubeChannelDetailsTool, YouTubeChannelDetailsTool
from .tools.comment import (
    FindMyCommentsTool,
    FindUserCommentsTool,
    ListVideoCommentRepliesTool,
    ListVideoCommentsTool,
    ReplyCommentTool,
)
from .tools.playlist import (
    CreatePlaylistTool,
    DeleteYoutubePlaylistsTool,
    InsertVideoIntoPlaylistTool,
    ListChannelPlaylistsTool,
    ListPlaylistVideosTool,
    ListUserPlaylistsTool,
)
from .tools.video import YouTubeVideoDetailsTool

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL")  # "gpt-3.5-turbo-0613"
llm = ChatOpenAI(temperature=0, model=OPENAI_MODEL, api_key=OPENAI_API_KEY)
tools = [
    YouTubeSearchVideoTool(),
    ListUserPlaylistsTool(),
    ListPlaylistVideosTool(),
    ListVideoCommentsTool(),
    YouTubeVideoDetailsTool(),
    YouTubeChannelDetailsTool(),
    DeleteYoutubePlaylistsTool(),
    InsertVideoIntoPlaylistTool(),
    CreatePlaylistTool(),
    ListChannelPlaylistsTool(),
    MyYouTubeChannelDetailsTool(),
    FindUserCommentsTool(),
    FindMyCommentsTool(),
    ListVideoCommentRepliesTool(),
    ReplyCommentTool(),
]


def get_tools(query: str, tools: list[Tool] = tools) -> str:
    """Get the agent tools."""
    documents: list[Document] = [
        Document(page_content=tool.description, metadata={"index": i})
        for i, tool in enumerate(tools)
    ]
    vectore_store = FAISS.from_documents(documents, OpenAIEmbeddings())
    retriver = vectore_store.as_retriever()
    retrieved = retriver.get_relevant_documents(query)
    return [tools[document.metadata["index"]] for document in retrieved]


def get_agent_executor():
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
