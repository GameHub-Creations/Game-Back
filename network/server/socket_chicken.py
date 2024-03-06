from network.server.main_server import websocket_endpoint, app
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from network.clients.html_client import html



def x():
    return '123'

async def websocket():
    await websocket_endpoint(play='123')


    # import json
    # string = '{"bird1": "Pigeon", "bird2": "Peacock", "bird3": "Eagle", "bird4": "Dove"}'
    # # Вывести строку
    # print("String is ", string)
    # # Преобразовать строку в словарь при помощи json.loads()
    # res_dict = json.loads(string)
    # print(type(res_dict))

    if __name__ == "__main__":
        uvicorn.run("network.server.socket_chicken:app", host="127.0.0.1", port=8080, log_level="info")
