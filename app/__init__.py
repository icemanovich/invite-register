import os
from flask import Flask
from config import load_config
from app.modules.ConsoleMail import ConsoleMail
import wtforms_json
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

__title__ = 'Invite Register Example'
__version__ = '0.1'


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object(load_config(os.environ.get('STAGE')))
app.name = app.config['NAME']

''' db - connected Database instance '''
db = SQLAlchemy(app)
mail = ConsoleMail()
mail.init_app(app)

wtforms_json.init()
CsrfProtect(app)

from app import views
