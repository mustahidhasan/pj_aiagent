#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.controller.service import Controller

from browser_use_tools.mcp_manager import McpManager
from browser_use_tools.browser_use_tools import add_langchain_tools_to_controller

controller = Controller()

async def main():
    mcp_manager = McpManager()
    await mcp_manager.load()
    langchain_tools = mcp_manager.get_tools()
    add_langchain_tools_to_controller(langchain_tools, controller)

    agent = Agent(
        task="""
test.txtをtestという内容で作成してください
ディレクトリの作成は不要です
""",
        llm=ChatOpenAI(model="gpt-4o-mini"),
        controller=controller
    )
    result = await agent.run()
    print(result)

    mcp_manager.stop_servers()

if __name__ == '__main__':
    asyncio.run(main())