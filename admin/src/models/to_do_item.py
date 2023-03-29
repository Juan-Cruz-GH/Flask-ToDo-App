from src.models.db import db
from datetime import datetime


class ToDoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    is_recurring = db.Column(db.Boolean, nullable=False)
    inserted_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name, description, is_recurring):
        self.name = name
        self.description = description
        self.is_recurring = is_recurring

    def __repr__(self) -> str:
        return f"Item with name {self.name} and description {self.description}"


def create(data):
    db.session.add(ToDoItem(**data))
    db.session.commit()


def read(id):
    return ToDoItem.query.get(id)


def update(data):
    item = ToDoItem.query.get(data["id"])
    item.name = data["name"]
    item.description = data["description"]
    item.is_recurring = data["is_recurring"]
    db.session.commit()


def delete(id):
    db.session.delete(read(id))
    db.session.commit()


def is_recurring(id):
    return read(id).is_recurring


def list_items(page):
    return ToDoItem.query.paginate(
        page, per_page=10
    )  # should ask the config module later
