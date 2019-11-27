# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BetterdaysItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    nickname = scrapy.Field()
    cityname = scrapy.Field()
    content = scrapy.Field()
    gender = scrapy.Field()
    score = scrapy.Field()
    approve = scrapy.Field()
    time = scrapy.Field()
