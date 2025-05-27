        import asyncio
        import websockets

        async def send():
            uri = "ws://localhost:8000/ws"
            async with websockets.connect(uri) as websocket:
                await websocket.send(json.dumps(formatted))
                reply = await websocket.recv()
                print("[WS REPLY]", reply)

        asyncio.run(send())
