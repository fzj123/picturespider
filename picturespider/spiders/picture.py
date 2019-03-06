# -*- coding: utf-8 -*-
import scrapy

from picturespider.items import PicturespiderItem


class PictureSpider(scrapy.Spider):
    name = "picture"
    allowed_domains = ["pixabay.com"]
    start_urls = ['https://pixabay.com/images/search/']

    def parse(self, response):
        picture_url = response.xpath('.//div[@class="item"]')
        for picture in picture_url:
            item = PicturespiderItem()
            item['img'] = picture.xpath('./a/img/@src').extract()
            yield item

        next_url = response.xpath('//*[@id="content"]/div/a/@href').extract_first()
        if next_url is not None:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)