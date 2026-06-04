from fastapi import APIRouter
from fastapi import Depends

from app.core.auth import (
    get_current_user_id
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
def get_me(
        user_id=Depends(
            get_current_user_id
        )
):

    return {
        "message":
        "Authenticated",

        "user_id":
        user_id
    }