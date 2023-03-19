from flask import Flask
from flask_migrate import Migrate
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Pokupki(db.Model):
    __tablename__ = 'pokupki'
    id = db.Column(db.Integer, primary_key = True)
    oxygen = db.Column(db.Integer, primary_key = True)
    fuel = db.Column(db.Integer, primary_key = True)

    def __init__(self, oxygen, fuel):
        self.oxygen = oxygen
        self.fuel = fuel
    def __repr__(self):
        return '<Pokupki %r>' % self.username

with app.app_context():
    db.session.commit()