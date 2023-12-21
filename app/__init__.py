from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.models import *

with app.app_context():
    db.create_all()
    view_counter = Visit.query.first()
    if not view_counter:
        v = Visit(id='1', count='0')
        db.session.add(v)
        db.session.commit()

from app import views



