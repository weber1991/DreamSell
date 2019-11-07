from . import home
from app import db
from app.home.forms import RegisterForm
from flask import render_template, url_for, redirect, session
from werkzeug.security import generate_password_hash


@home.route("/")
def index():
    return render_template('home/index.html')

@home.route("/register/", methods=["GET", "POST"])
def register():
    '''
    注册功能
    '''
    if "user_id" in session:
        return redirect(url_for("home.index"))
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            username = data["username"],
            email = data["email"],
            password = generate_password_hash(data["password"]),
            phone = data["phone"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home.index"))
    return render_template("home/register.html", form=form)

@home.route("/login/", methods=["GET", "POST"])
def login():
    return "login"