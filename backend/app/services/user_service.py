from sqlalchemy.orm import Session

from app.models.user import User


def get_user_by_email(
        db: Session,
        email: str
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def create_user(
        db: Session,
        user_data
):
    db.add(user_data)
    db.commit()
    db.refresh(user_data)

    return user_data