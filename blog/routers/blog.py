from urllib import request
from fastapi import APIRouter, status, Depends, Response, HTTPException
from typing import List
from .. import schemas, models, database, oauth2
 
from sqlalchemy.orm import session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)
getdb = database.getdb

@router.post("/",status_code=status.HTTP_201_CREATED, tags=["Blog"])
def create_blogs(request : schemas.Blog, 
                 db : session=Depends(getdb), get_current_user : schemas.User = Depends(oauth2.get_current_user)):

    new_blog = models.Blog(title = request.title, user_id = request.user_id,
                           body = request.body)
    check_user= db.query(models.User).filter(models.User.id == request.user_id).first()
    print(request.user_id)
    print(check_user)
    if not check_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You are not Existing user")
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    print(new_blog)
    return new_blog     
     

@router.get("/", response_model=List[schemas.Blogout], tags=["Blog"])
def get_all_blogs(db : session=Depends(getdb), get_current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.getall(db)



@router.get("/{id}",status_code=200, response_model= schemas.Blogout, tags=["Blog"])
def get_blog_by_id(id, response:Response,
                   db: session= Depends(getdb), get_current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blog_by_id(id, db)


@router.put("/", tags=["Blog"])
def update_blog_by_id(request: schemas.BaseBlog,
                      db:session=Depends(getdb), get_current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_by_id(db, request)
     

@router.delete("/{id}",status_code=200, tags=["Blog"])
def delete_blog_by_id(id, db : session=Depends(getdb), get_current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.Delete(id, db, request)
     
     

