import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from network.clients.html_client import html
from app.games.chicken import ch

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Преобразовать строку в словарь
            res_data = json.loads(data)
            all_desk = ch.step(res_data)
            # Преобразовать словарь с строку
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"{all_desk}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{all_desk}")

# if __name__ == "__main__":
#     uvicorn.run("network.server.main_server:app", host="127.0.0.1", port=8080, log_level="info")

#{'deck': 'open', 'card': '9 s'}
#ws.sand(JSON.stringify({player:player, cell:id}))