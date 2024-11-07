import gzip
import os
from datetime import datetime
import scrapy
import pandas as pd
from scrapy import Spider
from scrapy.cmdline import execute
import json
import fantasy_akhada.DB_CONFIG as db
from fantasy_akhada.items import FaContestItem


class FaContestScrap(scrapy.Spider):
    name = 'contests_fa'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/json',
        'Host': 'f.fantasyakhada.com',
        'sessionkey': 'bc1e58380c3345d3ec0781816e4266f1',
        'User-Agent': 'okhttp/4.9.2'
    }

    def __init__(self, time_frame=None, matches=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time_frame = time_frame
        self.matches = matches

    def start_requests(self):
        results = json.loads(self.matches)
        # scraped_data = list()
        payload = json.dumps({
                    "collection_master_id": results[0]["match_id"],
                    "sports_id": results[0]["sport_id"]
                })
        s_url = "https://f.fantasyakhada.com/fantasy/lobby/get_fixture_contest"

        yield scrapy.Request(method='POST',
                             url=s_url,
                             body=payload,
                             headers=self.headers,
                             cb_kwargs={'match_info': results},
                             callback=self.parse2)
#             # break

    def parse2(self, response, **kwargs):
        try:
            jd = json.loads(response.text)
            match_info = kwargs["match_info"]
            k = FaContestItem()
            k["main_tab_sport"] = match_info[0]["main_tab_sport"]
            k["match_id"] = match_info[0]["match_id"]
            k["tour_id"] = match_info[0]["tour_id"]
            k["match_name"] = match_info[0]["match_name"]
            k["team_1"] = match_info[0]["team_1"]
            k["team_2"] = match_info[0]["team_2"]
            k["tour_name"] = match_info[0]["tour_name"]
            k["match_start_datetime"] = match_info[0]["match_start_datetime"]
            for x in jd["data"]["contest"]:
                k["contest_description"] = x["description"]
                if x["contest_list"]:
                    for a in x["contest_list"]:
                        k["record_time"] = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        k["match_format"] = "NA"
                        k["tab"] = "NA"
                        k["winner_percent"] = "NA"
                        k["first_price"] = int((a["prize_distibution_detail"][0]["max_value"]).strip('.00')) if not None else None
                        k["second_price"] = "NA"
                        k["third_price"] = "NA"
                        k["contest_id"] = a["contest_id"]
                        k["entry_fee"] = a["entry_fee"]
                        k["max_spots"] = a["size"]
                        k["spots_filled"] = a["total_user_joined"]
                        k["total_price_amount"] = a["prize_pool"]
                        k["max_teams_per_user"] = a["multiple_lineup"]
                        k["contest_name"] = a["contest_title"]
                        k["winner"] = a["prize_distibution_detail"][0]["min"]
                        k["contest_guarantee"] = "Guarantee" if a["guaranteed_prize"] == "2" else "NA"
                        yield k
        except Exception as e:
            self.logger.info(e)
            self.logger.debug(e)
            self.logger.error("from contest----------------")
if __name__ == "__main__":
    execute(f'scrapy crawl {FaContestScrap.name}'.split())