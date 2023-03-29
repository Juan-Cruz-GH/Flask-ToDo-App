from src.models.db import db
from datetime import date


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.LargeBinary)
    color = db.Column(db.String(6))
    date_added = db.Column(db.Date, default=date.today)

    def __init__(self, name, description, icon, color):
        self.name = name
        self.description = description
        self.icon = self.set_icon(icon)
        self.color = color

    def set_icon(self, icon):
        if icon is None:
            self.icon = None
        else:
            self.icon = icon.encode("utf-8")

    def get_icon(self):
        return self.icon.decode("utf-8")


def create(data):
    db.session.add(Category(**data))
    db.session.commit()


def find_by_id(id):
    return Category.query.get(id)


def find_by_name(name):
    return Category.query.filter(Category.name == name).first()


def update(data):
    category = Category.query.get(data["id"])
    category.name = data["name"]
    category.description = data["description"]
    category.icon = data["icon"]
    category.color = data["color"]
    db.session.commit()


def delete_by_id(id):
    db.session.delete(find_by_id(id))
    db.session.commit()


def delete_by_name(name):
    db.session.delete(find_by_name(name))
    db.session.commit()


def list_categories(page, per_page):
    categories = Category.query.order_by(Category.name.asc()).paginate(
        page=page, per_page=per_page
    )
    return categories


def all_categories():
    list = []
    categories = Category.query.order_by(Category.name).all()
    for category in categories:
        row = category.__dict__
        dict = {
            "id": row["id"],
            "name": row["name"],
            "description": row["description"],
            "icon": row["icon"],
            "color": row["color"],
            "date_added": row["date_added"],
        }
        list.append(dict)
    return list
