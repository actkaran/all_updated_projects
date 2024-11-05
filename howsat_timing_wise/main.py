import json, time, subprocess, pymysql.cursors
from datetime import datetime, timedelta
import db_configs as db

while True:
    # Establish a connection to the database
    con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name,
                          cursorclass=pymysql.cursors.DictCursor)

    try:
        # Current time
        now = datetime.now()

        # Define time frames as tuples of (start hours, start minutes, end hours, end minutes, description)
        time_frames = [
            (23, 0, 23, 0, "23H"),
            (3, 0, 3, 0, "3H"),
            (1, 0, 1, 0, "1H"),
            (0, 45, 0, 45, "45M"),
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

                # cutoff_start_time_str = '2024-11-05 19:15:00'
                # cutoff_end_time_str = '2024-11-05 19:15:00'
                print(cutoff_end_time_str)
                # Write your query
                sql = f"""
                       SELECT * FROM {db.match}
                       WHERE STR_TO_DATE(match_start_datetime, '%%Y-%%m-%%d %%H:%%i:%%s') BETWEEN %s AND %s
                       """

                # Execute the query
                cursor.execute(sql, (cutoff_end_time_str, cutoff_start_time_str))
                results = cursor.fetchall()
                if results:
                    if description == '1M':
                        print("scraperrrrrrrrrrrr calling")
                        subprocess.run([
                            "python", "-m", "contests", json.dumps(results[0]), description
                        ])
                        time.sleep(45)
                        subprocess.run([
                            "python", "-m", "contests", json.dumps(results[0]), '15S'
                        ])
                    else:
                        print("scraperrrrrrrrrrrr calling")
                        subprocess.run([
                          "python", "-m", "contests", json.dumps(results[0]), description
                        ])
                    cursor.execute(f'DELETE FROM {db.contest}')
                    con.commit()


    except Exception as e:
        print(e)