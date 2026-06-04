from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependency import get_db

from app.schemas.user import UserCreate

from app.models.user import User

from app.services.user_service import (
    get_user_by_email,
    create_user
)

from app.core.security import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register_user(
        user: UserCreate,
        db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(
        db,
        user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(
            user.password
        )
    )

    create_user(db, new_user)

    return {
        "message":
        "User registered successfully"
    }