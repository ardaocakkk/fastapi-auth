from typing import Any
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True)
    hashed_password = Column(String(120))
    
    
    def verify_password(self, password):
        return pwd_context.verify(password, self.hashed_password)
    

        
    
    
    
    