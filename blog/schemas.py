from pydantic import BaseModel
from typing import List

#blog details
class BaseBlog(BaseModel):
    title : str
    body : str
    blog_id: int
 
class Blog(BaseModel):
    title : str
    body  : str
    user_id : int
    class Config():
        orm_mode = True
            
#User login
class User(BaseModel):
    name : str
    email : str
    password : str
    
class ShowBaseUser(BaseModel):
    name : str
    email : str
    class Config():
        orm_mode = True
        
class ShowUser(ShowBaseUser):
    name : str
    email : str
    blogs : List[Blog] = []
    class Config():
        orm_mode = True      
        
class Blogout(BaseModel):
    title: str
    body : str
    id : int
    user : ShowBaseUser
    
    class Config():
        orm_mode = True   
    
class Login(BaseModel):
    username : str
    password : str  

    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None