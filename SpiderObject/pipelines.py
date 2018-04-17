# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class SpiderobjectPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json


class IgxeSpiderPipeline(object):
    def __init__(self):
        self.filename = open("Igxe.csv", "wb")

    def process_item(self, item, spider):
        # type(item)为<class 'SpiderObject.items.SpiderobjectItem'>，类似字典的对象
        text = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # type(text)为str
        self.filename.write(text.encode('gbk'))
        return item

    def close_spider(self,spider):
        self.filename.close()
