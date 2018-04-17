# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderobjectItem(scrapy.Item):
    # define the fields for your item here like:
    # 物品名称
    good_name = scrapy.Field()
    # 物品详情链接
    good_link = scrapy.Field()
    # 物品图片
    good_image = scrapy.Field()
    # 物品在售数量
    good_couunts = scrapy.Field()
    # 物品起价
    good_price = scrapy.Field()

