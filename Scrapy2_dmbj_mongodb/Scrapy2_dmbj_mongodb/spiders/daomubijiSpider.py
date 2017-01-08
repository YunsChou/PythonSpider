
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector 
from scrapy.http import Request
from Scrapy2_dmbj_mongodb.items import Scrapy2DmbjMongodbItem
import re

class daomubiji(CrawlSpider):
	name = "daomubiji"
	start_urls = ['http://www.daomubiji.com/']

	def parse(self, response):
		selector = Selector(response)
		tables = selector.xpath('//table')
		#获取每本书的table
		for eachTable in tables:
			bookName = eachTable.xpath('tr/td[@colspan="3"]/center/h2/text()').extract()[0]
			bookTitles = eachTable.xpath('tr/td/a/text()').extract()
			chapterURLs = eachTable.xpath('tr/td/a/@href').extract()

			for i in range(len(chapterURLs)):
				item = Scrapy2DmbjMongodbItem()
				item['bookName'] = bookName
				item['bookTitle'] = bookTitles[i]
				item['chapterURL'] = chapterURLs[i]
				# yield item
				#不直接返回item，使用Request关联到下一个函数爬取二级页面内容，使用meta来传递参数
				yield Request(chapterURLs[i], callback=self.parseContent, meta = {'item' : item})

	def parseContent(self, response):
		selector = Selector(response)
		item = response.meta['item']
		#爬取二级页面的内容
		html = selector.xpath('//div[@class="content"]').extract()[0]
		textField = re.search('<div style="clear:both"></div>(.*?)<div', html, re.S).group(1)
		contents = re.findall('<p>(.*?)</p>', textField, re.S)
		fullContent = ''
		for content in contents:
			fullContent += content
		#将二级页面的内容赋值给模型
		item['contentText'] = fullContent
		#返回item，完成本次完整的数据模型爬取
		yield item