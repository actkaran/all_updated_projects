# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import tiffany.db_config as db
from tiffany.items import TiffanyItem, TiffanyData


class TiffanyPipeline:
    db.cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {db.db_link_table} (
        `id` INT PRIMARY KEY AUTO_INCREMENT,
         url VARCHAR(555),
         sku VARCHAR(300),
         hash_url VARCHAR(400) UNIQUE,
        `status` VARCHAR(100) DEFAULT 'pending'
        );
    ''')

    db.cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {db.db_data_table} (
        store_no VARCHAR(255),
        name VARCHAR(355),
        latitude VARCHAR(255),
        longitude VARCHAR(255),
        street VARCHAR(455),
        city VARCHAR(355),
        state VARCHAR(255),
        zip_code VARCHAR(50),
        county VARCHAR(255),
        phone VARCHAR(100),
        open_hours TEXT,
        url VARCHAR(555),
        provider VARCHAR(255),
        category VARCHAR(100),
        updated_date VARCHAR(300),
        country VARCHAR(255),
        `status` VARCHAR(100),
        direction_url VARCHAR(555),
        hash_url VARCHAR(555) UNIQUE
        );

''')

    def process_item(self, item, spider):
        if isinstance(item, TiffanyItem):
            cols = ", ".join(item.keys()).strip(', ')
            values = tuple(item.values())
            insert = f"""INSERT INTO {db.db_link_table} ({cols}) VALUES {values}"""
            db.cur.execute(insert)
            db.con.commit()
            print("Inserted...", item["url"])

        if isinstance(item, TiffanyData):
            try:
                cols = ", ".join(item.keys()).strip(', ')
                values = tuple(item.values())
                insert = f"""INSERT INTO {db.db_data_table} ({cols}) VALUES {values}"""
                db.cur.execute(insert)
                db.con.commit()
                print("Inserted...", item["hash_url"])
                db.cur.execute(f"UPDATE {db.db_link_table} SET status='Done' WHERE hash_url=%s", (item["hash_url"],))
                db.con.commit()
            except Exception as e:
                print(e)

        return item
