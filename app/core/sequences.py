import datetime
from typing import TypeVar, Type

from sqlalchemy import func, cast, Date
from sqlalchemy.orm import Session

from app.models.receipt import Receipt
from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


def create_number(db: Session, model: Type[ModelType]):
    count_item = db.query(model).count()
    next_item = count_item + 1
    day = datetime.date.today()

    y = day.strftime('%Y')
    m = day.strftime('%m')
    d = day.strftime('%d')
    new_number = y + m + d + "{:05d}".format(next_item)
    return new_number


def create_number_day_by_tor(db: Session, day: datetime.date, tor_id: int, model: Type[ModelType]):

    count_item = db.query(model).filter_by(
        tor_id=tor_id).filter(cast(model.created_at, Date) == day).count()  # db.query(model).count()

    next_item = count_item + 1
    y = day.strftime('%Y')
    m = day.strftime('%m')
    d = day.strftime('%d')
    new_number = y + m + d + str(tor_id) + "{:05d}".format(next_item)
    return new_number


def create_number_by_tor(db: Session, tor_id: int, model: Type[ModelType]):
    count_item = db.query(model).filter_by(tor_id=tor_id).count()  # db.query(model).count()

    next_item = count_item + 1
    current_date = datetime.date.today()
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')
    day = current_date.strftime('%d')

    new_number = year + month + day + str(tor_id) + "{:05d}".format(next_item)
    return new_number
