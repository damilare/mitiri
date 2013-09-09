import logging
from BeautifulSoup import BeautifulSoup, Tag

logger = logging.getLogger('mitiri')

class Parser(object):
    def __init__(self, db):
        self.db = db

    def parse(self, doc, source_id=None, rules=None):
        """ Parse raw HTML response """
        if not rules and source_id:
            rules = self._get_rule(source_id)
        if rules:
            return self._doc_to_structure(rules, doc)

    def _parse_link(self, link):
	""" extract url from link returns a pair """
	if isinstance(link, Tag) and link.name == 'a':
            return (link.get('href', None), getattr(link, 'text', None))

    def _doc_to_structure(self, rules, doc):
        ''' Rule to internal structure '''
        soup = BeautifulSoup(doc)
        dish = soup.find(rules['elem'], {"class": rules['class']})
        links = filter(lambda x: getattr(x, 'name', None) == 'a', dish)
        return map(self._parse_link, links)

    def _get_rule(self, source_id):
        rule = self.db.rules.find_one({"source_id": source_id})
        if not rule:
            raise Exception("Rule cannot be found for for source %s" %
                    source_id)
        return rule


