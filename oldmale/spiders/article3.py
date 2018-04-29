import scrapy 


class ArticleSpider(scrapy.Spider):
    name = "article3"
    start_urls = ['http://www.musicforprogramming.net/?twentyeight']

    def parse(self, response):
        content = response.xpath("/html/body/div[2]/div/a[1]").extract()
        yield {'article': ''.join(content)}
