
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.receipt import Receipt
from app.shemas.receipt import ReceiptCreate, ReceiptUpdate


class CRUDReceipt(CRUDBase[Receipt, ReceiptCreate, ReceiptUpdate]):

    def find_by_number(self, db: Session, *, number: str):
        query = db.query(Receipt)
        return query.filter(Receipt.personal_account == number).first()


receipt = CRUDReceipt(Receipt)
