from src.models.db import db
from datetime import date

PER_PAGE = 9


class ToDoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    is_recurring = db.Column(db.Boolean, nullable=False)
    inserted_at = db.Column(db.Date, default=date.today)

    def __init__(self, name, description, state, priority, is_recurring):
        self.name = name
        self.description = description
        self.state = state
        self.priority = priority
        self.is_recurring = is_recurring

    def __repr__(self) -> str:
        return (
            f"Name {self.name} \n Description {self.description} \n State {self.state}"
        )


def create(data):
    db.session.add(ToDoItem(**data))
    db.session.commit()


def read(id):
    return ToDoItem.query.get(id)


def update(data):
    item = ToDoItem.query.get(data["id"])
    item.name = data["name"]
    item.description = data["description"]
    item.state = data["state"]
    item.priority = data["priority"]
    item.is_recurring = data["is_recurring"]
    db.session.commit()


def delete(id):
    db.session.delete(read(id))
    db.session.commit()


def is_recurring(id):
    return read(id).is_recurring


def list_regular_items(page):
    regulars = (
        ToDoItem.query.filter(ToDoItem.is_recurring == False)
        .order_by(ToDoItem.priority.desc())
        .paginate(page=page, per_page=PER_PAGE)
    )
    return regulars


def list_recurring_items(page):
    recurring = (
        ToDoItem.query.filter(ToDoItem.is_recurring == True)
        .order_by(ToDoItem.priority.desc())
        .paginate(page=page, per_page=PER_PAGE)
    )
    return recurring
