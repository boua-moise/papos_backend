from pydantic import BaseModel

class ResponseLoginSchema(BaseModel):
    token: str

class LoginSchema(BaseModel):
    mail: str
    password: str

class UserSchema(BaseModel):
    id: int
    name: str
    firstname:str
    mail:str
