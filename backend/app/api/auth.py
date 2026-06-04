from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependency import get_db

from app.schemas.user import UserCreate

from app.models.user import User

from app.schemas.user import UserLogin
from app.core.security import (
    verify_password,
    create_access_token
)

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

@router.post("/login")
def login_user(
        user: UserLogin,
        db: Session = Depends(get_db)
):

    db_user = get_user_by_email(
        db,
        user.email
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
            user.password,
            db_user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {
            "sub": str(db_user.id)
        }
    )

    return {
        "access_token":
        access_token,

        "token_type":
        "bearer"
    }