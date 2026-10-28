from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/signup", status_code=status.HTTP_201_CREATED,response_model = schemas.SignupResponse)
def create_user(new_user: schemas.signup, db: Session = Depends(get_db)):
    
    if db.query(models.User).filter(models.User.username == new_user.username).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=" User already exitst")
    
    hashed_pwd = utils.hash(new_user.password)
    
    temp_dict = new_user.model_dump()
    temp_dict["hashed_password"] = hashed_pwd
    temp_dict.pop("password", None)
    new_user = models.User(**temp_dict) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user