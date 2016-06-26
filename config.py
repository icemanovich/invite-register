import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Turns on debugging features in Flask
DEBUG = os.environ.get('DEBUG', False)

# Configuration for the Flask-Bcrypt extension
BCRYPT_LEVEL = int(os.environ.get('BCRYPT_LEVEL', 12))

MAIL_FROM_EMAIL = os.environ.get('MAIL_FROM_EMAIL', "info@example.com")
SECRET_KEY = os.environ.get('SECRET_KEY')

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

NAME = os.environ.get('NAME', 'invite-register')

THREADED = os.environ.get('THREADED', False)

APP_HOST = os.environ.get('APP_HOST', '0.0.0.0')
APP_PORT = int(os.environ.get('APP_PORT', 8080))





