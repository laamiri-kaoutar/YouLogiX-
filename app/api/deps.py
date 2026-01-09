from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError

from app.core.config import settings
from app.schemas.auth_schemas import TokenData
from app.services.user_service import UserService
from app.models.user_models import User , Role
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login/access-token")

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    This function acts as a dependency. 
    It will be used in routes like: 
    def create_colis(user: User = Depends(get_current_user))
    """
    
    # Standard 401 Unauthorized Error to raise if anything goes wrong
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # 2. Decode the Token using the Secret Key
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        
        # 3. Extract the User ID (sub) from the token
        user_id: str = payload.get("sub")
        role: str = payload.get("role")
        
        if user_id is None:
            raise credentials_exception
            
        token_data = TokenData(email=user_id, role=role) # We store ID in the 'email' field of TokenData for now, or you can adjust Schema to use 'id'
        
    except (JWTError, ValidationError):
        raise credentials_exception

    # 4. Check if the User actually exists in the DB
    # (Maybe they were deleted after they got the token)
    user_service = UserService()
    user = user_service.get_user_by_id(int(user_id))
    
    if user is None:
        raise credentials_exception
        
    return user


def get_current_active_livreur(
    current_user: User = Depends(get_current_user)
) -> User:
    """Only allows LIVREURS or ADMINS to pass"""
    if current_user.role not in [Role.LIVREUR, Role.ADMIN]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions. You must be a Livreur."
        )
    return current_user

def get_current_active_admin(
    current_user: User = Depends(get_current_user)
) -> User:
    """Only allows ADMINS to pass"""
    if current_user.role != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions. Admin access required."
        )
    return current_user