
import urlparse
from scrapy.http import Request
from scrapy.spiders import Spider


class wavsound(Spider):
    name = "wavsourceBS"

    allowed_domains = ["wavsource.com"]
    start_urls = ["http://www.wavsource.com/movies/2010.htm"]

    def parse(self, response):
        base_url = 'http://www.wavsource.com/movies/2010.htm'
        for a in response.xpath('//a[@href]/@href'):
            link = a.extract()
            if link.endswith('\.wav'):
                link = urlparse.urljoin(base_url, link)
                yield Request(link, callback=self.save_wav)

    def save_wav(self, response):
        path = response.url.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(response.body)
