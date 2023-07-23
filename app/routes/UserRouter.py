from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from app.auth.auth import Auth
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.userModel import User
from app.schemas.userSchema import UserSchema
from app.services.UserService import UserService



router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/')
async def getAllUsers(db: Session = Depends(get_db)):
    return await UserService.getAllUsers(db=db)

@router.get("/me")
async def get_user(user: UserSchema = Depends(Auth.get_current_user)):
    return user

@router.get('/{id}')
async def getUserByID(id: int ,db: Session = Depends(get_db)):
    return await UserService.getUserByID(id=id, db=db)



@router.get("/a/{name}")
async def get_user_by_name(name:str, db:Session = Depends(get_db)):
    
    print(name)
    return await UserService.get_user_by_name(username=name,db=db)

@router.post('/')
async def createUser(user: UserSchema,db: Session = Depends(get_db)):
    return await UserService.createUser(user=user, db=db)


@router.delete('/{id}')
async def deleteUserById(id : int , db: Session = Depends(get_db)):
    return UserService.deleteUserByID(id=id, db=db)


    
    



# @router.put('/{id}')
# async def updateUser(id:int, user: UserSchema, db: Session = Depends(get_db)):
#     return await UserService.updateUser(id=id, user=user, db=db)