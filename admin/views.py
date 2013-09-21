import json
from bson import ObjectId
from flask import (Blueprint, render_template,
                    request, jsonify)
from setup import db
from models.trawler import Trawler

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin')
def home():
    sources = db.sources.find()
    return render_template('home.html', **{'sources': sources})

@admin.route('/admin/rule/preview', methods=['POST'])
def preview_rule():
    to_trawl = None
    trawler = Trawler(db)

    source_id = request.form.get('source_id', None)
    source_url = request.form.get('source_url', '')
    rules = request.form.get('rules', None)
    if rules:
        rules = json.loads(rules)
        # source_url overrides source
        if len(source_url) > 1:
            to_trawl = source_url
        else:
            source = db.sources.find_one({'_id': ObjectId(source_id)})
            if source:
                to_trawl = source['url']

    # trawl
    if to_trawl:
        entries = trawler.trawl_url(to_trawl, rules=rules, source_id=source_id)
        if entries:
            return jsonify({'status': 'Success', 'entries': entries})

    return jsonify({'status': 'Failure'})


@admin.route('/admin/rule/save', methods=['POST'])
def save_rule():
    source_id = request.form.get('source_id', None)
    source_url = request.form.get('source_url', '')
    rules = request.form.get('rules', None)

    if not source_id and source_url:
       source_id = db.sources.insert({'url': source_url, 'weight': 1})
      
    if rules:
       rules = json.loads(rules)
       db.rules.insert({'source_id': source_id, 'elem': rules['elem'], 'class': rules['class']})

    return jsonify({'status': 'Success', 'message': 'Rule successfully created'})
