from models import Character, Person, Chat
from utils.inference_wrappers.inference_wrapper import Inference_Wrapper
import requests
import json

CHAT_HISTORY_COUNT = 5

class Llama_Wrapper(Inference_Wrapper):
    def __init__(self, ip):
        self.ip = ip

    def inference(self, messages, user_text, person, character):
        headers = {
            'Content-Type': 'application/json',
        }

        json_data = {
            'model': "chuanli11/Llama-3.2-3B-Instruct-uncensored",
            'messages': messages
        }
        response = requests.post(f'http://{self.ip}/v1/chat/completions', headers=headers, json=json_data)
        
        content = json.loads(response.content)
        new_message = Chat(
            text=user_text, 
            response=content["choices"][0]["message"]["content"],
            token_count=content["usage"]["total_tokens"],
            person = person.id,
            character = character.id
        )
        return new_message
        