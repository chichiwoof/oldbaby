import scrapy 


class ArticleSpider(scrapy.Spider):
    name = "m4p"
    start_urls = ['http://www.musicforprogramming.net/']

    def parse(self, response):
        content = response.xpath("/html/body/pre/span[178]/a[1]").extract()
        yield {'article': ''.join(content)}
