from app import db
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
        return self.db.sources.find()

    def trawl(self):
        ''' Get a source, and parser into appropriate format '''
        for src in self.sources:
            doc = self.loader.load(src['url'])
            entry = self.parser.parse(doc, source_id=src['_id'])
            db.entry.insert(entry)


if __name__ == '__main__':
    Trawler(db).trawl()

