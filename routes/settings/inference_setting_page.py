from flask import request, render_template
from flask_login import login_required, current_user
from app import app, open_ai_wrapper
from models import Device
from enums.inference_agent import Inference_Agent

@app.route("/inference-setting", methods=["GET", "POST"])
@login_required
def inference_setting():
    if request.method == "POST":
        print(request.form)
        selected_inference_agent = Inference_Agent.GPT if request.form.get("inference-select") == "gpt" else Inference_Agent.LLAMA
        if open_ai_wrapper.inference_agent != selected_inference_agent:
            open_ai_wrapper.set_inference_agent(selected_inference_agent)
        open_ai_wrapper.set_llama_ip(request.form.get("ip"))

    gpt = open_ai_wrapper.inference_agent == Inference_Agent.GPT
    llama = open_ai_wrapper.inference_agent == Inference_Agent.LLAMA
        
    return render_template("inference_setting.html", ip=open_ai_wrapper.llama_ip, gpt=gpt, llama=llama)