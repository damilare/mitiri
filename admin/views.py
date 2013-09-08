from flask import Blueprint, render_template
from setup import app, db

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin')
def home():
    sources = db.sources.find()
    return render_template('home.html', **{'sources': sources})


