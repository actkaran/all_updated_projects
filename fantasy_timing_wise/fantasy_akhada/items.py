# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FaMatchItem(scrapy.Item):
    sport_id = scrapy.Field()
    main_tab_sport = scrapy.Field()
    match_id = scrapy.Field()
    season_scheduled_date = scrapy.Field()
    tour_id = scrapy.Field()
    match_name = scrapy.Field()
    team_1 = scrapy.Field()
    team_2 = scrapy.Field()
    tour_name = scrapy.Field()
    match_start_datetime = scrapy.Field()

class FaContestItem(scrapy.Item):
    main_tab_sport = scrapy.Field()
    match_id = scrapy.Field()
    tour_id = scrapy.Field()
    match_name = scrapy.Field()
    team_1 = scrapy.Field()
    team_2 = scrapy.Field()
    tour_name = scrapy.Field()
    match_start_datetime = scrapy.Field()
    # group_name = scrapy.Field()
    contest_description = scrapy.Field()
    record_time = scrapy.Field()
    # contest_unique_id = scrapy.Field()
    match_format = scrapy.Field()
    tab = scrapy.Field()
    winner_percent = scrapy.Field()
    first_price = scrapy.Field()
    second_price = scrapy.Field()
    third_price = scrapy.Field()
    contest_id = scrapy.Field()
    entry_fee = scrapy.Field()
    max_spots = scrapy.Field()
    # minimum_size = scrapy.Field()
    spots_filled = scrapy.Field()
    total_price_amount = scrapy.Field()
    max_teams_per_user = scrapy.Field()
    # user_joined_count = scrapy.Field()
    contest_name = scrapy.Field()
    # price_distribution_per = scrapy.Field()
    winner = scrapy.Field()
    contest_guarantee = scrapy.Field()
