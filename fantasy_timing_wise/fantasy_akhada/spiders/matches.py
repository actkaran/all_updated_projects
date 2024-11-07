import json
from datetime import datetime
import scrapy
import fantasy_akhada.DB_CONFIG as db
import pandas as pd
from scrapy.cmdline import execute
from fantasy_akhada.items import FaMatchItem


class FantasySpider(scrapy.Spider):
    name = "matches_fa"

    def start_requests(self):
        dic = [
            {
                "url": 'https://supersix-aws-live.s3.ap-south-1.amazonaws.com/appstatic/lobby_fixture_list_5.json?time=28715572',
                "sports": 'Football',
                "sport_id": 5},
            {
                "url": 'https://supersix-aws-live.s3.ap-south-1.amazonaws.com/appstatic/lobby_fixture_list_7.json?time=28715575',
                "sports": "Cricket",
                "sport_id": 7
            },
            {
                "url": 'https://supersix-aws-live.s3.ap-south-1.amazonaws.com/appstatic/lobby_fixture_list_4.json?time=28715576',
                "sports": 'Basketball',
                "sport_id": 4
            }
        ]
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive',
            'Host': 'supersix-aws-live.s3.ap-south-1.amazonaws.com',
            'User-Agent': 'okhttp/4.9.2'
        }
        for x in dic:
            url = x["url"]
            sport = x["sports"]
            sport_id = x["sport_id"]
            yield scrapy.Request(
                method='GET',
                url=url,
                headers=headers,
                cb_kwargs={'sports': sport, "sport_id": sport_id},
                callback=self.parse)
            # break

    def parse(self, response, **kwargs):
        temp = FaMatchItem()
        try:
            temp["sport_id"] = kwargs["sport_id"]
            jd = json.loads(response.text)
            for x in jd:
                temp["main_tab_sport"] = kwargs["sports"]
                temp["match_id"] = x["collection_master_id"]
                temp['season_scheduled_date'] = x["season_scheduled_date"]
                temp["tour_id"] = x["league_id"]
                temp["match_name"] = x["collection_name"]
                temp["team_1"] = x["home"]
                temp["team_2"] = x["away"]
                temp["tour_name"] = x["league_name"]
                temp["match_start_datetime"] = str(datetime.fromtimestamp(x["game_starts_in"] / 1000))
                yield temp
        except Exception as e:
            self.logger.info(e)
            self.logger.debug(e)
            self.logger.error("----------------")


if __name__ == '__main__':
    execute(f'scrapy crawl {FantasySpider.name}'.split())
