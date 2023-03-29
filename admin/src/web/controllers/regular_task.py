from flask import Blueprint, render_template, request, redirect, url_for
from src.models import regular_task
from src.models import category
from datetime import date

regular_task_blueprint = Blueprint("regular_tasks", __name__, url_prefix="/regular-tasks")


@regular_task_blueprint.route("/create-task", methods=["GET", "POST"])
def create_task():
    if request.method == "GET":
        return render_template(
            "/regular_tasks/add_task.html", categories=category.all_categories()
        )
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "priority": int(request.form.get("priority")),
        "category": category.find_by_id(request.form.get("category_id")),
        "deadline": request.form.get("deadline"),
    }
    if data["deadline"] == "":
        data["deadline"] = date.min
    regular_task.create(data)
    return redirect(url_for("regular_tasks.list_all", category=data["category"].name))


@regular_task_blueprint.route("/task/<id>", methods=["GET", "POST"])
def update_task(id):
    if request.method == "GET":
        kwargs = {
            "task": regular_task.find_by_id(id),
            "categories": category.all_categories(),
        }
        return render_template("/regular_tasks/show_task.html", **kwargs)
    data = {
        "id": request.form.get("id"),
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "priority": int(request.form.get("priority")),
        "category": category.find_by_id(request.form.get("category_id")),
        "deadline": request.form.get("deadline"),
        "is_completed": request.form.get("is_completed") == "yes",
    }
    regular_task.update(data)
    return redirect(url_for("regular_tasks.list_all", category=data["category"].name))


@regular_task_blueprint.get("/")
def list_all():
    per_page = 10  # need this variable to be customizable eventually
    category_arg = request.args.get("category", "Facultad", type=str)
    selected_category = category.find_by_name(category_arg)
    page = request.args.get("page", 1, type=int)
    kwargs = {
        "tasks": regular_task.list_tasks(
            category_id=selected_category.id, page=page, per_page=per_page
        ),
        "categories": category.all_categories(),
        "header": selected_category.name,
    }
    return render_template("/regular_tasks/list_all.html", **kwargs)


@regular_task_blueprint.route("/delete/<id>", methods=["GET", "DELETE"])
def delete_task(id):
    task = regular_task.find_by_id(id)
    category = task.category.name
    regular_task.delete_by_id(id)
    return redirect(url_for("regular_tasks.list_all", category=category))
