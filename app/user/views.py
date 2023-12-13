from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user

from app.user.models import User
from app.extensions import bcrypt, db

blueprint = Blueprint("user", __name__, url_prefix="/user")


@blueprint.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("user/register.html")
    else:
        if request.form.get('password') != request.form.get('confirm-password'):
            flash("Password tidak sama", 'error')
            return redirect(url_for('user.register'))

        user = User()
        user.username = request.form.get("username")
        user.password = bcrypt.generate_password_hash(request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.login'))


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("user/login.html")
    else:
        user = User.query.filter_by(username=request.form.get("username")).first()
        if not user:
            flash("Username atau password salah", 'error')
            return redirect(url_for('user.login'))

        if not bcrypt.check_password_hash(user.password, request.form.get("password")):
            flash("Username atau password salah", 'error')
            return redirect(url_for('user.login'))

        login_user(user)
        return redirect(url_for('public.home'))

@blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('public.home'))