import pymysql
from fantasy_akhada.items import FaMatchItem, FaContestItem
import fantasy_akhada.DB_CONFIG as db

class FantasyAkhadaPipeline:
    def process_item(self, item, spider):
        con = db.con
        cursor = db.con.cursor()
        ovh_cur = db.ovh_con.cursor()
        if isinstance(item, FaMatchItem):
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {db.MATCH}(
                sport_id VARCHAR(5),
                main_tab_sport VARCHAR(30),
                match_id VARCHAR(300) UNIQUE,
                season_scheduled_date VARCHAR(300),
                tour_id VARCHAR(300),
                match_name VARCHAR(300),
                team_1 VARCHAR(200),
                team_2 VARCHAR(200),
                tour_name VARCHAR(300),
                match_start_datetime VARCHAR(300)
            );
            """)
            try:
                cols = ", ".join(item.keys()).strip(', ')
                values = tuple(item.values())
                insert = f"""INSERT INTO {db.MATCH} ({cols}) VALUES {values}"""
                cursor.execute(insert)
                con.commit()
                print('inserted')
            except Exception as e:
                print(e)
                self.logger.info(e)
                self.logger.debug(e)
                self.logger.error("from match insert pipeline----------------")

        if isinstance(item, FaContestItem):
            try:
                ovh_cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {db.CONTEST} (
                main_tab_sport VARCHAR(50),
                match_id VARCHAR(50),
                tour_id VARCHAR(50),
                match_name VARCHAR(100),
                team_1 VARCHAR(50),
                team_2 VARCHAR(50),
                tour_name VARCHAR(100),
                match_start_datetime VARCHAR(300),
                contest_description TEXT,
                record_time VARCHAR(200),
                match_format VARCHAR(50),
                tab VARCHAR(50),
                winner_percent VARCHAR(100),
                first_price VARCHAR(100),
                second_price VARCHAR(100),
                third_price VARCHAR(100),
                contest_id VARCHAR(100),
                entry_fee VARCHAR(10),
                max_spots VARCHAR(100),
                spots_filled VARCHAR(100),
                total_price_amount VARCHAR(1000),
                max_teams_per_user VARCHAR(100),
                contest_name VARCHAR(100),
                winner VARCHAR(100),
                contest_guarantee VARCHAR(100)
            );
                """)
                cols = ", ".join(item.keys()).strip(', ')
                values = tuple(item.values())
                insert = f"""INSERT INTO {db.CONTEST} ({cols}) VALUES {values}"""
                ovh_cur.execute(insert)
                db.ovh_con.commit()
                print('inserted')
            except Exception as e:
                print(e)
                self.logger.info(e)
                self.logger.debug(e)
                self.logger.error("from contest pipeline----------------")
        return item
