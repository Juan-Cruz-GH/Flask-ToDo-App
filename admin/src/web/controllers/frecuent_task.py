from flask import Blueprint, render_template, request, redirect
from src.models import frecuent_task

frecuent_task_blueprint = Blueprint(
    "frecuent_tasks", __name__, url_prefix="/frecuent-tasks"
)


@frecuent_task_blueprint.get("/add-task")
def show_form_task():
    return render_template("")


@frecuent_task_blueprint.get("/task/<id>")
def show_task_data(id):
    kwargs = {"task": frecuent_task.find_by_id(id)}
    return render_template("", **kwargs)


@frecuent_task_blueprint.post("/create-task")
def create_task():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "priority": request.form.get("priority"),
        "category": request.form.get("category"),
        "frecuency": request.form.get("frecuency"),
    }
    frecuent_task.create(data)
    return redirect("/frecuent-tasks/all")


@frecuent_task_blueprint.post("/update-task")
def update_task():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "priority": request.form.get("priority"),
        "category": request.form.get("category"),
        "frecuency": request.form.get("frecuency"),
        "last_completed": request.form.get("last_completed"),
    }
    frecuent_task.update(data)
    return redirect("/frecuent-tasks/all")


@frecuent_task_blueprint.get("/")
def list_all():
    per_page = 10  # need this variable to be customizable eventually
    page = request.args.get("page", 1, type=int)
    kwargs = {"tasks": frecuent_task.list_tasks(page=page, per_page=per_page)}
    return render_template("/frecuent_tasks/list_all.html", **kwargs)


@frecuent_task_blueprint.route("/delete/<id>", methods=["GET", "DELETE"])
def delete_task(id):
    frecuent_task.delete_by_id(id)
    return redirect("/frecuent-tasks/all")
