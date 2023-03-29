from flask import Blueprint, render_template, request, redirect
from src.models import to_do_item

to_do_item_blueprint = Blueprint("to_do_items", __name__, url_prefix="/items")


@to_do_item_blueprint.route("/form_regular")
def form_regular_item():
    return render_template("/regular_items/add_regular.html")


@to_do_item_blueprint.route("/add_regular", methods=["POST"])
def add_regular():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "state": "Not started",
        "is_recurring": False,
    }
    to_do_item.create(data)
    return redirect("/items/regulars")


@to_do_item_blueprint.route("/regulars")
def list_regulars():
    page = request.args.get("page", 1, type=int)
    kwargs = {"regular_items": to_do_item.list_regular_items(page)}
    return render_template("regular_items/list_all_regulars.html", **kwargs)


@to_do_item_blueprint.route("/form_recurring")
def form_recurring_item():
    return render_template("/recurring_items/add_recurring.html")


@to_do_item_blueprint.route("/add_recurring", methods=["POST"])
def add_recurring():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "state": "Not started",
        "is_recurring": True,
    }
    to_do_item.create(data)
    return redirect("/items/recurring")


@to_do_item_blueprint.route("/recurring")
def list_recurring():
    page = request.args.get("page", 1, type=int)
    kwargs = {"recurring_items": to_do_item.list_recurring_items(page)}
    return render_template("/recurring_items/list_all_recurring.html", **kwargs)
