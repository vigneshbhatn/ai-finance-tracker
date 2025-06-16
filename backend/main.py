from fastapi import FastAPI, APIRouter
from app.routers import expense_route
from app.routers import budget_route
from app.routers import earning_route
from app.routers import user_route
from app.routers import auth_route
app = FastAPI()

app.include_router(expense_route.router)
app.include_router(budget_route.router)
app.include_router(earning_route.router)
app.include_router(user_route.router)
app.include_router(auth_route.router)

@app.get("/")
def read_root():
    return {"status":"Server is Running"}