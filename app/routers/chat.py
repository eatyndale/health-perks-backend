from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from models.user import User
from models.chat import ChatSession, ChatMessage
from schemas.chat import (
    ChatSession as ChatSessionSchema,
    ChatSessionCreate,
    ChatMessage as ChatMessageSchema,
    ChatResponse,
    EFTStatement,
    ReminderPhrase
)
from routers.auth import get_current_user

router = APIRouter()

@router.get("/history", response_model=List[ChatSessionSchema])
async def get_chat_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    sessions = db.query(ChatSession).filter(ChatSession.user_id == current_user.id).all()
    return sessions

@router.post("/sessions", response_model=ChatSessionSchema)
async def create_chat_session(
    session: ChatSessionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_session = ChatSession(
        title=session.title,
        user_id=current_user.id
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

@router.post("/respond", response_model=ChatResponse)
async def generate_response(
    message: str,
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verify session belongs to user
    session = db.query(ChatSession).filter(
        ChatSession.id == session_id,
        ChatSession.user_id == current_user.id
    ).first()
    if not session:
        raise HTTPException(status_code=404, detail="Chat session not found")

    # Save user message
    user_message = ChatMessage(
        session_id=session_id,
        role="user",
        content=message
    )
    db.add(user_message)

    # Generate AI response (placeholder - implement actual AI logic)
    ai_response = "This is a placeholder response. Implement actual AI logic here."
    
    # Save AI response
    assistant_message = ChatMessage(
        session_id=session_id,
        role="assistant",
        content=ai_response
    )
    db.add(assistant_message)
    db.commit()

    return ChatResponse(message=ai_response, session_id=session_id)

@router.post("/statements", response_model=EFTStatement)
async def generate_eft_statement(
    context: str,
    current_user: User = Depends(get_current_user)
):
    # Placeholder - implement actual EFT statement generation logic
    return EFTStatement(statement="This is a placeholder EFT statement.")

@router.post("/phrases", response_model=ReminderPhrase)
async def generate_reminder_phrase(
    context: str,
    current_user: User = Depends(get_current_user)
):
    # Placeholder - implement actual reminder phrase generation logic
    return ReminderPhrase(phrase="This is a placeholder reminder phrase.") 