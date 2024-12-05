from models import Character, Person, Chat
from openai import OpenAI
from utils.inference_wrappers.inference_wrapper import Inference_Wrapper

CHAT_HISTORY_COUNT = 5

class Open_AI_Wrapper(Inference_Wrapper):
    def __init__(self):
        self.client = OpenAI()

    def inference(self, messages, user_text, person, character):
        chat_completion = self.client.chat.completions.create(messages=messages, model="gpt-4o")
        new_message = Chat(
            text=user_text, 
            response=chat_completion.choices[0].message.content,
            token_count=chat_completion.usage.total_tokens,
            person = person.id,
            character = character.id
        )
        return new_message
        