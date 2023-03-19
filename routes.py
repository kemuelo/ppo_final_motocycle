from app import app, Pokupki, db
from flask import request

@app.route('/')
def hello():
    return 'hello'