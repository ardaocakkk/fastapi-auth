from fastapi import Depends, HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.config.database import Base, get_db
from app.models.userModel import User
from app.schemas.userSchema import UserSchema
from app.config.hashing import Hashing


class UserService():

    async def getAllUsers(db: Session):
        return  {"users": db.query(User).all()}

    async def get_user_by_name(username:str, db:Session):
        print(username)
        return db.query(User).filter(User.username == username).first()

    async def getUserByID(id:int,db: Session):
        return db.query(User).filter_by(id=id).first()
    

        

    async def createUser(user: UserSchema, db: Session = Depends(get_db)):
        newUser = User(
            username = user.username,
            hashed_password=Hashing.hash_password(user.hashed_password) 
        )
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
        return  newUser

    def deleteUserByID(id: int, db: Session = Depends(get_db)):
        theUser = db.query(User).filter_by(id=id).first()
        if theUser is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        db.delete(theUser)
        db.commit()
        return {"message": "user deleted successfully"}
        
    
    