from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags = ['Authentication'])

@router.post("/login",response_model = schemas.Token)
def login(user_credentials: schemas.login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Invalid Credentials")
    if not utils.verify(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Invalid Credentials")
    access_token = oauth2.create_access_token(data={"sub" : str(user.id)})
    return {"access_token" : access_token, "token_type": "bearer"}
    