import asyncio
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

stdio_server_params = StdioServerParameters(
    command= "python",
    args= ["C:/Users/spawande/Desktop/mcp-crash-course/servers/math_server.py"],
)

async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())
