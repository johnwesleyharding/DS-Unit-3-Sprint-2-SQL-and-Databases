# mongodb password (admin): q2iN90nL5l0c9Zp8

import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:q2iN90nL5l0c9Zp8@cluster0-wvshc.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db

# dir(db.test)

# help(db.test.insert_one)

# # insert a document
# db.test.insert_one({'x':1})

# dir(cursor)

