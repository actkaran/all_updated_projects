from itemadapter import ItemAdapter
from mountains_khakis.items import MountainsKhakisItem
import pymysql
import mountains_khakis.db_config as db
class MountainsKhakisPipeline:
    con = pymysql.connect(user=db.user, host=db.host, password=db.password, database=db.datab)
    cur = con.cursor()

    def process_item(self, item, spider):
        if isinstance(item, MountainsKhakisItem):
            self.cur.execute(
                f"""
                        CREATE TABLE IF NOT EXISTS {db.data} (
                        store_no VARCHAR(355),
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
                insert = f"""INSERT INTO {db.data} ({cols}) VALUES {values}"""
                self.cur.execute(insert)
                self.con.commit()
                print("Inserted")
            except Exception as e:
                print(e)
        return item
