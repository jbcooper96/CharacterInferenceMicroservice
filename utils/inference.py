from utils.inference_wrappers.open_ai_wrapper import Open_AI_Wrapper
from utils.inference_wrappers.llama_wrapper import Llama_Wrapper
from enums.inference_agent import Inference_Agent

class Inference:
    def __init__(self, inference_agent=Inference_Agent.GPT, llama_ip=None):
        self.inference_agent = inference_agent
        self.llama_ip = llama_ip
        self.set_inference_agent(inference_agent)

    def get_chat_completion(self, user_text, person_name, character_name):
        return self.inference_wrapper.get_chat_completion(user_text, person_name, character_name)

    def set_inference_agent(self, inference_agent):
        self.inference_agent = inference_agent
        if inference_agent == Inference_Agent.GPT:
            self.inference_wrapper = Open_AI_Wrapper()
        elif inference_agent == Inference_Agent.LLAMA:
            self.inference_wrapper = Llama_Wrapper(self.llama_ip)

    def set_llama_ip(self, llama_ip):
        if self.inference_agent == Inference_Agent.LLAMA:
            self.inference_wrapper.ip = llama_ip
            self.llama_ip = llama_ip