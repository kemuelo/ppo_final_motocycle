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
    day = db.Column(db.Integer, primary_key = True)
    oxygen = db.Column(db.Integer)
    fuel = db.Column(db.Integer)
    money = db.Column(db.Integer)
    energy_distribution = db.Column(db.Integer)

    def __init__(self, oxygen, fuel, money, energy_distribution):
        self.oxygen = oxygen
        self.fuel = fuel
        self.money = money
        self.energy_distribution = energy_distribution
    def __repr__(self):
        return '<Pokupki %r>' % self.username

with app.app_context():
    db.session.commit()