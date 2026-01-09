from app.models.user_models import User
from app.core.database import get_db

class UserRepository:
    def __init__(self):
        self.db_gen = get_db()
        self.db = next(self.db_gen)

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user_data: dict) -> User:
        db_user = User(**user_data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_by_id(self, id: int) -> User | None:
        return self.db.query(User).filter(User.id == id).first()