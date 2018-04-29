# -*- coding: utf-8 -*-
import scrapy


class LoopermanSpider(scrapy.Spider):
    name = 'looperman'
    allowed_domains = ['https://www.looperman.com/loops']
    start_urls = ['http://https://www.looperman.com/loops/']

    def parse(self, response):
        pass
