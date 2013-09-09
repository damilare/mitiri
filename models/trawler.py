from datetime import datetime
from loader import Loader
from parser import Parser

class Trawler(object):
    def __init__(self, db):
        self.db = db
        self.loader = Loader()
        self.parser = Parser(db)
        self.sources = self.load_sources()

    def load_sources(self):
        ''' Load sources from DB '''
        # think about an algorithm
        # for getting appropriate source
        return self.db.sources.find({'has_rules': True})

    def trawl_url(self, url, rules=None, source_id=None):
        doc = self.loader.load(url)
        return self.parser.parse(doc, source_id, rules=rules) 

    def trawl(self):
        ''' Get a source, and parser into appropriate format '''
        for src in self.sources:
            doc = self.loader.load(src['url'])
            entries = self.parser.parse(doc, source_id=src['_id'])
            for entry in entries:
                db.entries.insert({
                    'source_id': src['_id'],
                    'entry': entry,
                    'date_created': datetime.now()})


if __name__ == '__main__':
    Trawler(db).trawl_all()

