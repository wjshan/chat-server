from datetime import datetime

from fastapi_socketio import SocketManager

from chat_server.db import get_db
from chat_server.serializers.message import MessageSaveModel
from chat_server.services import Message
import json


def register_socket(socket: SocketManager):
    @socket.on("send_message")
    async def send_message(sid, message: dict):
        msg = MessageSaveModel(**message, create_at=datetime.utcnow())
        res = await Message.save_message(msg)
        # todo: 将消息存入MongoDB并发送出去
        await socket.emit("receive", json.loads(res.json()))
        return message
