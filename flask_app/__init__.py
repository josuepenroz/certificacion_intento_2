from flask import Flask
app = Flask(__name__)
from flask_app.controllers import usuarios
app.secret_key = "akld32dadsa"