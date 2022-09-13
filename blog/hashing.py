from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def bcrypt(password):
    return pwd_context.hash(password)

def verify(hashed_pass, plain_pass):
    return pwd_context.verify(plain_pass, hashed_pass)