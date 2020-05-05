import os

from pymongo import MongoClient

client = MongoClient(os.environ['DATABASE_URI'])
db = client[os.environ['DATABASE']]
books_coll = db.books
