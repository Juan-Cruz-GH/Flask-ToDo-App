from src.models.db import db
from datetime import date


class RegularTask(db.Model):
    __tablename__ = "regular_tasks"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", backref="tasks")
    deadline = db.Column(db.String(100), nullable=False)

    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    date_added = db.Column(db.Date, default=date.today)

    def __init__(self, name, description, priority, category, deadline):
        self.name = name
        self.description = description
        self.priority = priority
        self.category = category
        self.deadline = deadline


def create(data):
    db.session.add(RegularTask(**data))
    db.session.commit()


def find_by_id(id):
    return RegularTask.query.get(id)


def find_by_name(name):
    return RegularTask.query.get(name)


def update(data):
    task = RegularTask.query.get(data["id"])
    task.name = data["name"]
    task.description = data["description"]
    task.priority = data["priority"]
    task.category = data["category"]
    task.deadline = data["deadline"]
    task.is_completed = data["is_completed"]
    db.session.commit()


def delete_by_id(id):
    db.session.delete(find_by_id(id))
    db.session.commit()


def delete_by_name(name):
    db.session.delete(find_by_name(name))
    db.session.commit()


def list_tasks(page, per_page):
    tasks = (
        RegularTask.query.filter(RegularTask.is_completed == False)
        .order_by(RegularTask.priority.asc())
        .paginate(page=page, per_page=per_page)
    )
    return tasks


def complete_task(id):
    task = find_by_id(id)
    task.is_completed = True
    db.session.commit()
