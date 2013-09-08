from flask import (Blueprint, render_template, 
                    request, jsonify)
from setup import app, db

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin')
def home():
    sources = db.sources.find()
    return render_template('home.html', **{'sources': sources})

@admin.route('/admin/rule/build', methods=['POST'])
def rule_builder():
   source = request.form.get('source', '')
   source_url = request.form.get('source_url', '')
   rule = request.form.get('rule', '')

   return jsonify({'status': 'Success'})



