import pymysql
from datetime import datetime, timedelta
import db_configs as db
from slack_sdk import WebClient


client = WebClient(token=db.slack_app_token)
channel = db.channel_id
# making general variables from db_config file...
db_name = db.db_name
user = db.db_user
host = db.db_host
passs = db.db_password
match =  db.match
con = pymysql.connect(user=user,
                      host=host,
                      password=passs,
                      database=db_name
                      )
cur = con.cursor()

last_sql_match_table_updated_time = f"""
SELECT UPDATE_TIME
FROM   information_schema.tables
WHERE  TABLE_SCHEMA = '{db_name}'
   AND TABLE_NAME = '{match}'
"""

cur.execute(last_sql_match_table_updated_time)
result = cur.fetchone()
try:
    one_record = result[0]
    if result and one_record:
        time_difference = datetime.now() - one_record
        if time_difference > timedelta(hours=3): # here timedelta will compare time_diff... "seconds" with 10800(3 hour)...
            client.chat_postMessage(
                channel=channel,
                text=f"Database: {db_name} | Table: {match} [ not updated more than 3 hours.]",
            )
except Exception as e:
    client.chat_postMessage(
        channel=channel,
        text=f"Error [{db_name}] in Except Block: {e}",
    )