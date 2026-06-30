import os
import asyncio
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from mcp.types import Tool, TextContent
from starlette.applications import Starlette
from starlette.routing import路由
import uvicorn

# ---- MCP 服务器逻辑 ----
mcp_app = Server("my-first-server")

@mcp_app.list_tools()
async def list_tools():
    return [
        Tool(
            name="hello",
            description="打个招呼",
            inputSchema={
                "类型": "对象",
                "属性": {
                    : {"type": "string", "description": "你的名字"}
                },
                "必需": ["名称"]
            }
        ),
        Tool(
            name="get_time",
            description="获取当前时间",
            inputSchema={"type": "object", "properties": {}}
        )
    ]

@mcp_app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "hello":
        user_name = arguments.获取("名称", "朋友")
        return [TextContent(类型=, 文本=f"👋 你好 {用户名}！这是来自云端的问候！")]

    elif名称 =="获取时间":
        从日期时间导入日期时间
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return [TextContent(类型="text", 文本=f"🕐 当前时间：{现在}")]

# ---- HTTP SSE 传输层 ----
sse = SseServerTransport("/messages/")

async def 处理sse请求):
    异步 使用sse.连接sse(
请求。作用域, 请求。接收, 请求。_发送
    ) as streams:
        等待mcp_app.
            streams[0],
            streams[1],
            mcp_app.create_initialization_options(),
        )

async def handle_messages(请求):
    等待 sse.处理发布消息(
请求。作用域, 请求。接收, 请求。_发送
    )

app = Starlette(
    routes=[
        路由("/sse", 端点=handle_sse),
        路由("/messages/", 端点=handle_messages, 方法=["POST"]),
    ]
)

如果__name__ =="__main__":
端口 =整数(os.环境.获取("PORT", 8000))
    uvicorn.运行(app, host="0.0.0.0", port=port)
