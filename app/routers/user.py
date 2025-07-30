from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.models.user import UserResponse
from app.services.user_service import get_users_by_filters
from app.db.session import get_db_session

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserResponse])
async def list_users(
    role: Optional[str] = None,
    status: Optional[str] = None,
    db: AsyncSession = Depends(get_db_session),
):
    pass