import logging
from BeautifulSoup import BeautifulSoup

logger = logging.getLogger('mitiri')

class Parser(object):
    def __init__(self, db):
        self.db = db

    def parse(self, doc, source_id):
        """ Parse raw HTML response """
        rules = self._get_rule(source_id)
        return _doc_to_structure(rules, doc)

    def _doc_to_structure(self, rules, doc):
        ''' Rule to internal structure '''
        return None

    def _get_rule(self, source_id):
        rule = self.db.rules.find_one({"source_id": source_id})
        if not rule:
            raise Exception("Rule cannot be found for for source %s" %
                    source_id)
        return rule


