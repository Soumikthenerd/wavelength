from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError, ExpiredSignatureError
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException,status, Depends
from . import database, models
from sqlalchemy.orm import Session

# In production, keep this secret and load from environment variables
SECRET_KEY = "<YOUR SUPER SECRET KEY>"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

check_authorization_header = OAuth2PasswordBearer(tokenUrl = "login")

def create_access_token(data):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithms=ALGORITHM)
    return encoded_jwt

def validate_access_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm = [ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                       detail = " THIS NIGGA DOESNT EVEN EXIST -_- ",
                                       headers = {"WWW-Authenticate": "Bearer"},
                                       )
        return user_id
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                       detail = " time's up! now reverify broda ",
                                       headers = {"WWW-Authenticate": "Bearer"},
                                       )
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                       detail = " O_O trying to hack in ?? who do you think you are f off this instant :( ",
                                       headers = {"WWW-Authenticate": "Bearer"},
                                       )
    
def get_current_user(token = Depends(check_authorization_header), db: Session = Depends(database.get_db)):
    user_id = validate_access_token(token)
    user = db.query(models.User).filter(models.User.id == int(user_id)).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                            detail = " THIS NIGGA DOESNT EVEN EXIST -_- ",
                                            headers = {"WWW-Authenticate": "Bearer"},
                                            )
    return user 