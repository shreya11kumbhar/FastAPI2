from  fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, models, database, hashing
from .. import JWTtoken
from sqlalchemy.orm import session

router = APIRouter(
    tags=["Authentication"]
)

getdb = database.getdb

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(), db: session = Depends(getdb)):
    log_details = db.query(models.User).filter(models.User.email == request.username).first()
    if not log_details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Invalid Username")
    
    if not hashing.verify(log_details.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Invalid Password")
    
    access_token = JWTtoken.create_access_token(data={"sub": log_details.email})
    return {"access_token": access_token, "token_type": "bearer"}
     




