import pymongo
import pandas as pd
import Genesis.DB_CONFIG as db

df = pd.read_excel("usa_locators.xlsx")

for index, row in df.iterrows():
    db.location.insert_one(row.to_dict())
    print("data inserted")
db.client.close()