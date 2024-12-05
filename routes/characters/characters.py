from models import User, Character
from app import app
from flask_login import login_user, login_required
from flask import request, render_template, redirect, url_for

@app.route("/characters", methods=["GET"])
@login_required
def characters():
    page = request.args.get('page')
    if page == None:
        page = 1
    characters = Character.get_all_paginated(page=page)
    return render_template("characters.html", characters=characters)
    