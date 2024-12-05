from models import Device
import functools
from hmac import compare_digest
from flask import request

def is_valid(api_key):
    device = Device.find_by_device_key(api_key)
    if device and compare_digest(device.device_key, api_key):
        return True

def api_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if request.json:
            api_key = request.json.get("api_key")
        else:
            return {"message": "Please provide an API key"}, 400
        # Check if API key is correct and valid
        if request.method == "POST" and is_valid(api_key):
            return func(*args, **kwargs)
        else:
            return {"message": "The provided API key is not valid"}, 403
    return decorator