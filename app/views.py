from app import app, db
from .models import Visit
from flask import render_template


@app.route('/')
def home():
    view_counter = Visit.query.first()
    view_counter.count = Visit.count + 1
    db.session.commit()

    return render_template('index.html', count=view_counter.count)
