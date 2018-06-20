# -*- coding: utf-8 -*-
import scrapy


class LotterySpider(scrapy.Spider):
    name = 'lottery'
    allowed_domains = ['www.lottery.gov.cn']
    start_urls = ['http://www.lottery.gov.cn/']

    def parse(self, response):
        pass
