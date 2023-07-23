from fastapi import FastAPI
from app.routes import UserRouter, TokenRouter
from app.config.database import create_engine, Base

app = FastAPI()

Base.metadata.create_all(bind=create_engine)

@app.get("/")
def hello():
    return {"message": "Hello World"}

app.include_router(UserRouter.router)
app.include_router(TokenRouter.router)