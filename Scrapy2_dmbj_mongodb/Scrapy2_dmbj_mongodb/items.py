# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Field, Item


class Scrapy2DmbjMongodbItem(Item):
    bookName = Field()
    bookTitle = Field()
    # chapterNum = Field()
    # chapterName = Field()
    chapterURL = Field()
    contentText = Field()
