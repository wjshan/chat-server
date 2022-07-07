from typing import List

from fastapi import APIRouter, Body

from chat_server.serializers.message import ChatGroupWithMessage, CompleteMessage, ChatPreLoadBody
from chat_server.services import Group, Message

router = APIRouter(prefix="/chat")


@router.get("/message_list")
async def message_list() -> List[ChatGroupWithMessage]:
    result = []
    async for group in Group.list_group():
        result.append(ChatGroupWithMessage(group=group, messages=await Message.get_group_message(group.group_id)))
    return result


@router.post("/sub_page_load")
async def sub_page_load(info: ChatPreLoadBody = Body()) -> List[CompleteMessage]:
    return await Message.get_before_message(info.group_id, info.first_message_id)
