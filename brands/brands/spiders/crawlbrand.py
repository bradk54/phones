# -*- coding: utf-8 -*-
import scrapy


class CrawlbrandSpider(scrapy.Spider):
    name = 'crawlbrand'
    allowed_domains = ['https://www.gsmarena.com/apple-phones-48.php']
    start_urls = ['http://https://www.gsmarena.com/apple-phones-48.php/']

    def parse(self, response):
        pass
