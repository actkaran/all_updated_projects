import scrapy


class MatchData(scrapy.Item):
    match_id = scrapy.Field()
    main_tab_sport = scrapy.Field()
    team_1 = scrapy.Field()
    team_2 = scrapy.Field()
    match_start_datetime = scrapy.Field()
    match_format = scrapy.Field()
    tour_name = scrapy.Field()


class ContestsData(scrapy.Item):
    main_tab_sport = scrapy.Field()
    match_id = scrapy.Field()
    tour_id = scrapy.Field()
    match_name = scrapy.Field()
    team_1 = scrapy.Field()
    team_2 = scrapy.Field()
    tour_name = scrapy.Field()
    match_start_datetime = scrapy.Field()
    contest_description = scrapy.Field()
    record_time = scrapy.Field()
    match_format = scrapy.Field()
    tab = scrapy.Field()
    winner_percent = scrapy.Field()
    first_prize = scrapy.Field()
    second_prize = scrapy.Field()
    third_prize = scrapy.Field()
    contest_id = scrapy.Field()
    entry_fee = scrapy.Field()
    max_spots = scrapy.Field()
    spots_filled = scrapy.Field()
    total_price_amount = scrapy.Field()
    max_teams_per_user = scrapy.Field()
    contest_name = scrapy.Field()
    winner = scrapy.Field()
    contest_guarantee = scrapy.Field()
