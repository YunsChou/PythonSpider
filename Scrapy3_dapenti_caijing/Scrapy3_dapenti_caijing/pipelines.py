# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class Scrapy3DapentiCaijingPipeline(object):
	def __init__(self):
		host = settings['MONGODB_HOST']
		port = settings['MONGODB_PORT']
		dbName = settings['MONGODB_DBNAME']
		docName = settings['MONGODB_DOCNAME']
		client = pymongo.MongoClient()
		tdb = client[dbName]
		self.post = tdb[docName]
		
	def process_item(self, item, spider):
		dataInfo = dict(item)
		self.post.insert(dataInfo)
		return item
