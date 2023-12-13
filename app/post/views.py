from flask import Blueprint, render_template

blueprint = Blueprint("post", __name__, url_prefix="/post")


@blueprint.route("/create")
def create():
    pass

@blueprint.route("/update")
def update():
    pass