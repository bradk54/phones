# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PhonesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    screen = scrapy.Field()
    screenRes = scrapy.Field()
    screenType = scrapy.Field()
    opSys = scrapy.Field()
    memory = scrapy.Field()
    rearCamera = scrapy.Field()
    frontCamera = scrapy.Field()
    sensors = scrapy.Field()
    batterySize = scrapy.Field()
    basePrice = scrapy.Field()
    pricing = scrapy.Field()
    capacities = scrapy.Field()
    released = scrapy.Field()

    # pass
