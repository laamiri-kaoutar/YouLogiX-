from loguru import logger
from app.repositories.user_repository import UserRepository
from app.core.security import verify_password, create_access_token
from app.schemas.auth_schemas import Token, LoginRequest

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def authenticate_user(self, login_data: LoginRequest) -> Token | None:
        logger.info(f"Login attempt for user: {login_data.email}")

        user = self.user_repo.get_by_email(login_data.email)
        
        if not user or not verify_password(login_data.password, user.hashed_password):
            logger.warning(f"Authentication failed for {login_data.email}")
            return None
        
        access_token = create_access_token(
            data={"sub": str(user.id), "role": user.role}
        )
        
        logger.success(f"Token generated successfully for user {login_data.email}")

        return Token(
            access_token=access_token,
            token_type="bearer",
            role=user.role 
        )