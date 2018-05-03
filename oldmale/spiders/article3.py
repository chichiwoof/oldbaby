import scrapy 

class ArticleSpider(scrapy.Spider):
    name = "article3"
    start_urls = ['http://www.musicforprogramming.net/?twentyeight']

    def parse(self, response):
        content = response.xpath("/html/body/div[3]/div[1]/div/span").extract()
        yield {'article': ''.join(content)}
