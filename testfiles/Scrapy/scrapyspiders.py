import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class wavsource1(CrawlSpider):
    name = "wavsource1"
    allowed_domains = ["wavsource.com"]
    start_urls = ["http://www.wavsource.com/movie_stars/de_niro.htm"]
    rules = (
        Rule(LinkExtractor( allow=(),
                                #(a regular expression (or list of)) – a single regular expression (or list of regular expressions) that the (absolute) urls must match in order to be extracted. If not given (or empty), it will match all links.
                            deny=(),
                                #(a regular expression (or list of)) – a single regular expression (or list of regular expressions) that the (absolute) urls must match in order to be excluded (ie. not extracted). It has precedence over the allow parameter. If not given (or empty) it won’t exclude any links.
                            allow_domains=(),
                                #a single value or a list of string containing domains which will be considered for extracting the links
                            deny_domains=(),
                                #a single value or a list of strings containing domains which won’t be considered for extracting the links
                            deny_extensions=None,
                                #a single value or list of strings containing extensions that should be ignored when extracting links. If not given, it will default to the IGNORED_EXTENSIONS list defined in the scrapy.linkextractors package.
                            restrict_xpaths=(),
                                #is an XPath (or list of XPath’s) which defines regions inside the response where links should be extracted from. If given, only the text selected by those XPath will be scanned for links. See examples below.
                            restrict_css=(),

                            tags=('a', 'area'),
                            attrs=('href', ),
                            canonicalize=False,
                            unique=True,
                            process_value=None,
                            strip=True)
                        )
        #Rule(callback)
        #Rule(cb_kwargs)
        #Rule(follow)
        #Rule(process_links)
        #Rule(process_request)


#     def parse_item(self, response):
#        self.logger.info('Hi, this is an item page! %s', response.url)
#        item = scrapy.Item()
#        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
#        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
#        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
#        return item
________________________________________________________________________________

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item



________________________________________________________________________________


import urlparse
from scrapy.http import Request
from scrapy.spiders import Spider


class wavsound(Spider):
    name = "wavsourcesimple"

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
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

_______________________________________________________________________________



class WavSourceSpider(scrapy.Spider):
    name = "wavsourcesimple"

    def start_requests(self):
        urls = ['http://www.wavsource.com/movies/movies1.htm'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'whoknows-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)



_____________________________________________________________________________


import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'wavsourcelinkex2'
    allowed_domains = ['wavsource.com']
    start_urls = ['http://www.wavsource.com/movies/movies1.htm']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('\.htm', '\.wav' ), )),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('\.htm', )), callback='parse_item'),
    )

def parse_item(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


    #def parse_item(self, response):
    #    self.logger.info('Hi, this is a music page! %s', response.url)
    #    item = scrapy.Item()
    #    item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
    #    item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
    #    item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
    #    return item





import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)






import scrapy
from myproject.items import MyItem

class MySpider(scrapy.Spider):
    name = 'wavsourcemyspider'
    start_urls = (
        'http://www.wavsource.com/movies/movies1.htm'
        )

    def parse(self, response):
        # collect `item_urls`
        for item_url in item_urls:
            yield scrapy.Request(item_url, self.parse_item)

    def parse_item(self, response):
        item = MyItem()
        # populate `item` fields
        # and extract item_details_url
        yield scrapy.Request(item_details_url, self.parse_details, meta={'item': item})

    def parse_details(self, response):
        item = response.meta['item']
        # populate more `item` fields
        return item





import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article"
    start_urls = ['https://www.looperman.com/loops/detail/126558/post-malone-type-loop-by-stevenabbs-free-100bpm-hip-hop-piano-loop']

    def parse(self, response):
        content = response.xpath(".//div[contains(@class,'player-wrapper')]").extract()
        yield {'article': ''.join(content)}


<div class="player-wrapper 2054317cd2f3456788b7ec06943e8487a2cef89e loop" rel="./media/loops/1533861/looperman-l-1533861-0086820-martingunnarsson-soothing-jazz-piano-1.mp3">

