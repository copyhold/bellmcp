import os
import platform
import asyncio
import sys
from mcp.server.fastmcp import FastMCP
# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def play_finish_bell():
    """Rings a bell when the task finished"""
    system = platform.system()
    if system == "Darwin":  # macOS
        os.system("afplay /Users/ilya/projects/bellmcp/complete.ogg")
    elif system == "Linux":
        os.system("paplay ./complete.ogg")
    else:
        print("\a", end="", flush=True)

@mcp.tool()
def play_waiting_bell():
    """Rings a bell when waiting for user input"""
    system = platform.system()
    if system == "Darwin":  # macOS
        os.system("afplay /Users/ilya/projects/bellmcp/wait-user.ogg")
    elif system == "Linux":
        os.system("paplay ./wait-user.ogg")
    else:
        print("\a", end="", flush=True)
