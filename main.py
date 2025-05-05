from fastapi import FastAPI, APIRouter
from app.routers import expense_route
from app.routers import budget_route
from app.routers import earning_route
app = FastAPI()

app.include_router(expense_route.router)
app.include_router(budget_route.router)
app.include_router(earning_route.router)


@app.get("/")
def read_root():
    return {"status":"Server is Running"}