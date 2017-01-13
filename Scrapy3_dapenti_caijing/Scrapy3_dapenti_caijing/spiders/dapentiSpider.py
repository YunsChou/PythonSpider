
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from Scrapy3_dapenti_caijing.items import Scrapy3DapentiCaijingItem
import urllib.parse

class dapentiSpider(CrawlSpider):
	name = 'dapenti'
	start_urls = ['http://www.dapenti.com/blog/blog.asp?name=caijing&page=1']

	

	def parse(self, response):
		url = 'http://www.dapenti.com/blog/blog.asp?name=caijing&page=1'
		selector = Selector(response)
		uls = selector.xpath('//td[@class="oblog_t_2"]/div[@align="left"]/ul/li/a')
		for ul in uls:
		# for i in range(1):
			# ul = uls[i]
			item = Scrapy3DapentiCaijingItem()
			item['title'] = ul.xpath('text()').extract()[0]
			href = ul.xpath('@href').extract()[0]
			detail_url = urllib.parse.urljoin(url, href)
			yield Request(detail_url, callback = self.parseContent, meta = {'item' : item})

	def parseContent(self, response):
		selector = Selector(response)
		item = response.meta['item']
		item['publish'] = selector.xpath('//span[@class="oblog_text"]/text()').extract()[0]
		contents = selector.xpath('//div[@align="left"]/p/text()').extract()
		fullContent =  '\n'.join(contents)
		item['content'] = fullContent
		yield item