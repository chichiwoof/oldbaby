import scrapy


class ArticleSpider(scrapy.Spider):
    name = "m4p2"
    start_urls = ['http://www.musicforprogramming.net/?one']

    def parse(self, response):
        content = response.xpath("//a[@href]/@href").extract_first()
	yield {'music': ''.join(content)}
