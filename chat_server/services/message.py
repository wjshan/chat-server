from typing import AsyncIterator, List

from chat_server.db import get_db
from chat_server.serializers.message import MessageSaveModel, CompleteMessage, ChatGroup
from bson import ObjectId

class Message(object):

    @staticmethod
    async def save_message(message: MessageSaveModel) -> CompleteMessage:
        db = await get_db()
        collector = db[Group.get_group_name_by_id(message.group_id)]
        result = await collector.insert_one(message.dict())
        return CompleteMessage(**message.dict(), message_key=str(result.inserted_id))

    @staticmethod
    async def get_group_message(group_id: str) -> List[CompleteMessage]:
        db = await get_db()
        collector = db[Group.get_group_name_by_id(group_id)]
        result = []
        async for message in collector.find().sort([("_id", -1)]).limit(20):
            result.append(CompleteMessage(**message, message_key=str(message['_id'])))
        return result[::-1]

    @staticmethod
    async def get_before_message(group_id: str, last_message_id: str = None) -> List[CompleteMessage]:
        db = await get_db()
        collector = db[Group.get_group_name_by_id(group_id)]
        cursor = collector.find({'_id': {'$lt': ObjectId(last_message_id)}})
        result = []
        async for message in cursor.sort([("_id", -1)]).limit(20):
            result.append(CompleteMessage(**message, message_key=str(message['_id'])))
        return result[::-1]



class Group(object):

    @staticmethod
    def get_group_name_by_id(group_id: str):
        return f"group@{group_id}"

    @staticmethod
    async def add_group(name: str, group_id: str):
        db = await get_db()
        collector = db["groups"]
        await collector.insert_one({"name": name, "id": group_id})
        return {"name": name, "id": group_id}

    @staticmethod
    async def list_group() -> AsyncIterator[ChatGroup]:
        db = await get_db()
        collector = db["groups"]
        async for group in collector.find():
            yield ChatGroup(group_id=group['id'], group_name=group['name'])
