from setup import app, db

@app.route('/')
def home():
	return 'Return all posts'

@app.route('/single')
def single():
	return 'Single post, exactact if possible'

@app.route('/vote')
def vote():
	return 'Post request to vote up or down a post'

@app.route('/comment')
def comment():
	return 'Post request for comments'

if __name__ == '__main__':
	app.run()