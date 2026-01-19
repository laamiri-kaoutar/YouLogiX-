from fastapi import FastAPI, APIRouter, HTTPException, status, Depends, Request
from app.schemas.zone_schemas import ZoneCreate, ZoneUpdate, ZoneResponse, ZoneSearchName, ZoneSearchCodePastal
from app.controllers.ZoneController import ZoneController
from fastapi.responses import JSONResponse
from jose import JWTError, jwt

from app.api.deps import get_current_active_client, get_current_active_admin
from app.models.user_models import User
from app.core.config import settings

# Public routes that don't need authentication
PUBLIC_ROUTES = [
    "/",
    "/api/v1/users/login",
    "/api/v1/users/historique_Colis" , 
    "/register",
    "/docs",
    "/openapi.json",
    "/redoc",
    "/api/v1/auth/login", 
    "/api/v1/zones/all",  
    "/api/v1/users/register",
    "/api/v1/auth/login/access-token"
]


async def authentication_middleware(request: Request, call_next):
    # Skip authentication for public routes
    if request.url.path in PUBLIC_ROUTES:
        return await call_next(request)
    
    # Skip docs, openapi, and static files
    if (request.url.path.startswith("/docs") or 
        request.url.path.startswith("/redoc") or
        request.url.path.startswith("/static") or
        request.url.path.endswith("/openapi.json")):
        return await call_next(request)
    
    print(f"🔍 Checking auth for: {request.url.path}")
    
    # Get Authorization header
    auth_header = request.headers.get("Authorization")
    print(f"Auth header: {auth_header}")
    
    if not auth_header:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Missing Authorization header"},
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Check Bearer token format
    if not auth_header.startswith("Bearer "):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Invalid authorization header format. Use: Bearer <token>"},
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Extract token
    token = auth_header.split(" ")[1]
    
    try:
        # Decode token
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        
        # Extract user info
        user_id = payload.get("sub")
        role = payload.get("role")
        
        if user_id is None:
            raise JWTError("Invalid token payload - missing user ID")
        
        # Store user info in request state for use in endpoints
        request.state.user_id = user_id
        request.state.role = role
        
        print(f"✅ Authenticated: User ID {user_id} (Role: {role})")
        
    except jwt.ExpiredSignatureError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Token has expired"},
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    except JWTError as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": f"Invalid token: {str(e)}"},
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    except Exception as e:
        print(f"❌ Authentication error: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Authentication failed"},
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Continue to endpoint
    response = await call_next(request)
    return response