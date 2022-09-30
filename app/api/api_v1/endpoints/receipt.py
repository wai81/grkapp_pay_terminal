from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import parse_obj_as
from sqlalchemy.orm import Session
from app import crud
from app.api.depend import get_db
from app.shemas.receipt import Receipt, ReceiptCreate, ReceiptCreateInDB, ReceiptUpdate

router = APIRouter()


@router.get("/", status_code=200, response_model=List[Receipt])
def receipts(
        *,
        db: Session = Depends(get_db),
) -> Any:
    """
    Cписок квитанций для оплаты
    """
    objects = crud.receipt.get_all(db=db)
    return objects


@router.get("/{receipt_id}", status_code=200, response_model=Receipt)
def get_receipt(
        *,
        receipt_id: UUID,
        db: Session = Depends(get_db),
) -> dict:
    """
    Квитанция для оплаты по id
    """
    obj = crud.receipt.get(db=db, id=receipt_id)
    return obj


@router.post("/", status_code=201, response_model=Receipt)
def create_receipt(
        *,
        receipt_in: ReceiptCreate,
        db: Session = Depends(get_db)
) -> dict:
    """
    Новая квитанция для оплаты
    """
    new_obj = crud.receipt.create(db=db, obj_in=receipt_in)
    return new_obj


@router.put("/{receipt_id}", status_code=201, response_model=Receipt)
def update_receipt(
        *,
        receipt_id: UUID,
        obj_in: ReceiptUpdate,
        db: Session = Depends(get_db)
) -> dict:
    """
    Изменить квитанцию для оплаты
    """
    receipt = crud.receipt.get(db=db, id=receipt_id)
    if not receipt:
        raise HTTPException(
            status_code=400, detail=f"Recipe with ID: {receipt_id} not found."
        )
    upd_obj = crud.receipt.update(db=db, db_obj=receipt, obj_in=obj_in)
    return upd_obj


@router.delete("/{receipt_id}", status_code=200)
def delete_receipt(
        *,
        receipt_id: UUID,
        db: Session = Depends(get_db)
):
    """
    Удалить квитанцию для оплаты
    """
    return crud.receipt.remove(db=db, id=receipt_id)




