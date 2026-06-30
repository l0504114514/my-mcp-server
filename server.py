import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

app = Server("my-first-server")

@app.list_tools()
async def list_tools():
    return [
        Tool(工具(
            name="hello",
            description="打个招呼",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "你的名字"}
                },
                "required": ["name"]
            }
        ),
        Tool(工具(
            name="get_time",
            description="获取当前时间",
            inputSchema={"type": "object", "properties": {}}
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "hello":
        user_name = arguments.get("name", "朋友")
        return [TextContent(type="text", text=f"👋 你好 {user_name}！这是来自云端的问候！")]
    
    elif name == "get_time":
        from datetime import datetime
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return [TextContent(type="text", text=f"🕐 当前时间：{now}")]

async def main():
    async with stdio_server() as (read, write):
        await app.run(read, write, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
