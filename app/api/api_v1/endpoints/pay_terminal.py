from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.depend import get_db
from app.shemas.receipt import Receipt, ReceiptUpdateStatus, ReceiptInDB

router = APIRouter()


@router.get("/{number}", status_code=200, response_model=Receipt)
def get_receipt(
        *,
        number: int,
        db: Session = Depends(get_db),
) -> dict:
    """
    Квитанция для оплаты по номеру квитанции
    """
    if len(str(number)) != 16:
        raise HTTPException(
            status_code=400, detail=f"Invalid receipt number"
        )

    obj = crud.receipt.find_by_number(db=db, number=str(number))
    if not obj:
        raise HTTPException(
            status_code=400, detail=f"Recipe with number: {number} not found"
        )

    return obj


@router.put("/{number}", status_code=201, response_model=ReceiptInDB)
def change_status_receipt(
        *,
        number: int,
        obj_in: ReceiptUpdateStatus,
        db: Session = Depends(get_db)
) -> dict:
    """
    Изменить квитанцию для оплаты
    """
    if len(str(number)) != 16:
        raise HTTPException(
            status_code=400, detail=f"Invalid receipt number"
        )

    obj = crud.receipt.find_by_number(db=db, number=str(number))
    if not obj:
        raise HTTPException(
            status_code=400, detail=f"Recipe with number: {number} not found."
        )
    upd_obj = crud.receipt.update(db=db, db_obj=obj, obj_in=obj_in)
    return upd_obj
