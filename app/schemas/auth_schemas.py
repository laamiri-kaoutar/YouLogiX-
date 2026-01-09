# app/schemas/auth_schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional

# 1. Login Request Schema
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# 2. Token Response Schema (What sends back to user)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str

# 3. Token Data Schema (Internal use for decoding)
class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None