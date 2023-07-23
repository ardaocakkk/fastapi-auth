from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from app.schemas.tokenSchema import Token, TokenData
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.services.UserService import UserService
from app.schemas.userSchema import UserSchema
from app.config.hashing import Hashing
from app.config.database import get_db
from app.models.userModel import User
SECRET_KEY = "32150f0e4083daddc03f6fbafe441a296790e0bc5c65b7d1324f55fa95412de6"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Auth():
    SECRET_KEY = "32150f0e4083daddc03f6fbafe441a296790e0bc5c65b7d1324f55fa95412de6"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    

    
    async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user = db.query(User).filter(User.username == payload.get("username")).first()
            print(user)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=401, detail="Error")
        return UserSchema.from_orm(user)
    

    
    async def authenticate_user(username: str, password: str, db:Session):
        user = await UserService.get_user_by_name(db=db, username=username)

        if not user:
            return False

        if not user.verify_password(password):
            return False

        return user


    async def create_token(user: User):
        user_obj = UserSchema.from_orm(user)
        token = jwt.encode(user_obj.dict(),SECRET_KEY)
        return dict(access_token=token,token_type="bearer")