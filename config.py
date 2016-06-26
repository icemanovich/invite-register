import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import timedelta


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def make_sqlite_uri(db_name) -> str:
    """ Make connection string with DB

    :param db_name: database name
    :return:
    """
    return 'sqlite:///{0}'.format(os.path.join(BASE_DIR, '{0}.sqlite'.format(db_name)))


class ConfigBase(object):

    APP_HOST = os.environ.get('APP_HOST', '0.0.0.0')
    APP_PORT = int(os.environ.get('APP_PORT', 8080))

    THREADED = os.environ.get('THREADED', False)

    # Turns on debugging features in Flask
    DEBUG = os.environ.get('DEBUG', False)

    # Turn off by default
    TESTING = False

    # Configuration for the Flask-Bcrypt extension
    BCRYPT_LEVEL = int(os.environ.get('BCRYPT_LEVEL', 12))

    MAIL_FROM_EMAIL = os.environ.get('MAIL_FROM_EMAIL', "info@example.com")
    MAIL_DEBUG = os.environ.get('MAIL_DEBUG', 1)
    SECRET_KEY = os.environ.get('SECRET_KEY')

    NAME = os.environ.get('NAME', 'invite_register')

    CSRF_ENABLED = os.environ.get('CSRF_ENABLED', True)

    # The lifetime of a permanent session
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)

    # Flask-SQLAlchemy will not track modifications of objects and emit signals
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Enable query recording
    SQLALCHEMY_RECORD_QUERIES = False

    # Database location
    SQLALCHEMY_DATABASE_URI = make_sqlite_uri('invite_register_dev.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
    DATABASE_CONNECT_OPTIONS = {}


class ConfigProduction(ConfigBase):
    SQLALCHEMY_DATABASE_URI = make_sqlite_uri('invite_register.db')


class ConfigDevelopment(ConfigBase):
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_DATABASE_URI = make_sqlite_uri('invite_register_dev')


class ConfigTesting(ConfigBase):
    # Enable testing mode
    TESTING = True

    SQLALCHEMY_DATABASE_URI = make_sqlite_uri('invite_register_test')
    WTF_CSRF_ENABLED = False


def load_config(stage='development'):
    """ Get config object depends on type

    :param stage:
    :return:
    """
    patterns = {
        'production': ConfigProduction,
        'development': ConfigDevelopment,
        'testing': ConfigTesting,
    }

    if stage.lower() in patterns:
        return patterns[stage.lower()]

    return patterns['development']
