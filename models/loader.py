import logging
import requests
from setup import db

logger = logging.getLogger('mitiri')

class Loader(object):
    def __init__(self):
        pass

    def load(self, url):
        ''' Fetches a URL '''
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                return resp.content
        except e:
            logger.error("Error loading url %s"  % url)
            return ''


