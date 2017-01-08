
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector 
from Scrapy1_doubanTop250.items import Scrapy1Doubantop250Item

class doubanTop250(CrawlSpider):
	name = 'doubanTop250'
	start_urls = ['https://movie.douban.com/top250']

	url = 'https://movie.douban.com/top250'

	def parse(self, response):
		item = Scrapy1Doubantop250Item()
		selector = Selector(response)
		Movies = selector.xpath('//div[@class="info"]')
		#获取当前页的电影信息
		for eachMovie in Movies:
			titles = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
			fullTitle = ''
			for eachTitle in titles:
				fullTitle += eachTitle
			movieInfos = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
			movieInfo = ';'.join(movieInfos)
			star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
			quotes = eachMovie.xpath('div[@class="bd"]/div[@class="quote"]/span[@class="inq"]/text()').extract()
			quote = ''
			if quotes:
				quote = quotes[0]
			item['title'] = fullTitle
			item['movieInfo'] = movieInfo
			item['star'] = star
			item['quote'] = quote
			yield item
		#获取‘下一页按钮’的值，如果@href不为空，继续爬取
		nextLinks = selector.xpath('//span[@class="next"]/link/@href').extract()
		if nextLinks:
			nextLink = nextLinks[0]
			print(nextLink)
			yield Request(self.url + nextLink, callback = self.parse)

		