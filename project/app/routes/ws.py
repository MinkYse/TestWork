from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..ws.ws_manager import WsManager

websockets_router = APIRouter()

manager = WsManager()


@websockets_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    id = 1
    try:
        while True:
            data = await websocket.receive_json()
            message = data['message']
            if message == '':
                continue
            await websocket.send_json({'message': message, 'id': id})
            id += 1
    except WebSocketDisconnect:
        manager.remove(websocket)