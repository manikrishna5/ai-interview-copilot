from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer

from app.core.security import (
    verify_access_token
)

security = HTTPBearer()


def get_current_user_id(
        credentials=Depends(security)
):

    token = credentials.credentials

    user_id = verify_access_token(
        token
    )

    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return user_id