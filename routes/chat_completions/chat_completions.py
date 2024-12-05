from flask import request
from app import app, open_ai_wrapper
from utils.security import api_required

@app.route("/chatcompletions", methods=["POST"])
@api_required
def chat_completions():
    character = request.json.get("character")
    person = request.json.get("person")
    text = request.json.get("text")
    if person == None or text == None or character == None:
        return {"message": "Invalid input"}, 422
    
    response = open_ai_wrapper.get_chat_completion(text, person, character)
    return response, 200
