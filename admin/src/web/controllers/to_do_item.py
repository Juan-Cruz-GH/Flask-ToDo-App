from flask import Blueprint
from src.models import to_do_item

to_do_item_blueprint = Blueprint("to_do_items", __name__, url_prefix="/items")


@to_do_item_blueprint.route("/add", methods=["POST"])
def add():
    return "add"
