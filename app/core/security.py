import bcrypt, jwt, datetime
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from prisma.models import Creator

def verify_password(password:str, hashpass:str):
    is_valid = bcrypt.checkpw(password.encode(), hashpass.encode())
    return is_valid

def create_token(data:int):
    payload = {
        "iat":datetime.datetime.now(),
        "sub": str(data),
        "exp": datetime.datetime.now() + datetime.timedelta(hours=5)
    }

    token = jwt.encode(payload, key="$2b$12$ib08nfwfUXkJKgGfhWfR4ecZKlh8ScmXENDXHgfPCsJxHFJutSDXS", algorithm="HS256")

    return token

def decode_token(token):
    token_decoded = jwt.decode(token, key="$2b$12$ib08nfwfUXkJKgGfhWfR4ecZKlh8ScmXENDXHgfPCsJxHFJutSDXS", algorithms="HS256")
    return token_decoded.get("sub")

receive_token = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: Annotated[str, Depends(receive_token)]):
    try:
        decoded = int(decode_token(token))
    except:
        raise HTTPException(detail="Accès non autorisé", status_code=status.HTTP_401_UNAUTHORIZED)
    user = await Creator.prisma().find_unique(where={"id":decoded})
    return user
