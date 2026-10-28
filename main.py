from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session   
from .routers import auth, user
from . import schemas, models, utils
from . database import get_db, engine
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def welcome_messages():
    return {"message": "Hello World"}







app.include_router(auth.router)
app.include_router(user.router)

