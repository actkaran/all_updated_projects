import os
from datetime import datetime
import pandas
import db_configs as db
import pymysql.cursors
import websocket, json, sys, random, logging


# Configure logging
log_file_name = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
logging.basicConfig(
    filename=f"logs\contest_log_{log_file_name}.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define the WebSocket URL
ws_url = "wss://golobby-www.howzat.com/"
# -------
# Define the headers
ua = ['Dart/3.5 (dart:io)', 'Dart/3.4 (dart:io)', 'Dart/3.3 (dart:io)', 'Dart/3.2 (dart:io)', 'Dart/3.1 (dart:io)',
      'Dart/3.0 (dart:io)']
headers = {
    "Accept-Encoding": "gzip",
    "Cache-Control": "no-cache",
    "Connection": "Upgrade",
    "Cookie": "pids=s%3AnExG8SwV_2npToltIXhIENnCpuT03nBD.DIX8yxqGge79RwIK0HOsHPV7cX9MwA%2BLwnwHyNcLxWc; Domain=howzat.com; Path=/; Expires=Tue, 25 Feb 2025 08:07:50 GMT; Secure; SameSite=None,__cf_bm=5QViftfa4Ik077sgm2Cea4MwNV9Eeexc5A_iSqs6cQU-1724918870-1.0.1.1-BGIzBgOEe0wYN3Kg8IXSBYM_7JCmnbZt0lV0vLxX6xvXq9YdW1QbzikcOrEg2RpGOpD2a3fMYqK2SgWwO0t.4A; path=/; expires=Thu, 29-Aug-24 08:37:50 GMT; domain=.howzat.com; HttpOnly; Secure; SameSite=None",
    "Host": "golobby-www.howzat.com",
    "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
    # "Sec-WebSocket-Key": "4aGLgEk8Oxmk/rytpxPFKQ==",
    "Sec-WebSocket-Version": "13",
    "Upgrade": "websocket",
    "User-Agent": random.choice(ua)
}

ws = websocket.create_connection(ws_url, header=headers)


def match_data_scraper(response, metadata):
    try:
        response = json.loads(response)
        if response['data']['l1']['contests']:
            for contest_info in response['data']['l1']['contests']:
                metadata['contest_id'] = contest_info['id']
                metadata['contest_name'] = contest_info["brand"]["info"]
                metadata['total_prize_amount'] = contest_info['prizeDetails'][0]['totalPrizeAmount']
                metadata['entry_fee'] = contest_info['entryFee']
                metadata['max_spots'] = contest_info['size']
                metadata['total_spots_filled'] = contest_info['joined']
                metadata['winner'] = contest_info['prizeDetails'][0]['noOfPrizes']
                metadata['winner_percent'] = round((metadata['winner'] / metadata['max_spots']) * 100, 2)
                metadata['first_prize'] = contest_info['prizeDetails'][0]['firstPrizeAmt']
                if metadata["first_prize"] == 0:
                    metadata["first_prize"] = contest_info["whiteGoodsInfo"][0]["brand"]
                metadata['max_teams_per_user'] = contest_info['teamsAllowed']
                metadata['record_time'] = str(datetime.now())
                metadata['match_format'] = 'N/A'
                metadata['contest_guarantee'] = 0 if contest_info["guaranteed"] == False else 1
                metadata['tab'] = 'N/A'
                metadata['main_tab_sport'] = 'N/A'
                # print(metadata)
                insert_data(metadata)
        if response['data']['l1']['template']:
            for contest_info2 in response['data']['l1']['template']:
                metadata['contest_id'] = contest_info2['id']
                metadata['contest_name'] = contest_info2["brand"]["info"]
                metadata['total_prize_amount'] = contest_info2['prizeDetails'][0]['totalPrizeAmount']
                metadata['entry_fee'] = contest_info2['entryFee']
                metadata['max_spots'] = contest_info2['size']
                metadata['total_spots_filled'] = contest_info2['joined']
                metadata['winner'] = contest_info2['prizeDetails'][0]['noOfPrizes']
                metadata['winner_percent'] = round((metadata['winner'] / metadata['max_spots']) * 100, 2)
                metadata["first_prize"] = "N/A"
                metadata["second_price"] = "N/A"
                metadata["third_price"] = "N/A"
                if contest_info2["prizeStructures"]:
                    for abc in contest_info2["prizeStructures"]:
                        if abc["tranch"] == 1:
                            metadata['first_prize'] = abc["amount"]
                        if abc["tranch"] == 2:
                            metadata['second_price'] = abc["amount"]
                        if abc["tranch"] == 3:
                            metadata['third_price'] = abc["amount"]
                metadata['max_teams_per_user'] = contest_info2['teamsAllowed']
                metadata['record_time'] = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                metadata['match_format'] = 'N/A'
                metadata['contest_guarantee'] = 0 if contest_info2["guaranteed"] == False else 1
                metadata['tab'] = 'N/A'
                metadata['main_tab_sport'] = 'N/A'
                # print(metadata)
                # I made the function separate to insert the data of metadata
                insert_data(metadata)
    except Exception as e:
        logging.error(f"scrape function Error: {e}")


def match_details_request(metadata):
    try:
        m_id = metadata['league_id']
        # Prepare JSON object
        json_object = {
            "iType": 19,
            "id": int(m_id),
            "withPrediction": False,
            "sportsId": 1,
            "fantasyTemplateId": 0,
            "is_innings": True,
            "subscribe": True,
            "withContestPersonalization": True
        }
        json_string = json.dumps(json_object)

        # Send JSON object to server
        ws.send(json_string)

        print("Sent to server:", json_string)

        # Continuously receive messages until an error occurs
        while True:
            response = ws.recv()
            print("Response from server:", response)
            if '{"bReady": 1}' in response:
                pass
            else:
                if 'brandLogoUrl' in response:
                    match_data_scraper(response, metadata)
                    ws.close()
    except websocket._exceptions.WebSocketConnectionClosedException:
        print("Connection closed unexpectedly.")


# custom functions...........
def insert_data(item):
    db.ovh_cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {db.contest} (
    main_tab_sport VARCHAR(50),
    match_id VARCHAR(50),
    tour_id VARCHAR(50),
    match_name VARCHAR(100),
    league_id VARCHAR(100),
    team_1 VARCHAR(50),
    team_2 VARCHAR(50),
    tour_name VARCHAR(100),
    match_start_datetime VARCHAR(300),
    contest_description TEXT,
    record_time VARCHAR(200),
    match_format VARCHAR(50),
    tab VARCHAR(100),
    winner_percent VARCHAR(100),
    first_prize VARCHAR(100),
    second_price VARCHAR(100),
    third_price VARCHAR(100),
    contest_id VARCHAR(100),
    entry_fee VARCHAR(10),
    max_spots INT,
    total_spots_filled INT,
    total_prize_amount VARCHAR(1000),
    max_teams_per_user INT,
    contest_name VARCHAR(100),
    winner VARCHAR(100),
    minimum_size VARCHAR(300),
    contest_guarantee VARCHAR(100)
    );
    """)
    try:
        cols = ", ".join(item.keys()).strip(', ')
        values = tuple(item.values())
        insert = f"""INSERT INTO {db.contest} ({cols}) VALUES {values}"""
        db.ovh_cur.execute(insert)
        db.ovh_con.commit()
        print('inserted')
        logging.error(f"contest Inserted...{item['contest_id']}")
    except Exception as e:
        print(e)
        logging.error(f"Failed to insert: {item['contest_id']}. Error: {e}")






if __name__ == "__main__":

    data = json.loads(sys.argv[1])
    time_frame = sys.argv[2]

    # calling contest scraper function...
    match_details_request(data)