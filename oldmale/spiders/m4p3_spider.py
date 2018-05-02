import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class M4p3Spider(CrawlSpider):
	name = "m4p3"
	allowed_domains = ['musicforprogramming.net']
	start_urls = ['http://www.musicforprogramming.net/?one']

	rules = (
		Rule(LinkExtractor(restrict_xpaths=restrict_xpaths=('//li[@class="next"]/a')), callback='parse_item'),
	)

	def parse_item(self, response):
		content = response.xpath("//*").extract()
		yield {'music': ''.join(content)}

