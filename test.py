from src.database import Database

Database.initialize()

for i in Database.find_one (collection='blogs',query={'blog_id':'11db4a43529f424ea1dba0b8b2b90df7'}):
    print(i)













'''
import pymongo
URI = "mongodb://127.0.0.1:27017"
client=pymongo.MongoClient(URI)
database=client['fullstack']
collection=database['test']
collection.insert({'name':'vishnuvijay'})
#print (collection.find())
student=collection.find({})
print (student)
for i in student:
    print(i)

'''