import requests
from app import db

class Loader(object):
    def __init__(self):
        pass

    def fetch(self, url):
        ''' Fetches a URL '''
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.content


