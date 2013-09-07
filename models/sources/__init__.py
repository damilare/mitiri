import csv
from app import db

def load_data(db):
    for url in csv.reader(open('urls.csv')):
        db.sources.insert({'url': url[0], 
            'tags': url[1].split(','), 
            'domain': url[2],
            'weight': 1})

if __name__ == '__main__':
    load_data(db)
