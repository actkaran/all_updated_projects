import json
from myteam11_bot.items import MatchData
import scrapy
from scrapy.cmdline import execute
from datetime import datetime


class MyteamMatch(scrapy.Spider):
    name = 'myteam11_match'
    match_headers = {
        "Accept-Encoding": "gzip",
        "appCode": "2",
        "AppType": "1",
        "AppVersion": "101",
        "Connection": "Keep-Alive",
        "DeviceName": "SM-G988N",
        "DeviceOS": "Android",
        "Host": "app.myteam11.com",
        "IsPlayStore": "1",
        "User-Agent": "okhttp/4.9.1",
        "UserId": "18816731"
    }

    def start_requests(self):
        match_urls_list = [
            {'url': 'https://app.myteam11.com/match/v1/upcoming/1', 'sports': 'Cricket'},
            {'url': 'https://app.myteam11.com/match/v1/upcoming/2', 'sports': 'Football'}
        ]
        for match_url in match_urls_list:
            yield scrapy.Request(
                url=match_url['url'],
                headers=self.match_headers,
                cb_kwargs={
                    'sports': match_url['sports']
                }
            )

            # break

    def parse(self, response, **kwargs):
        try:
            data = json.loads(response.text)
            matches = data.get('Response', {}).get('NotStarted', [])
            match_item = MatchData()
            if matches:
                for match in matches:
                    match_item['match_id'] = match.get('MatchId')
                    match_item['main_tab_sport'] = kwargs['sports']
                    match_item['team_1'] = match.get('TeamName1')
                    match_item['team_2'] = match.get('TeamName2')
                    match_item["match_format"] = match.get('Format')
                    temp_date = datetime.strptime(match.get('StartDate'), "%d-%m-%Y %H:%M:%S")
                    match_item['match_start_datetime'] = temp_date.strftime("%Y-%m-%d %H:%M:%S")
                    match_item['tour_name'] = match.get('RelatedName')
                    yield match_item
        except Exception as e:
            self.logger.info(e)
            self.logger.debug(e)
            self.logger.error("----------------")

if __name__ == "__main__":
    execute(f'scrapy crawl {MyteamMatch.name}'.split())