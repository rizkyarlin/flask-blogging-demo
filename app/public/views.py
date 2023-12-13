from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint("public", __name__, url_prefix="/")


@blueprint.route("/")
def home():
    return render_template("home.html", posts=range(10))

