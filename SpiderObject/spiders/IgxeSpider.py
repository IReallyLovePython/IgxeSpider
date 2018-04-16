# -*- coding: utf-8 -*-
import scrapy
from SpiderObject.items import SpiderobjectItem


class IgxespiderSpider(scrapy.Spider):
    name = 'IgxeSpider'
    allowed_domains = ['igxe.cn']

    page = 1
    url = 'https://www.igxe.cn/pubg/578080/%s/0/0' % page

    start_urls = [
        url
    ]

    def parse(self, response):
        for each in response.xpath("//div[@class='mod-theKeyItem']"):
            item = SpiderobjectItem()

            # 物品名称
            item['good_name'] = each.xpath("./div[@class='mod-theKeyItem-hd']//a/text()").extract()[0]
            # 物品详情链接
            item['good_link'] = each.xpath("./div[@class='mod-theKeyItem-hd']//a/@href").extract()[0]
            # 物品图片
            item['good_image'] = each.xpath("./div[@class='mod-theKeyItem-bd']//img/@src").extract()[0]
            # 物品在售数量
            item['good_couunts'] = \
                each.xpath("./div[@class='mod-theKeyItem-bd']//span[@class='amount']//b/text()").extract()[0]
            # 物品起价
            item['good_price'] = \
                each.xpath("./div[@class='mod-theKeyItem-bd']//span[@class='price']//b/text()").extract()[0]

            yield item

        # if self.page < 12:
        #     self.page += 1
        # yield scrapy.Request(self.url, callback=self.parse)
