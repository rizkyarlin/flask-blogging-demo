from flask import Blueprint, render_template

blueprint = Blueprint("user", __name__, url_prefix="/user")


@blueprint.route("/register")
def register():
    return render_template("home.html", posts=range(10))

@blueprint.route("/login")
def login():
    pass

@blueprint.route("/logout")
def logout():
    pass