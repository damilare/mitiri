import logging
from app import db
from BeautifulSoup import BeautifulSoup

logger = logging.getLogger('mitiri')

class Parser(object):
    def __init__(self, source_id):
        self.source_id = source_id

    def parse(doc):
        """ Parse raw HTML response """
        rules = self._get_rule(source_id)
        return _doc_to_structure(rules, doc)

    def _doc_to_structure(rules, doc):
        ''' Rule to internal structure '''
        return None

    def _get_rule(source_id)
        rule = db.source.find_one({"_id": source_id})
        if not rule:
            raise Exception("Rule cannot be found for for source %s" %
                    source_id)
        return rule


