from datetime import datetime
import random
import pymysql
import db_configs as db
import websocket
import json

# making connection of pymysql to insert matches...
con = pymysql.connect(user=db.db_user,
                      host=db.db_host,
                      password=db.db_password,
                      database=db.db_name
                      )
cur = con.cursor()
cur.execute(f"CREATE DATABASE IF NOT EXISTS {db.db_name};")
cur.execute(f"USE {db.db_name};")

def insert_data(item):
    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {db.match} (
    match_id VARCHAR(50) UNIQUE,
    tour_id VARCHAR(50),
    match_name VARCHAR(100),
    league_id VARCHAR(100),
    team_1 VARCHAR(50),
    team_2 VARCHAR(50),
    tour_name VARCHAR(100),
    match_start_datetime VARCHAR(300)
        );
    """)
    try:
        cols = ", ".join(item.keys()).strip(', ')
        values = tuple(item.values())
        insert = f"""INSERT INTO {db.match} ({cols}) VALUES {values}"""
        cur.execute(insert)
        con.commit()
        print('inserted')
    except Exception as e:
        print(e)

# Define the WebSocket URL
ws_url = "wss://golobby-www.howzat.com/"

# Define the headers
ua = ['Dart/3.4 (dart:io)','Dart/3.3 (dart:io)','Dart/3.2 (dart:io)','Dart/3.1 (dart:io)','Dart/3.0 (dart:io)']
headers = {
    "Accept-Encoding": "gzip",
    "Cache-Control": "no-cache",
    "Connection": "Upgrade",
    "Cookie": "pids=s%3AzvhF61V_w1PFzWO0oq8InBqOOZDRaICF.jPSphX59ISHszNEkNmMNnAwyNIPrlpVKJfsdgAFROfo; Domain=howzat.com; Path=/; Expires=Wed, 05 Feb 2025 07:51:42 GMT; Secure; SameSite=None,__cf_bm=U3pkx2xXu12bxDMl_..OvPWScgJwWPveCORz5eYCk6Q-1723189902-1.0.1.1-cCj_RO6_PqKenDAVWOBy4DwjU2o8weLFB.Y9Z8tRsbkYeNL8NSvrOwFtf1gad_rX8R7CUqocE6.aREVS5MgPzw; path=/; expires=Fri, 09-Aug-24 08:21:42 GMT; domain=.howzat.com; HttpOnly; Secure; SameSite=None",
    "Host": "golobby-www.howzat.com",
    "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
    # "Sec-WebSocket-Key": "4aGLgEk8Oxmk/rytpxPFKQ==",
    "Sec-WebSocket-Version": "13",
    "Upgrade": "websocket",
    "User-Agent": random.choice(ua)
}


# Establish WebSocket connection
ws = websocket.create_connection(ws_url, header=headers)


def match_scraper(response):
    match_details = json.loads(response)
    for match_detail in match_details:
        data = dict()
        data['match_id'] = match_detail['matchId']
        data['tour_id'] = match_detail['series']['id']
        data['league_id'] = match_detail['leagueId']
        data['tour_name'] = match_detail['matchName']
        tms = match_detail['matchStartTime'] / 1000
        data['match_start_datetime'] = str(datetime.fromtimestamp(tms))# timestamp
        data['team_1'] = match_detail['teamA']['name']
        data['team_2'] = match_detail['teamB']['name']
        data['match_name'] = f"{data['team_1']} vs {data['team_2']}"
        insert_data(data)

def get_matches():
    try:
        json_object = {
            "iType": 35,
            "sportsId": 1
        }
        json_string = json.dumps(json_object)

        # Send JSON object to server
        ws.send(json_string)

        print("Sent to server:", json_string)

        # Continuously receive messages until an error occurs
        while True:
            response = json.loads(ws.recv())
            if "data" in response:
                if isinstance(response['data'], str) and 'matchId' in response['data']:
                    match_scraper(response=response['data'])
    except websocket._exceptions.WebSocketConnectionClosedException:
        print("Connection closed unexpectedly.")
    finally:
        # Ensure the WebSocket connection is properly closed
        ws.close()


if __name__ == '__main__':
    get_matches()