https://www.looperman.com/media/loops/1533861/looperman-l-1533861-0086820-martingunnarsson-soothing-jazz-piano-1.mp3

view-source:https://www.looperman.com/loops/detail/126558/post-malone-type-loop-by-stevenabbs-free-100bpm-hip-hop-piano-loop

#  <script type="text/javascript">


import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article3"
    start_urls = ['http://www.musicforprogramming.net/?twentyeight']

    def parse(self, response):
        content = response.xpath("/html/body/div[3]/div[1]/div/span").extract()
        yield {'article': ''.join(content)}

http://www.musicforprogramming.net/?twentyeight



/html/body/div[1]/div[3]/div[1]/div[4]/p[2]/a[2]


//*[@id="player"]
//*[@id="player"]
/html/body/div[2]/div/a[1]
import scrapy


class ArticleSpider(scrapy.Spider):
    name = "m4p"
    start_urls = ['http://www.musicforprogramming.net/?twentyeight']

    def parse(self, response):
        content = response.xpath("/html/body/div[2]/div/a[1]").extract()
        yield {'music': ''.join(content)}



http://www.musicforprogramming.net/?fortytwo

view-source:http://www.musicforprogramming.net/?twentyeight
/html/body/pre/span[218]/a
/html/body/div[2]/div/a[1]
http://datashat.net/music_for_programming_28-big_war.mp3

http://www.musicforprogramming.net/

/html/body/pre/span[178]/a[1]




#  https://www.looperman.com/media/loops/1533861/looperman-l-1533861-0086820-martingunnarsson-soothing-jazz-piano-1.mp3

http://www.wavsource.com/ "snds_2018-01-14_3453803176249356"  "/movies/2001/"   "completed.wav"



http://www.wavsource.com/snds_2018-01-14_3453803176249356/movies/2001/stress_pill.wav
http://www.wavsource.com/snds_2018-01-14_3453803176249356/movies/airplane/computer_blow.wav
http://www.wavsource.com/snds_2018-01-14_3453803176249356/people/women/ahhah_x.wav



#  //a[@class='bf' and starts-with(@href, '/book/')]

#  a[contains(@href,'listDetails.do') and @id='oldcontent']");


        # <a href="/snds_2018-01-14_3453803176249356/movies/2001/completed.wav" title=" added April 4, 2004 ">Completed</a>
        # <a href="/snds_2018-01-14_3453803176249356/movies/2001/daisy.wav" title=" added July 24, 2001 ">Daisy</a>






import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article"
    start_urls = ['http://blog.theodo.fr/2018/02/scrape-websites-5-minutes-scrapy']

    def parse(self, response):
        content = response.xpath(".//div[@class='entry-content']/descendant::text()").extract()
        yield {'article': ''.join(content)}




page = response.url.split("/")[-2]
filename = 'quotes-%s.html' % page
with open(filename, 'wb') as f:
    f.write(response.body)
self.log('Saved file %s' % filename)


Absolute vs relative XPaths (/ vs .)

/ introduces an absolute location path, starting at the root of the document.
. introduces a relative location path, starting at the context node.
Named element vs any element (ename vs *)

/ename selects an ename root element
./ename selects all ename child elements of the current node.
/* selects the root element, regardless of name.
./* or * selects all child elements of the context node, regardless of name.
descendant-or-self axis (//*)

//ename selects all ename elements in a document.
.//ename selects all ename elements at or beneath the context node.
//* selects all elements in a document, regardless of name.
.//* selects all elements, regardless of name, at or beneath the context node.
With these concepts in mind, here are answers to your specific questions...

.//*[@id='Passwd'] means to select all elements at or beneath the current context node that have an id attribute value equal to 'Passwd'.
//child::input[@type='password'] can be simplified to //input[@type='password'] and means to select all input elements in the document that have an type attribute value equal to 'password'.
