import gzip
import json
import os.path
from datetime import datetime
import scrapy
from scrapy import Spider
from scrapy.cmdline import execute
import pandas as pd
from myteam11_bot.items import ContestsData
import myteam11_bot.DB_CONFIG as db


class Myteam11Contest(scrapy.Spider):
    name = 'myteam11_contests'

    contest_headers = {
        "Accept-Encoding": "gzip",
                    "AppType": "1",
                    "AppVersion": "117",
                    "AuthExpire": "4d253275-b349-4dad-bb6d-66ae7a7140df",
                    "campaignId": "",
                    "Connection": "Keep-Alive",
                    "DeviceName": "SM-G965N",
                    "DeviceOS": "Android",
                    "ExpireToken": "70012760-5332-4fbe-ba0a-214e29ef830a",
                    "Host": "gameplay.myteam11.com",
                    "IsPlayStore": "1",
                    "User-Agent": "okhttp/4.9.1",
                    "UserId": "18831232"
    }

    def __init__(self, time_frame=None, matches=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time_frame = time_frame
        self.matches = matches

    def start_requests(self):
        results = json.loads(self.matches)
        self.contest_headers['matchID'] = results[0]['match_id']
        ta_dic = {
            '1': 'MEGA CONTEST',
            '2': 'HOT CONTEST',
            '3': 'CONTEST FOR CHAMPION',
            '4': 'HEAD TO HEAD',
            '5': 'WINNER TAKES ALL',
            '6': 'MORE CONTESTS',
            '7': 'PRACTICE CONTEST',
            '12': '4X WINNINGS',
            '15': '10X WINNINGS',
        }
        for x in ta_dic:
            yield scrapy.Request(
                url=f"https://gameplay.myteam11.com/league/v1/category/list/{results[0]['match_id']}/{x}",
                headers=self.contest_headers,
                callback=self.contest_parse,
                dont_filter=True,
                cb_kwargs={
                    'match_info': results,
                    'tab': ta_dic[x]
                }
            )

    def contest_parse(self, response, **kwargs):
        data = json.loads(response.text)
        cf = ContestsData()
        match_info = kwargs["match_info"]
        cf['match_id'] = match_info[0]['match_id']
        cf['main_tab_sport'] = match_info[0]['main_tab_sport']
        cf['team_1'] = match_info[0]['team_1']
        cf['team_2'] = match_info[0]['team_2']
        cf['match_format'] = match_info[0]['match_format']
        cf['match_start_datetime'] = match_info[0]['match_start_datetime']
        cf['tour_name'] = match_info[0]['tour_name']
        cf['tab'] = kwargs["tab"]
        for t in data['data']['categories']:
            cf['max_teams_per_user'] = data["data"]["maxTeams"]
            cf['contest_id'] = t['id']
            cf['entry_fee'] = round(t['fees'])
            cf['contest_guarantee'] = "Guaranteed" if t['isGuaranteed'] else "NA"
            cf['max_spots'] = t["noofMembers"]
            cf['spots_filled'] = t['totalJoined']
            cf['winner'] = t["noofWinners"]
            cf['total_price_amount'] = round(t['winAmount'])
            cf['contest_description'] = 'NA'
            cf["winner_percent"] = t['percentageWinners']
            cf["contest_name"] = t["title"]
            cf["match_format"] = "NA"
            cf["tour_id"] = "NA"
            cf["record_time"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            cf["second_prize"] = "NA"
            cf["third_prize"] = "NA"
            for y in data["data"]["categories"]:
                for z in y["leagueInfo"]:
                    if 'First Prize' in z["tooltip"]:
                        cf["first_prize"] = z["title"]
            yield cf

if __name__ == "__main__":
    execute(f'scrapy crawl {Myteam11Contest.name}'.split())
