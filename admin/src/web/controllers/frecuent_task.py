from flask import Blueprint, render_template, request, redirect, url_for
from src.models import frecuent_task
from src.models import category

frecuent_task_blueprint = Blueprint(
    "frecuent_tasks", __name__, url_prefix="/frecuent-tasks"
)


@frecuent_task_blueprint.route("/create-task", methods=["GET", "POST"])
def create_task():
    if request.method == "GET":
        return render_template(
            "/frecuent_tasks/add_task.html",
            categories=category.all_categories(),
        )
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "priority": int(request.form.get("priority")),
        "category": category.find_by_id(request.form.get("category_id")),
        "frecuency": request.form.get("frecuency"),
    }
    frecuent_task.create(data)
    return redirect(url_for("frecuent_tasks.list_all", category=data["category"].name))


@frecuent_task_blueprint.route("/task/<id>", methods=["GET", "POST"])
def update_task(id):
    if request.method == "GET":
        kwargs = {
            "task": frecuent_task.find_by_id(id),
            "categories": category.all_categories(),
        }
        return render_template("/frecuent_tasks/show_task.html", **kwargs)
    data = {
        "id": request.form.get("id"),
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "priority": int(request.form.get("priority")),
        "category": category.find_by_id(request.form.get("category_id")),
        "frecuency": request.form.get("frecuency"),
        "completed_today": request.form.get("completedToday") == "yes",
    }
    frecuent_task.update(data)
    return redirect(url_for("frecuent_tasks.list_all", category=data["category"].name))


@frecuent_task_blueprint.get("/")
def list_all():
    per_page = 10  # need this variable to be customizable eventually
    category_arg = request.args.get("category", "Facultad", type=str)
    category_id = category.find_by_name(category_arg).id
    page = request.args.get("page", 1, type=int)
    kwargs = {
        "tasks": frecuent_task.list_tasks(
            category_id=category_id, page=page, per_page=per_page
        ),
        "categories": category.all_categories(),
    }
    return render_template("/frecuent_tasks/list_all.html", **kwargs)


@frecuent_task_blueprint.route("/delete/<id>", methods=["GET", "DELETE"])
def delete_task(id):
    task = frecuent_task.find_by_id(id)
    category = task.category.name
    frecuent_task.delete_by_id(id)
    return redirect(url_for("frecuent_tasks.list_all", category=category))
