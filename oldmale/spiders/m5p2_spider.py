import urlparse
import scrapy

from scrapy.http import Request

class Wavspider(scrapy.Spider):
    name = "m5p2"

    allowed_domains = ['musicforprogramming.net']
    start_urls = ['http://www.musicforprogramming.net/?one']

    def parse(self, response):
        base_url = "http://www.musicforprogramming.net/?one"
        for a in response.xpath('//a[@href]/@href'):
            link = a.extract()
            if link.endswith('.mp3'):
                link = urlparse.urljoin(base_url, link)
                yield Request(link, callback=self.save_mp3)

    def save_mp3(self, response):
        path = response.url.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(response.body)
