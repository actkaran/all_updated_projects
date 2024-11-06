# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import metro_canada.db_config as db
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from metro_canada.items import MetroLinks, MetroCanadaItem


class MetroCanadaPipeline:
    con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)
    cur = con.cursor()

    def process_item(self, item, spider):
        if isinstance(item, MetroLinks):
            self.cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {db.db_link_table} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    url VARCHAR(555),
                    status VARCHAR(100) DEFAULT 'pending');
                """)

            try:
                # cols = ", ".join(item.keys()).strip(', ')
                # values = tuple(item.values())
                # insert = f"""INSERT INTO {db.db_link_table} ({cols}) VALUES {values}"""
                insert = f"INSERT INTO {db.db_link_table} (url) VALUES(%s);"
                self.cur.execute(insert, (item["url"]))
                self.con.commit()
                print("Inserted....")
            except pymysql.err.IntegrityError:
                print("Duplicate...")
            except Exception as e:
                print(e)
        if isinstance(item, MetroCanadaItem):
            self.cur.execute(f"""
                    CREATE TABLE IF NOT EXISTS {db.db_data_table} (
                    product_url VARCHAR(555),
                    category VARCHAR(300),
                    product_name VARCHAR(400),
                    product_number VARCHAR(200) UNIQUE,
                    mrp VARCHAR(100),
                    price VARCHAR(100),
                    currency VARCHAR(10),
                    serving_for_people VARCHAR(200),
                    quantity VARCHAR(150),
                    price_per_unit VARCHAR(100),
                    product_image VARCHAR(300),
                    product_description TEXT,
                    ingredients TEXT,
                    valid_date VARCHAR(200)
                    );""")
            try:
                temp_id = item["o_id"]
                del item["o_id"]
                cols = ", ".join(item.keys()).strip(', ')
                values = tuple(item.values())
                insert = f"""INSERT INTO {db.db_data_table} ({cols}) VALUES {values}"""
                self.cur.execute(insert)
                self.con.commit()
                print("Inserted....")
                update = f"""UPDATE {db.db_link_table} SET status='Done' WHERE id=%s"""
                self.cur.execute(update, (temp_id,))
                self.con.commit()
            except pymysql.err.IntegrityError:
                print("Duplicate...")
            except Exception as e:
                print(e)

        return item
