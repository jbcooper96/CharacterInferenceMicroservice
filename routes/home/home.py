from app import app
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("add_device"))
    else:
        return redirect(url_for("login"))