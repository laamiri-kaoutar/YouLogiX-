from fastapi import APIRouter, HTTPException, status, Depends , Request
from app.services.auth_service import AuthService
from app.schemas.auth_schemas import LoginRequest, Token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse


router = APIRouter()

    
@router.post("/login", response_model=Token)
def login(login_data: LoginRequest):
    service = AuthService()
    # Attempt to authenticate
    token = service.authenticate_user(login_data)
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    
    return token

# ---  SPECIFICALLY for Swagger UI (Form Data) ---
@router.post("/login/access-token", response_model=Token)
def login_for_swagger(form_data: OAuth2PasswordRequestForm = Depends()):
  
    login_data = LoginRequest(email=form_data.username, password=form_data.password)
    
    service = AuthService()
    token = service.authenticate_user(login_data)
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    print(token)
    return token