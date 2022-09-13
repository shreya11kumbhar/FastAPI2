from fastapi import APIRouter, status, HTTPException, Depends
from .. import models, schemas, database
from sqlalchemy.orm import session
from  ..hashing import bcrypt
from ..repository import user

router = APIRouter(
    prefix="/users",
    tags=["User"]
)

getdb = database.getdb

@router.post("/",response_model=schemas.ShowBaseUser, status_code=status.HTTP_201_CREATED, tags=["User"])
def Create_user(request: schemas.User, db : session=Depends(getdb)):
    return user.create(db, request)
     
     

@router.get("/{id}",status_code=200, response_model=schemas.ShowUser, tags=["User"])
def get_user_by_id(id:int, db : session=Depends(getdb)):
    get_by_id = db.query(models.User).filter(models.User.id == id).first()
    if not get_by_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"The User with id {id} not available")
    else:
        return get_by_id