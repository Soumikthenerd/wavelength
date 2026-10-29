from pydantic import BaseModel, EmailStr


#first time signup / new registration
class signup(BaseModel):
    f_name: str
    l_name: str           | None = None
    age: int              | None = None
    gender: str           | None = None
    username: str 
    email : EmailStr
    password: str
    bio : str             | None = None
    location : str        | None = None
    instruments : list[str] = [] 
    class Config:
        from_attributes = True

class SignupResponse(BaseModel):
    f_name: str
    username: str
    class Config:
        from_attributes = True


#login
class login(BaseModel):
    username: str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str
    





