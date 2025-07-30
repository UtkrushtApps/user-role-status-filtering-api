from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
from app.models.user import UserResponse

async def get_users_by_filters(db: AsyncSession, role: Optional[str], status: Optional[str]) -> List[UserResponse]:
    pass