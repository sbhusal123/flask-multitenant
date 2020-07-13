import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get config file
try:
    config = os.environ['CONFIG']
except KeyError as ke:
    config = 'development.cfg'
config_file = os.getcwd() + '/config/' + config

# Init flask app
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile(config_file)

# Init database with SqlAlchemy
db = SQLAlchemy(app)

