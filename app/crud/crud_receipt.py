import datetime
from typing import List, Union, Dict, Any
from uuid import UUID

from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.core.sequences import create_number, create_number_day_by_tor
from app.crud.base import CRUDBase
from app.models.receipt import Receipt
from app.shemas.receipt import ReceiptCreate, ReceiptUpdate, ReceiptCreateInDB, ReceiptInDB


class CRUDReceipt(CRUDBase[Receipt, ReceiptCreate, ReceiptUpdate]):

    def find_by_number(self, db: Session, *, number: str):
        query = db.query(Receipt)
        return query.filter(Receipt.personal_account == number).first()


receipt = CRUDReceipt(Receipt)
