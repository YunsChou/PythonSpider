# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
# from scrapy.settings import Settings
import pymongo

class Scrapy2DmbjMongodbPipeline(object):
	def __init__(self):
		# settings = Settings()
		host = settings['MONGODB_HOST']
		port = settings['MONGODB_PORT']
		dbName = settings['MONGODB_DBNAME']
		docName = settings['MONGODB_DOCNAME']
		client = pymongo.MongoClient()
		tdb = client[dbName]
		self.post = tdb[docName]

	def process_item(self, item, spider):
		bookInfo = dict(item)
		self.post.insert(bookInfo)
		return item
