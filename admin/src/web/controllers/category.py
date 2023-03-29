from flask import Blueprint, render_template, request, redirect
from src.models import category

category_blueprint = Blueprint("categories", __name__, url_prefix="/categories")


@category_blueprint.get("/add-category")
def show_form_category():
    return render_template("")


@category_blueprint.get("/category/<id>")
def show_category_data(id):
    kwargs = {"category": category.find_by_id(id)}
    return render_template("", **kwargs)


@category_blueprint.post("/create-category")
def create_category():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "icon": request.form.get("icon"),
        "color": request.form.get("color"),
    }
    category.create(data)
    return redirect("/categories/all")


@category_blueprint.post("/update-category")
def update_category():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "icon": request.form.get("icon"),
        "color": request.form.get("color"),
    }
    category.update(data)
    return redirect("/categories/all")


@category_blueprint.get("/")
def list_all():
    per_page = 10  # need this variable to be customizable eventually
    page = request.args.get("page", 1, type=int)
    kwargs = {"categories": category.list_categories(page=page, per_page=per_page)}
    return render_template("/categories/list_all.html", **kwargs)


@category_blueprint.route("/delete/<id>", methods=["GET", "DELETE"])
def delete_category(id):
    category.delete_by_id(id)
    return redirect("/categories/all")
