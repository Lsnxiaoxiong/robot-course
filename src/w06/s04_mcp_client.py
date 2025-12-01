import asyncio
import json
import os.path
from pathlib import Path
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from dotenv import load_dotenv

from src.w06.model import ModelEnum

load_dotenv()


class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.server_configs = None
        self.sessions_dic: dict[str, ClientSession] = {}
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.tools = []
        self.model = ModelEnum.QWEN_FLASH.value

        self.messages = [

            {
                "role": "system",
                "content": """
                Answer in Chinese, and be simple and short as possible. With no emojis and markdown format.
                """
            },
        ]

    async def connect_to_all_servers(self):
        self.server_configs = [
            {
                "timeout": 60,
                "type": "stdio",
                "command": "uv",
                "args": [
                    "--directory",
                    "D:/source/robot-course/src/w06",
                    "run",
                    "s04_mcp_demo01.py"
                ]
            },
            # {
            #
            #     "command": "uv",
            #     "args": [
            #         'run',
            #         '--active',
            #         "C:/major/projectcode/projectfile/pythonProject/mcp-server/.venv/Scripts/python.exe",
            #         "C:/major/projectcode/projectfile/pythonProject/mcp-server/server.py"
            #     ]
            # },
            # {
            #
            #     "command": "C:/major/projectcode/projectfile/pythonProject/mcp-server/.venv/Scripts/python.exe",
            #     "args": [
            #         # '--active',
            #         # ,
            #         "C:/major/projectcode/projectfile/pythonProject/mcp-server/server.py"
            #     ]
            # },
            # {
            #     "name": 'desktop-commander',
            #     "command": "npx",
            #     "args": [
            #         "-y",
            #         "@smithery/cli@latest",
            #         "run",
            #         "@wonderwhy-er/desktop-commander",
            #         "--key",
            #         "a3fdf915-3047-4071-a49e-2f0a3cdb91cd"
            #     ]
            # },
        ]

        for server in self.server_configs:
            await self.connect_to_server(server)
        # tasks = [self.connect_to_server(server) for server in self.server_configs]
        # res = asyncio.gather(*tasks)
        # tools.append(res)
        print(self.tools)

    def get_work_dir(self, args: list):
        work_dir = None
        for arg in args:
            if arg.endswith(".py"):
                work_dir = os.path.join(arg, os.path.pardir)
        return work_dir

    async def connect_to_server(self, server_config: dict):
        server_params = StdioServerParameters(
            command=server_config["command"],
            args=server_config["args"],
            env=None,
            cwd=self.get_work_dir(server_config["args"])
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await session.initialize()

        response = await session.list_tools()
        tools = response.tools

        for tool in tools:
            self.tools.append(tool)
            self.sessions_dic[tool.name] = session
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    async def process_query(self, query: str) -> str:
        self.messages.append({
            "role": "user",
            "content": query
        })
        available_tools = [{
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.inputSchema
            }
        } for tool in self.tools]

        print(available_tools)

        response = self.model.client.chat.completions.create(
            model=self.model.model_name,
            messages=self.messages,
            tools=available_tools,
            extra_body={"enable_thinking": False},
            parallel_tool_calls=True,
        )
        resp = response.choices[0]

        while True:
            if resp.finish_reason == 'stop':

                self.messages.append({
                    "role": "assistant",
                    "content": resp.message.content
                })
                break
            elif resp.finish_reason == 'tool_calls':
                tools_info = resp.message.model_dump()
                if 'reasoning_content' in tools_info:
                    tools_info.pop('reasoning_content')
                self.messages.append(tools_info)
                for tool in resp.message.tool_calls:
                    tool_name = tool.function.name
                    tool_args = json.loads(tool.function.arguments)
                    print("=" * 20)
                    print(f"正在调用工具 {tool_name}，参数为：{tool_args}")
                    result = await self.sessions_dic[tool_name].call_tool(tool_name, tool_args)

                    self.messages.append({
                        "role": "tool",
                        "content": result.content[0].text,
                        "tool_call_id": tool.id
                    })

            response = self.model.client.chat.completions.create(
                model=self.model.model_name,
                messages=self.messages,
                tools=available_tools,
                extra_body={"enable_thinking": False},
                parallel_tool_calls=True
            )
            resp = response.choices[0]
            print("=" * 20, f"调用结果：{resp}")

        res = resp.message.content
        return res

    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                query = input("\nQuery: ").strip()

                if query.lower() == 'quit':
                    break

                response = await (self.process_query(query))
                print(response)

            except Exception as e:
                print(f"\nError: {str(e)}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()


async def main():
    client = MCPClient()
    try:
        await client.connect_to_all_servers()
        await client.chat_loop()
    finally:
        await client.cleanup()


if __name__ == "__main__":
    import sys

    asyncio.run(main())
