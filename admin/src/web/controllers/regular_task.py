from flask import Blueprint, render_template, request, redirect
from src.models import regular_task

regular_task_blueprint = Blueprint("regular_tasks", __name__, url_prefix="/regular-tasks")


@regular_task_blueprint.get("/add-task")
def show_form_task():
    return render_template("")


@regular_task_blueprint.get("/task/<id>")
def show_task_data(id):
    kwargs = {"task": regular_task.find_by_id(id)}
    return render_template("", **kwargs)


@regular_task_blueprint.post("/create-task")
def create_task():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "priority": request.form.get("priority"),
        "category": request.form.get("category"),
        "deadline": request.form.get("deadline"),
        "is_completed": request.form.get("is_completed"),
    }
    regular_task.create(data)
    return redirect("/regular-tasks/all")


@regular_task_blueprint.post("/update-task")
def update_task():
    data = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "priority": request.form.get("priority"),
        "category": request.form.get("category"),
        "deadline": request.form.get("deadline"),
        "is_completed": request.form.get("is_completed"),
    }
    regular_task.update(data)
    return redirect("/regular-tasks/all")


@regular_task_blueprint.get("/")
def list_all():
    per_page = 10  # need this variable to be customizable eventually
    page = request.args.get("page", 1, type=int)
    kwargs = {"tasks": regular_task.list_tasks(page=page, per_page=per_page)}
    return render_template("/regular_tasks/list_all.html", **kwargs)


@regular_task_blueprint.route("/delete/<id>", methods=["GET", "DELETE"])
def delete_task(id):
    regular_task.delete_by_id(id)
    return redirect("/regular-tasks/all")
