import pymongo


# connect to mongoClient with connection string
client = pymongo.MongoClient("");

# connect to the database
database = client.get_database('sample_restaurants')

# connect to the collection
collection= database.get_collection('restaurants')

# read documents from the collection
documents = collection.find().limit(10);

for document in documents:
    print(document)