from setup import db

class Document(object):
	def __init__(self):
		self.db = db
		validation_rules = None

	def _is_empty(self, var, default_type=dict):
		return var if not var else default_type()

	def insert(self, doc):
		self._validate(doc)
		self.collection.insert(doc)

	@classmethod
	def fetch_all(self):
		return db.posts.find()

	def find_one(self, condition=None):
		return self.collection.find_one(self._is_empty(condition))

	def delete(self, condition=None):
		return self.collection.remove(self._is_empty(condition))		
		
	def update(self, condition=None):
		raise NotImplementedError("Coming Soon")

	def _validate(self, doc):
		""" Look for validation rule """
		pass

	def _set_validation(self):
		pass

class Post(Document):
	def __init__(self, *args, **kwargs):
		super(Post, self ).__init__()
		self.collection = self.db.post
		
class Comment(Document):
	pass


