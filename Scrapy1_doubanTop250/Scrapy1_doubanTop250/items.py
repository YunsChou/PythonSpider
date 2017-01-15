# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Scrapy1Doubantop250Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    info = Field()
    star = Field()
    quote = Field()
    imgsrc = Field()
