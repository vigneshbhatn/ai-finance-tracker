from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.models.earning_model import Earning
from app.models.user_model import User
from app.schema.earning_schema import EarningCreate
from app.schema.earning_schema import EarningResponse
from app.util.config import get_db
from app.util.security import get_current_user

router = APIRouter()

@router.post("/earnings/")
def create_earning(earning: EarningCreate, db: Session = Depends(get_db),user: User = Depends(get_current_user)):
    db_earning = Earning(
        amount=earning.amount,
        source=earning.source,
        date=earning.date,
        user_id = user.id
    )
    db.add(db_earning)
    db.commit()
    db.refresh(db_earning)
    return db_earning

@router.get("/earnings/", response_model=list[EarningResponse])
def get_earnings(db: Session = Depends(get_db),user: User = Depends(get_current_user)):
    return db.query(Earning).filter(Earning.user_id == user.id).all()

@router.put("/earnings/{earning_id}", response_model=EarningResponse)
def update_earning(earning_id: int, updated: EarningCreate, db: Session = Depends(get_db),user: User = Depends(get_current_user)):
    db_earning = db.query(Earning).filter(Earning.user_id == user.id,earning_id == Earning.id).first()
    if not db_earning:
        raise HTTPException(status_code=404, detail="Earning not found")

    db_earning.amount = updated.amount
    db_earning.source = updated.source
    db_earning.date = updated.date

    db.commit()
    db.refresh(db_earning)
    return db_earning

@router.delete("/earnings/{earning_id}",response_model=EarningResponse)
def delete_earning(earning_id: int,db: Session = Depends(get_db),user: User = Depends(get_current_user)):
    earning = db.query(Earning).filter(Earning.user_id == user.id,earning_id==Earning.id).first()
    if earning is None:
        raise HTTPException(status_code=404, detail="Earning not found")
    db.delete(earning)
    db.commit()
    return JSONResponse(content={"message": "Earning deleted"})