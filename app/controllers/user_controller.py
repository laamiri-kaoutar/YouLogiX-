from app.services.user_service import UserService
from app.schemas.user_schemas import UserCreate

class UserController:
    def __init__(self):
        self.service = UserService()

    def create(self, user_data: UserCreate):
        # Returns User object or None (if email exists)
        return self.service.create_user(user_data)

    def get_by_id(self, id: int):
        return self.service.get_user_by_id(id)