
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from Scrapy4_dapenti_tugua.items import Scrapy4DapentiTuguaItem
import urllib.parse

class dapentiSpider(CrawlSpider):
	name = 'dapenti'
	start_urls = ['http://www.dapenti.com/blog/blog.asp?name=xilei&subjectid=70&page=1']


	def parse(self, response):
		url = 'http://www.dapenti.com/blog/blog.asp?name=xilei&subjectid=70&page=1'
		selector = Selector(response)
		print('-----------------------------------')
		uls = selector.xpath('//div[@align="left"]/ul/li/a')
		for ul in uls:
			item = Scrapy4DapentiTuguaItem()
			item['title'] = ul.xpath('text()').extract()[0]
			href = ul.xpath('@href').extract()[0]
			detail_url = urllib.parse.urljoin(url, href)
			yield Request(detail_url, callback = self.parseContent, meta = {'item' : item})
			# yield item

	def parseContent(self, response):
		selector = Selector(response)
		item = response.meta['item']
		item['publish'] = selector.xpath('//span[@class="oblog_text"]/text()').extract()[0]
		contents = selector.xpath('//div[@class="oblog_text"]/p').extract()
		fullContent =  ''.join(contents)
		item['content'] = fullContent
		yield item