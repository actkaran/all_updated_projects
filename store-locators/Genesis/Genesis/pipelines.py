# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from Genesis.items import GenesisItem
import pymongo
import Genesis.DB_CONFIG as db


class GenesisPipeline:

    def process_item(self, item, spider):
        if isinstance(item, GenesisItem):
            temp = item["db_zip"]
            try:
                item.pop("db_zip")
                db.data_table.insert_one(dict(item))
                print("Inserted")

                # Update one document where status is 'pending'
                db.location.update_one(
                    {"zipcode": temp},  # Filter criteria
                    {"$set": {"status": "Done"}}  # Update operation
                        )
                print("Done status")
            except Exception as e:
                # Update one document where status is 'pending'
                db.location.update_one(
                    {"zipcode": temp},  # Filter criteria
                    {"$set": {"status": "pending"}}  # Update operation
                )
                print(e)

        return item
