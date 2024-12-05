from models import Character
from app import app
from flask_login import login_user, login_required
from flask import request, render_template, redirect, url_for

@app.route("/characters/add", methods=["POST"])
@login_required
def add_character():
    name = request.form.get("name")
    prompt = request.form.get("prompt")
    character = Character(
        name = name,
        prompt = prompt
    )
    character.save_to_db()

    return redirect(url_for("characters")), 201