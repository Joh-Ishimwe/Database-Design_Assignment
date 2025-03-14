from fastapi import FastAPI
from app.routes.sql_crud import router as sql_router
from app.routes.nosql_crud import router as nosql_router

app = FastAPI()

app.include_router(sql_router, prefix="/sql", tags=["SQL CRUD"])
app.include_router(nosql_router, prefix="/nosql", tags=["NoSQL CRUD"])

@app.get("/")
def home():
    return {"message": "Hello, FastAPI is working!!!"}