from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from enums.inference_agent import Inference_Agent

basedir = os.path.abspath(os.path.dirname(__file__))

environment = os.environ["ENVIRONMENT_NAME"]
is_dev = environment == "DEV"

app = Flask(__name__)
if is_dev:
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_STRING"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from utils.inference import Inference
open_ai_wrapper = Inference(Inference_Agent.LLAMA)

from models import User
@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)

import routes.home.home 
import routes.auth.login
import routes.auth.logout
import routes.auth.device
import routes.characters.characters
import routes.characters.add_character
import routes.chat_completions.chat_completions
import routes.settings.inference_setting_page

if __name__ == "__main__":
    app.run()