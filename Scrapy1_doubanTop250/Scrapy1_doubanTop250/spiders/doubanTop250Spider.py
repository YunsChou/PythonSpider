
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
		Movies = selector.xpath('//div[@class="item"]')
		#获取当前页的电影信息
		for eachMovie in Movies:
			# 电影图片
			imgsrc = eachMovie.xpath('div[@class="pic"]/a/img/@src').extract()[0]
			# 电影其他信息
			MovieInfo = eachMovie.xpath('div[@class="info"]')
			titles = MovieInfo.xpath('div[@class="hd"]/a/span/text()').extract()
			fullTitle = ''
			for eachTitle in titles:
				fullTitle += eachTitle
			infos = MovieInfo.xpath('div[@class="bd"]/p/text()').extract()
			info = ';'.join(infos)
			star = MovieInfo.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
			quotes = MovieInfo.xpath('div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()
			quote = ''
			if len(quotes) > 0:
				quote = quotes[0]
			item['title'] = fullTitle
			item['info'] = info
			item['star'] = star
			item['quote'] = quote
			item['imgsrc'] = imgsrc
			yield item
		# 获取‘下一页按钮’的值，如果@href不为空，继续爬取
		nextLinks = selector.xpath('//span[@class="next"]/link/@href').extract()
		if nextLinks:
			nextLink = nextLinks[0]
			print(nextLink)
			yield Request(self.url + nextLink, callback = self.parse)

		
		

		