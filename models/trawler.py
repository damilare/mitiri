from app import db
from loader import Loader
from parser import Parser

class Trawler(object)
    def __init__(self):
        self.loader = Loader()
        self.parser = Parser()
        sources = self.load_sources()
        self.trawl(sources)

    def load_sources(self):
        ''' Load sources from DB '''
        # think about an algorithm
        # for getting appropriate source
        return db.sources.find()

    def trawl(source):
        ''' Get a source, and parser into appropriate format '''
        for url, source_id in sources:
            doc = self.loader(url)
            entry = parser.parser(doc, source_id)
            db.entry.insert(entry)

