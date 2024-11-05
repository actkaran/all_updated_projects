import pymysql
from itemadapter import ItemAdapter
import myteam11_bot.DB_CONFIG as db
from myteam11_bot.items import MatchData, ContestsData


class Myteam11BotPipeline:
    def process_item(self, item, spider):

        cursor = db.con.cursor()
        ovh_cur = db.ovh_con.cursor()
        if isinstance(item, MatchData):
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {db.MATCH}(
                match_id VARCHAR(200) UNIQUE,
                main_tab_sport VARCHAR(100),
                team_1 VARCHAR(100),
                team_2 VARCHAR(100),
                match_start_datetime VARCHAR(255),
                match_format VARCHAR(200),
                tour_name VARCHAR(300)
            );
            """)
            try:
                cols = ", ".join(item.keys()).strip(', ')
                values = tuple(item.values())
                insert = f"""INSERT INTO {db.MATCH} ({cols}) VALUES {values}"""
                cursor.execute(insert)
                db.con.commit()
                print('inserted')
            except Exception as e:
                print(e)

        if isinstance(item, ContestsData):
            ovh_cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {db.CONTEST} (
            record_time VARCHAR(300),
            main_tab_sport VARCHAR(50),
            tour_id VARCHAR(50),
            tour_name VARCHAR(100),
            match_id VARCHAR(50),
            match_name VARCHAR(100),
            match_start_datetime VARCHAR(300),
            match_format VARCHAR(50),
            team_1 VARCHAR(100),
            team_2 VARCHAR(100),
            tab VARCHAR(100),
            contest_name VARCHAR(100),
            contest_description TEXT,
            contest_id VARCHAR(100),
            total_price_amount VARCHAR(1000),
            entry_fee VARCHAR(200),
            max_spots VARCHAR(100),
            spots_filled VARCHAR(200),
            winner_percent VARCHAR(100),
            winner VARCHAR(200),
            contest_guarantee VARCHAR(100),
            first_priZe VARCHAR(100),
            second_prize VARCHAR(100),
            third_prize VARCHAR(100),
            max_teams_per_user VARCHAR(200)   
        );
            """)

            try:
                cols = ", ".join(item.keys()).strip(', ')
                values = tuple(item.values())
                insert = f"""INSERT INTO {db.CONTEST} ({cols}) VALUES {values}"""
                ovh_cur.execute(insert)
                db.ovh_con.commit()
                print('inserted')
            except Exception as e:
                print(e)

        return item
