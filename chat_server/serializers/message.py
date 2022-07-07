import datetime
from typing import Optional, List

from pydantic import BaseModel


class SimpleMessage(BaseModel):
    message_content: Optional[str]
    user_name: str
    uid: str
    message_type: str
    image_url: Optional[str]
    group_id: str

class MessageSaveModel(SimpleMessage):
    create_at: datetime.datetime

class CompleteMessage(MessageSaveModel):
    message_key: str


class ChatGroup(BaseModel):
    group_id: str
    group_name: str


class ChatGroupWithMessage(BaseModel):
    group: ChatGroup
    messages: List[CompleteMessage]


class ChatPreLoadBody(BaseModel):
    group_id: str
    first_message_id: str
