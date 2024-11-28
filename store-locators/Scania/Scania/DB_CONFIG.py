import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# database
scania_database = client["scania_locators_data"]