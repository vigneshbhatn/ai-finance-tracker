from fastapi import FastAPI, APIRouter
from app.routers import expense_route

app = FastAPI()

app.include_router(expense_route.router)

@app.get("/")
def read_root():
    return {"status":"Server is Running"}