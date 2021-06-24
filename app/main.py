from fastapi import FastAPI
from .routers import users, items
from . import models, schemas
from .database import SessionLocal, engine

# Create tables
try:
    models.Base.metadata.create_all(bind=engine)
except:
    pass

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}
    