from models import Character, Person, Chat

CHAT_HISTORY_COUNT = 5

class Inference_Wrapper:
    def get_chat_completion(self, user_text, person_name, character_name):
        character = Character.get_by_name(character_name)
        if character == None:
            return "", "Character name does not exist"
        
        person = Person.get_or_create_by_name(person_name)
        messages = self.get_messages(character, person, user_text)
        new_message = self.inference(messages, user_text, person, character)

        new_message.save_to_db()
        return new_message.response

    def inference(self, messages, user_text, person, character):
        pass

    def get_messages(self, character, person, user_text):
        messages = [self.get_message(character.prompt, "system")]
        chats = Chat.get_chats_for_person_and_character(person, character)
        if chats != None:
            for chat in chats[:CHAT_HISTORY_COUNT]:
                messages.append(self.get_message(chat.text))
                messages.append(self.get_message(chat.response, "assistant"))

        messages.append(self.get_message(user_text))
        return messages
            

    def get_message(self, text, role="user"):
        return {
            "role": role,
            "content": text
        }
        