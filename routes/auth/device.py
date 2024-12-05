from flask import request, render_template
from flask_login import login_required, current_user
from app import app
from models import Device

@app.route("/add-device", methods=["GET", "POST"])
@login_required
def add_device():
    if request.method == "POST":
        device_name = request.form.get("device_name")
        device = Device.find_by_name(device_name)
        if device != None:
            return {'message': f"A device with name '{device_name}' already exists."}, 400
        device = Device(
            device_name=device_name,
            user_id=current_user.get_id()
        )
        device.save_to_db()

        return render_template("add_device.html", key=device.device_key), 201


    return render_template("add_device.html")

