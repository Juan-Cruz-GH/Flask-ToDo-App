from flask import Blueprint, render_template, request, redirect
from src.models import to_do_item

to_do_item_blueprint = Blueprint("to_do_items", __name__, url_prefix="/items")


@to_do_item_blueprint.route("/add_regular", methods=["POST"])
def add_regular():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "is_recurring": False,
    }
    to_do_item.create(data)
    return redirect("/items/regulars")


@to_do_item_blueprint.route("/add_recurring", methods=["POST"])
def add_recurring():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "is_recurring": True,
    }
    to_do_item.create(data)
    return redirect("/items/recurring")


@to_do_item_blueprint.route("/regulars")
def list_regulars():
    return "regulars"


@to_do_item_blueprint.route("/recurring")
def list_recurring():
    return "recurring"


@to_do_item_blueprint.route("/form_recurring")
def form_recurring_item():
    return render_template("/recurring_items/add.html")


@to_do_item_blueprint.route("/form_regular")
def form_regular_item():
    return render_template("/regular_items/add.html")
