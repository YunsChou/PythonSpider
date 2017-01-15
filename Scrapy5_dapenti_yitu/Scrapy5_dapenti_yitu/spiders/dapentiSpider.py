from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from Scrapy5_dapenti_yitu.items import Scrapy5DapentiYituItem
import urllib.parse

class dapentiSpider(CrawlSpider):
	name = 'dapenti'
	start_urls = ['http://www.dapenti.com/blog/blog.asp?name=tupian']

	def parse(self, response):
		selector = Selector(response)
		tables = selector.xpath('//td[@class="oblog_t_2"]/div/ul/table[@class="ke-zeroborder"]')
		for table in tables:
			item = Scrapy5DapentiYituItem()
			title = table.xpath('tbody/tr/td[@class="oblog_t_4"]/div/span/span/a/text()').extract()[0]
			# print('title : %s' %title)
			publish = table.xpath('tbody/tr/td/table[@class="ke-zeroborder"]/tbody/tr/td/div/span/text()').extract()[0]
			# print('publish : %s' %publish)
			divNode = table.xpath('tbody/tr/td/span[@class="oblog_text"]/div[@align="left"]')[0]
			# print('divNode : %s' %divNode)

			item['title'] = title
			item['publish'] = publish
			imgsrc = ''
			fullContent = ''
			imgsrcs = divNode.xpath('img/@src').extract()
			if len(imgsrcs) > 0:
				imgsrc = imgsrcs[0]
				pNodes = divNode.xpath('p')
				if len(pNodes) > 0:
					contents = pNodes.xpath('strong/text()').extract()
					fullContent = ''.join(contents)
				else:
					contents = divNode.xpath('strong/text()').extract()
					fullContent = ''.join(contents)

				item['imgsrc'] = imgsrc
				item['content'] = fullContent
				yield item
			else:
				p_imgsrcs = divNode.xpath('p/img/@src').extract()
				if len(p_imgsrcs) == 0:
					p_imgsrcs = divNode.xpath('p/strong/img/@src').extract()
				if len(p_imgsrcs) > 0:
					imgsrc = p_imgsrcs[0]
					contents = divNode.xpath('p/strong/text()').extract()
					fullContent = ''.join(contents)

					item['imgsrc'] = imgsrc
					item['content'] = fullContent
					yield item
				
