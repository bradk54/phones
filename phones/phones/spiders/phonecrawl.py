# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule,Spider
import string
from scrapy import Request
from phones.items import PhonesItem
# import pandas as pd
url = 'https://www.gsmarena.com/'
class PhonecrawlSpider(scrapy.Spider):
    name = 'phonecrawl'
    allowed_domains = ['www.gsmarena.com']
    start_urls = ["http://www.gsmarena.com/results.php3?",]
    rules = [Rule(LinkExtractor(allow=('/pn\d+')),callback='parse',follow=True)]

    def parse(self, response):
        for href in response.xpath('//div[@class="makers"]/ul/li/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback = self.parse_dat)


    def parse_dat(self,response):
        for sel in response.xpath('//body'):
            item = PhonesItem()
            item['title'] = sel.xpath('.//h1[contains(@class,"specs-phone-name-title")]/text()').extract()
            item['screen'] = sel.xpath('.//td[@data-spec="displaysize"]/text()').extract()
            yield item
