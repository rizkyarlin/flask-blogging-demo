from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str]
