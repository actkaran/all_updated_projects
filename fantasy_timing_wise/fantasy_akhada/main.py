import json
import subprocess
import time
import pymysql.cursors
from datetime import datetime, timedelta
from openpyxl import Workbook
import fantasy_akhada.DB_CONFIG as db
import logging

# Configure logging
log_file_name = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
logging.basicConfig(
    filename=f"logs\main_file_{log_file_name}.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
while True:
    # Establish a connection to the database
    con = pymysql.connect(user=db.DB_USER, host=db.DB_HOST, password=db.DB_PASS, database=db.DB_NAME,
                          cursorclass=pymysql.cursors.DictCursor
                          )


    try:
        # Current time
        now = datetime.now()

        # Define time frames as tuples of (start hours, start minutes, end hours, end minutes, description)
        time_frames = [
            (23, 0, 23, 0, "23H"),
            (10, 0, 10, 0, "10H"),
            (3, 0, 3, 0, "3H"),
            (1, 0, 1, 0, "1H"),
            (0, 30, 0, 30, "30M"),
            (0, 15, 0, 15, "15M"),
            (0, 5, 0, 5, "5M"),
            (0, 1, 0, 1, "1M")
        ]
        # Create a new cursor
        with con.cursor() as cursor:
            for start_hour, start_min, end_hour, end_min, description in time_frames:
                # Calculate the start and end of the time range

                start_time = now + timedelta(hours=start_hour, minutes=start_min)
                end_time = now + timedelta(hours=end_hour, minutes=end_min)

                # Convert datetime to string format suitable for SQL query
                cutoff_start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
                cutoff_end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
                print(cutoff_end_time_str)

                # Write your query
                sql = f"""
                       SELECT * FROM {db.MATCH}
                       WHERE STR_TO_DATE(match_start_datetime, '%%Y-%%m-%%d %%H:%%i:%%s') BETWEEN %s AND %s
                       """
                # Execute the query
                cursor.execute(sql, (cutoff_end_time_str, cutoff_start_time_str))
                results = cursor.fetchall()
                # print(results)
                if results:
                    print("match founded...")
                    print(results)
                    if description == '1M':
                        logging.error(f"Before 1M Match found: {results}")
                        subprocess.run([
                            'python', '-m', 'scrapy', 'crawl', 'contests_fa',
                            '-a', f'time_frame={description}',
                            '-a', f'matches={json.dumps(results)}'
                        ])
                        time.sleep(45)
                        subprocess.run([
                            'python', '-m', 'scrapy', 'crawl', 'contests_fa',
                            '-a', f'time_frame=15S',
                            '-a', f'matches={json.dumps(results)}'
                        ])
                    else:
                        logging.error(f"Match found: {results}")
                        subprocess.run([
                            'python', '-m', 'scrapy', 'crawl', 'contests_fa',
                            '-a', f'time_frame={description}',
                            '-a', f'matches={json.dumps(results)}'
                        ])
    except Exception as e:
        print(e)
        logging.error(f"Error: {e}")