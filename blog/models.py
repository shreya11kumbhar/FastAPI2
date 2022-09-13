import email
from turtle import color, title
from sqlalchemy import Column, String,Integer,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

 

class Blog(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("UsersData.id"))
    
    user = relationship("User", back_populates="blogs")
    
class User(Base):
    __tablename__ = "UsersData"
    id = Column(Integer, primary_key=True)
    #id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship("Blog", back_populates="user")
    