from flask import Flask
import products_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"