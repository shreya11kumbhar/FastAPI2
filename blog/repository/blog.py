from turtle import title
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.orm import session

def create(request: schemas.Blog, db:session):
    new_blog = models.Blog(title = request.title, user_id = request.user_id,
                           body = request.body)
    check_user= db.query(models.User).filter(models.User.id == request.user_id).first()
    if not check_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You are not Existing user")
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    print(new_blog)
    return new_blog     
    

def getall(db: session):
    all_blogs = db.query(models.Blog).all()
    return all_blogs

def get_blog_by_id(id, db: session):
    get_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not get_blog:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"details" : f"The blog with id {id} is not available"} 
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"The blog with id {id} is not available")
    else:
        return  get_blog
    
def update_by_id(db:session, request: schemas.BaseBlog):
    update_blog=db.query(models.Blog).filter(models.Blog.id == request.blog_id) 
    if not update_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"The blog with id {id} is not available")
    update_blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return update_blog.first()

def Delete(id, db:session, request: schemas.Blog):
    delete_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not delete_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog with {id} does not exist")
    delete_blog.delete(synchronize_session=False)
    db.commit()
    return "Deleted successfully"