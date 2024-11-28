# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import verizon.DB_config as db
from verizon.items import VerizonItem, VerizonPdp
import pymysql


class VerizonPipeline:
    def process_item(self, item, spider):
        con = pymysql.connect(user=db.USER, host=db.HOST, password=db.PASSWORD, database=db.DATABASE)
        cur = con.cursor()
        if isinstance(item, VerizonPdp):
            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {db.LINKDATA} (
            store_no VARCHAR(300) UNIQUE,
            name VARCHAR(355),
            url TEXT,
            `status` VARCHAR(100) DEFAULT 'pending'
            );
                        """)
            try:
                cols = ", ".join(item.keys()).strip(', ')
                values = tuple(item.values())
                insert = f"""INSERT INTO {db.LINKDATA} ({cols}) VALUES {values}"""
                cur.execute(insert)
                con.commit()
                print("Inserted")
            except Exception as e:
                print(e)

        if isinstance(item, VerizonItem):
            cur.execute(
                f"""
            CREATE TABLE IF NOT EXISTS {db.DATATABLE} (
            store_no VARCHAR(355) UNIQUE,
            name  VARCHAR(300),
            longitude  VARCHAR(300),
            latitude  VARCHAR(300),
            street  VARCHAR(355),
            city  VARCHAR(100),
            state  VARCHAR(20),
            zip_code  VARCHAR(50),
            county  VARCHAR(300),
            country  VARCHAR(100),
            open_hours  TEXT,
            phone_number  VARCHAR(300),
            status  VARCHAR(50),
            url  TEXT,
            provider  VARCHAR(100),
            category  VARCHAR(100),
            updated_date  VARCHAR(100),
            direction_url  TEXT
            );
            """)
        try:
            cols = ", ".join(item.keys()).strip(', ')
            values = tuple(item.values())
            insert = f"""INSERT INTO {db.DATATABLE} ({cols}) VALUES {values}"""
            cur.execute(insert)
            con.commit()
            print("Inserted")
        except Exception as e:
            print(e)
        return item
