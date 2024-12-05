from models import User
from app import app
from flask_login import login_user
from flask import request, render_template, redirect, url_for

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form.get("username")).first()
        
        if user.password == request.form.get("password"):
            login_user(user)
            return redirect(url_for("home"))
        
    return render_template("login.html")