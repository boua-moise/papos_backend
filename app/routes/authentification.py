from fastapi import APIRouter
from app.schemas.authentification import LoginSchema, ResponseLoginSchema
from app.services.authentification import AuthService
from fastapi import Depends
from app.core.security import get_current_user
from app.schemas.authentification import UserSchema

authentication = APIRouter(prefix="/auth", tags=["Authentication"])

@authentication.post("/login", response_model=ResponseLoginSchema)
async def login(user_info:LoginSchema):
    return await AuthService.login(user_info)

@authentication.get("/currentuser", response_model=UserSchema)
async def current_user(user = Depends(get_current_user)):
    return await AuthService.current_user(user)
