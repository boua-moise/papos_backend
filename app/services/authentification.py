from prisma.models import Creator
from fastapi import HTTPException, status
from app.schemas.authentification import LoginSchema
from app.core.security import get_current_user, create_token, verify_password



class AuthService:
    @staticmethod
    async def login(user:LoginSchema):
        existe_user = await Creator.prisma().find_unique(where={"mail": user.mail})

        if not existe_user:
            raise HTTPException(detail="Informations incorrects", status_code=status.HTTP_403_FORBIDDEN)
        
        val = verify_password(user.password, existe_user.password)

        if not val:
            raise HTTPException(detail="Informations incorrects", status_code=status.HTTP_403_FORBIDDEN)
        
        token = create_token(existe_user.id)

        return {"token": token}
    
    async def current_user(user):
        return user