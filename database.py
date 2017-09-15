import pymongo
class Database(object):
    URI="mongodb://127.0.0.1:27017"
    DATABASE=None

    @staticmethod
    def initialize():
      client=pymongo.MongoClient(Database.URI)
      Database.DATABASE=client['fullstack']
      #collections=['posts']

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection,query):
        return Database.DATABASE[collection].find(query)
         #return Database.DATABASE['posts'].find({'blog_id':'8758a22c58a54749a93c61c424a45c72'})

    @staticmethod
    def find_one(collection,query):
       return  Database.DATABASE[collection].find_one(query)