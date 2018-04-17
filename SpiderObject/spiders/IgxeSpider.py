# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector, FormRequest

from SpiderObject.items import SpiderobjectItem


class IgxespiderSpider(scrapy.Spider):
    name = 'IgxeSpider'
    allowed_domains = ['igxe.cn']

    page = 1
    url = 'https://www.igxe.cn/login'

    start_urls = [
        url
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/65.0.3325.181Safari/537.36'
    }

    def parse(self, response):
        csrf = Selector(response).xpath('//input[@name="csrfmiddlewaretoken"]/@value').extract()[0]
        return [FormRequest.from_response(response,  # "https://www.igxe.cn/login",
                                          headers=self.headers,  # 注意此处的headers
                                          formdata={
                                              'csrfmiddlewaretoken': csrf,
                                              'username': 'h877969945j',
                                              'password': 'h25254818j.',
                                          },
                                          callback=self.parse_page,
                                          dont_filter=True
                                          )]

    def parse_page(self, response):
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

        url = 'https://www.igxe.cn/pubg/578080/%s/0/0' % self.page
        if self.page <12:
            self.page += 1
        yield scrapy.Request(url, callback=self.parse_page)
