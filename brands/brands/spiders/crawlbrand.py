# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule,Spider
import string
from scrapy import Request
from brands.items import BrandsItem

class CrawlbrandSpider(scrapy.Spider):
    name = 'crawlbrand'
    allowed_domains = ['www.gsmarena.com']
    start_urls = ["http://www.gsmarena.com/oneplus-phones-95.php",]
    base_url = 'http://www.gsmarena.com/'
    rules = [Rule(LinkExtractor(allow=('/pn\d+')),callback='parse',follow=True)]

    def parse(self, response):
        for href in response.xpath('//div[@class="makers"]/ul/li/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback = self.parse_data)

        next_page_partial_url = response.xpath('//a[@class="pages-next"]/@href').extract_first()
        next_page_url = self.base_url+next_page_partial_url
        yield scrapy.Request(next_page_url,callback = self.parse)

    def parse_data(self, response):
        for sel in response.xpath('//body'):
            item = BrandsItem()
            item['title'] = sel.xpath('.//h1[contains(@class,"specs-phone-name-title")]/text()').extract()
            item['screen'] = sel.xpath('.//td[@data-spec="displaysize"]/text()').extract()
            item['screenRes'] = sel.xpath('.//td[@data-spec="displayresolution"]/text()').extract()
            item['screenType'] = sel.xpath('.//td[@data-spec="displaytype"]/text()').extract()
            item['opSys'] = sel.xpath('.//td[@data-spec="os"]/text()').extract()
            item['memory'] = sel.xpath('.//td[@data-spec="internalmemory"]/text()').extract()
            item['rearCamera'] = sel.xpath('.//td[@data-spec="cam1modules"]/text()').extract()
            item['frontCamera'] = sel.xpath('.//td[@data-spec="cam2modules"]/text()').extract()
            item['sensors']= sel.xpath('.//td[@data-spec="sensors"]/text()').extract()
            item['batterySize'] = sel.xpath('.//td[@data-spec="batdescription1"]/text()').extract()
            item['basePrice']=sel.xpath('.//td[@data-spec="price"]/a/text()').extract()
            item['released']=sel.xpath('.//td[@data-spec="year"]/text()').extract()
            item['capacities'] = sel.xpath('.//div[@class = "pricing"]/span/text()').extract()
            item['pricing']=sel.xpath('.//div[@class = "pricing"]//a/text()').extract()
            yield item
