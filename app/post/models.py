from typing import List
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db


post_categories_table = db.Table(
    "post_categories",
    db.metadata,
    db.Column("post_id", db.ForeignKey("posts.id")),
    db.Column("category_id", db.ForeignKey("categories.id")),
)

class Post(db.Model):
    __tablename__ = "posts"
    id = mapped_column(Integer, primary_key=True)
    title: Mapped[str]
    body: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="posts")
    categories: Mapped[List["Category"]] = relationship(
        secondary=post_categories_table,
        back_populates="posts",
    )


class Category(db.Model):
    __tablename__ = "categories"
    id = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    posts: Mapped[List["Post"]] = relationship(
        secondary=post_categories_table,
        back_populates="categories"
    )
