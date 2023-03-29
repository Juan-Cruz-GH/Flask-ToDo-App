from src.models.db import db
from datetime import date


class FrecuentTask(db.Model):
    __tablename__ = "frecuent_tasks"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", backref="frequent_tasks")
    frecuency = db.Column(db.String(50), nullable=False)

    last_completed = db.Column(db.Date, default=date.min, nullable=False)
    date_added = db.Column(db.Date, default=date.today)

    def __init__(self, name, description, priority, category, frecuency):
        if priority < 0 or priority > 5:
            raise ValueError("Priority must be an integer between 0 and 5.")
        self.name = name
        self.description = description
        self.priority = priority
        self.category = category
        self.frecuency = frecuency


def create(data):
    db.session.add(FrecuentTask(**data))
    db.session.commit()


def find_by_id(id):
    return FrecuentTask.query.get(id)


def find_by_name(name):
    return FrecuentTask.query.get(name)


def update(data):
    task = FrecuentTask.query.get(data["id"])
    task.name = data["name"]
    task.description = data["description"]
    task.priority = data["priority"]
    task.category = data["category"]
    task.frecuency = data["frecuency"]
    if data["completed_today"]:
        task.last_completed = date.today()
    db.session.commit()


def delete_by_id(id):
    db.session.delete(find_by_id(id))
    db.session.commit()


def delete_by_name(name):
    db.session.delete(find_by_name(name))
    db.session.commit()


def list_tasks(category_id, page, per_page):
    category_tasks = FrecuentTask.query.filter_by(category_id=category_id)
    tasks = category_tasks.order_by(FrecuentTask.priority.asc()).paginate(
        page=page, per_page=per_page
    )
    return tasks
