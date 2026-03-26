from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    name:str
    email:EmailStr
    password:str
    role:str

class UserResponse(BaseModel):
    id:int
    name: str
    email: EmailStr
    password:str
    role:str

    class Config:
        from_attributes = True

        


