from pymongo import MongoClient

user = 'user'
pwd = 'user'
auth_db = 'admin'
host = 'a.b.c.d'
port = 5022

uri = "mongodb://{}:{}@{}/{}?authMechanism=SCRAM-SHA-1".format(user,
                                                               pwd,
                                                               ':'.join([host, str(port)]),
                                                               auth_db)
# Get mongo connection
con=MongoClient(host=uri)

# Select the database to be accessed
db=con['test']

# Do database operations using db object

print 'Number of documents in collection are {}'.format(db.any_collection.count())

docs = db.any_collection.find({},{'_id':1, 'name':1}).limit(5)

for cell in docs:
    print cell['name']
