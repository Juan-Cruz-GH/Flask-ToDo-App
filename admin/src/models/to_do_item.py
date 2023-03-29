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

    def add():
        pass
