from flask import Blueprint, render_template

from setup import app, db
from models import Post

pages = Blueprint('pages', __name__, template_folder='templates',
                static_folder='static', static_url_path='/static')

@pages.route('/')
def home():
	posts = Post.fetch_all()
	return render_template('home.html', **{'posts': posts})

@pages.route('/single')
def single():
	return 'Single post, exactact if possible'

@pages.route('/vote')
def vote():
	return 'Post request to vote up or down a post'

@pages.route('/comment')
def comment():
	return 'Post request for comments'

