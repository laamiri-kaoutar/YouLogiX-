from loguru import logger  # <--- Import Loguru
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate
from app.core.security import get_password_hash 

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, user_data: UserCreate):
        logger.info(f"Attempting to create new user: {user_data.email}") # <--- Log entry

        # Check if email already exists
        if self.repo.get_by_email(user_data.email):
            logger.warning(f"Registration failed: Email {user_data.email} already exists") # <--- Log rejection
            return None 

        # HASH THE PASSWORD
        hashed_pwd = get_password_hash(user_data.password)

        data_dict = user_data.model_dump()
        del data_dict['password'] 
        data_dict['hashed_password'] = hashed_pwd

        # Save
        new_user = self.repo.create(data_dict)
        
        # Log success with the new ID
        logger.success(f"User created successfully with ID: {new_user.id}") # <--- Log success
        return new_user

    def get_user_by_id(self, id: int):
        logger.debug(f"Fetching user profile for ID: {id}") # <--- Log internal detail
        
        user = self.repo.get_by_id(id)
        
        if not user:
             logger.warning(f"User lookup failed: ID {id} not found")
             
        return user