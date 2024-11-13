from pymongo import MongoClient
from random import randint

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["demo"]
collection = db["testing"]

# Create 100 sample documents
records = []
for i in range(100):
    record = {
        "name": f"Name_{i}",
        "age": randint(18, 60),
        "email": f"user{i}@example.com",
        "address": {
            "street": f"Street {i}",
            "city": f"City_{randint(1, 10)}",
            "zipcode": f"{10000 + i}"
        },
        "active": bool(i % 2)  # Example field to alternate between True and False
    }
    records.append(record)

# Insert records into the collection
result = collection.insert_many(records)
print("Inserted IDs:", result.inserted_ids)
