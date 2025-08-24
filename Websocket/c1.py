import asyncio, websockets

async def run():
    uri = "ws://127.0.0.1:8765"
    async with websockets.connect(uri) as ws:
        for m in ["hello", "websocket", "bye"]:
            await ws.send(m)
            reply = await ws.recv()
            print("server replied:", reply)

asyncio.run(run())
