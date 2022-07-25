# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    coin = scrapy.Field()
    bvid = scrapy.Field()
    dynamic = scrapy.Field()
    url = scrapy.Field()

    # 文件信息
    mp4_urls = scrapy.Field()
    mp3_urls = scrapy.Field()
    mp4_paths = scrapy.Field()
    mp3_paths = scrapy.Field()

