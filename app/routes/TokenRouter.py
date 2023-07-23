from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.tokenSchema import Token
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.UserService import UserService
from typing import Annotated
from app.auth.auth import Auth



router = APIRouter(prefix="/token", tags=['token'])

@router.post("/")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = await Auth.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="invalid credentials")
    return await Auth.create_token(user=user)



