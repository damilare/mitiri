from flask import Blueprint, render_template

from setup import app, db
from models import Post

pages = Blueprint('pages', __name__, template_folder='templates')

@pages.route('/')
def home():
	posts = Post.fetch_all()
	return render_template('home.html', **{'posts': posts})

@pages.route('/single/<post_id>')
def single(post_id):
	posts = Post.fetch_one(post_id)
	return render_template('single.html', **{'post': posts})

@pages.route('/vote')
def vote():
	return 'Post request to vote up or down a post'

@pages.route('/comment')
def comment():
	return 'Post request for comments'

@pages.route('/external')
def external(post_slug):
	return 'Store stat and take user away'

