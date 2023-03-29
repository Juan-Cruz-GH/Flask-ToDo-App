from flask import Blueprint, render_template, request, redirect
from src.models import to_do_item

to_do_item_blueprint = Blueprint("to_do_items", __name__, url_prefix="/items")


@to_do_item_blueprint.get("/form_regular")
def form_regular_item():
    return render_template("/regular_items/add_regular.html")


@to_do_item_blueprint.get("/regular/<id>")
def regular_item_profile(id):
    kwargs = {"regular_item": to_do_item.find(id)}
    return render_template("/regular_items/show_item.html", **kwargs)


@to_do_item_blueprint.post("/add_regular")
def add_regular():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "state": "Not started",
        "priority": request.form.get("priority"),
        "is_recurring": False,
    }
    to_do_item.create(data)
    return redirect("/items/regulars")


@to_do_item_blueprint.post("/modify_regular")
def update_regular():
    data = {
        "id": request.form.get("id"),
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "state": request.form.get("state"),
        "priority": request.form.get("priority"),
        "is_recurring": False,
    }
    to_do_item.update(data)
    return redirect("/items/regulars")


@to_do_item_blueprint.get("/regulars")
def list_regulars():
    page = request.args.get("page", 1, type=int)
    kwargs = {"regular_items": to_do_item.list_regular_items(page)}
    return render_template("regular_items/list_all_regulars.html", **kwargs)


@to_do_item_blueprint.get("/form_recurring")
def form_recurring_item():
    return render_template("/recurring_items/add_recurring.html")


@to_do_item_blueprint.get("/recurring/<id>")
def recurring_item_profile(id):
    kwargs = {"recurring_item": to_do_item.find(id)}
    return render_template("/recurring_items/show_item.html", **kwargs)


@to_do_item_blueprint.post("/add_recurring")
def add_recurring():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "state": "Not started",
        "priority": request.form.get("priority"),
        "is_recurring": True,
    }
    to_do_item.create(data)
    return redirect("/items/recurring")


@to_do_item_blueprint.post("/modify_recurring")
def update_recurring():
    data = {
        "id": request.form.get("id"),
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "state": request.form.get("state"),
        "priority": request.form.get("priority"),
        "is_recurring": True,
    }
    to_do_item.update(data)
    return redirect("/items/recurring")


@to_do_item_blueprint.get("/recurring")
def list_recurring():
    page = request.args.get("page", 1, type=int)
    kwargs = {"recurring_items": to_do_item.list_recurring_items(page)}
    return render_template("/recurring_items/list_all_recurring.html", **kwargs)


@to_do_item_blueprint.delete("/delete/<id>")
def to_do_item_delete(id):
    item = to_do_item.find(id)
    to_do_item.delete(id)
    if item.is_recurring:
        return redirect("/items/recurring")
    return redirect("/items/regulars")
