from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ChatMessageBase(BaseModel):
    role: str
    content: str

class ChatMessageCreate(ChatMessageBase):
    pass

class ChatMessage(ChatMessageBase):
    id: int
    session_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ChatSessionBase(BaseModel):
    title: str

class ChatSessionCreate(ChatSessionBase):
    pass

class ChatSession(ChatSessionBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime]
    messages: List[ChatMessage] = []

    class Config:
        from_attributes = True

class ChatResponse(BaseModel):
    message: str
    session_id: int

class EFTStatement(BaseModel):
    statement: str

class ReminderPhrase(BaseModel):
    phrase: str 