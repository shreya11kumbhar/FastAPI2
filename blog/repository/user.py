from .. import schemas, models
from sqlalchemy.orm import session
from  ..hashing import bcrypt


def create(db: session, request: schemas.User):
    new_user = models.User(name = request.name, email= request.email,
                           password=bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
    
    
    