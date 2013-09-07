import csv, sys
from app import db
from models.trawler import Trawler

def reload_data(db):
    db.
    for i, url in enumerate(csv.reader(open('models/sources/urls.csv'))):
        if i == 0:
            continue
        db.sources.insert({'url': url[0], 
            'tags': url[1].split(','), 
            'domain': url[2],
            'weight': 1,
            'has_rule': False
            })

def trawl_sources(db):
    Trawler(db).trawl()

if __name__ == '__main__':
    if sys.argv[1] == 'trawl':
        trawl_sources(db)
    elif sys.argv[1] == 'reload':
        reload_data(db)
    else:
        print 'Supply correct arg fool!'


