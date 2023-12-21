from sqlalchemy.orm import Mapped, mapped_column
from app import db


class Visit(db.Model):
    __tablename__ = 'count_view'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    count: Mapped[str] = mapped_column(db.Integer)

    def __init__(self, id, count):
        self.id = id
        self.count = count
