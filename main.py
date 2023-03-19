from flask import Flask
from app import app
from flask import request
app = Flask(__name__)
from request import *


@app.route('/')
def hello():
    return '''<!DOCTYPE html>
                <html>
                  <head>
                    <title>Программа расчёта</title>
                  </head>
                  <body>
                    <h1>П!</h1>
                    <ul>
                      <li></li>
                    </ul>
                  </body>
                </html>'''

if __name__ == "__main__":
    app.run()