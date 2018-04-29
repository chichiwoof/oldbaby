import scrapy 


class ArticleSpider(scrapy.Spider):
    name = "article"
    start_urls = ['https://www.looperman.com/loops/detail/126558/post-malone-type-loop-by-stevenabbs-free-100bpm-hip-hop-piano-loop']


    def parse(self, response):
        content = response.xpath(".//div[contains(@class,'player-wrapper')]").extract()
        yield {'article': ''.join(content)}
