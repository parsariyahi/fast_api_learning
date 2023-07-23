from sqlalchemy.orm import Session

from db.repository.user import  create_user
from schemas.user import User as UserSchema

def create_random_user(db: Session):
    user = UserSchema(
        email="test@example.com",
        password="test1234",
    )
    user = create_user(user, db)

    return user