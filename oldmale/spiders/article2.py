import scrapy 


class ArticleSpider(scrapy.Spider):
    name = "article2"
    start_urls = ['http://www.wavsource.com/movies/2001.htm']

    def parse(self, response):
        content = response.xpath(".//td[@class='c']/descendant::a[contains(@href)]").extract()
        yield {'article': ''.join(content)}
