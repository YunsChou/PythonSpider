# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy5DapentiYituItem(scrapy.Item):
    title = scrapy.Field()
    publish = scrapy.Field()
    content = scrapy.Field()
    imgsrc = scrapy.Field()
