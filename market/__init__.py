from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from market import routes


app = Flask(__name__)  # Here the __name__ is the same script name, we are in right now.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  # Here we pass the DB file name.
app.config['SECRET_KEY'] = '184f69ae1f11ddd539a433b0'
db = SQLAlchemy(app)  # initialize an instance of the db class. Pass the app name to the db object.

from market import routes