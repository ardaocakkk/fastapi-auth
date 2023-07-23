from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    username: str
    hashed_password: str
    

    
    