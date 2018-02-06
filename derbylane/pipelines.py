# -*- coding: utf-8 -*-
from derbylane.repository import Repository
from derbylane.items import EntryItem, ResultItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DerbylanePipeline(object):
   def open_spider(self, spider):
      self.repo = Repository(spider.settings)

   def close_spider(self, spider):
      self.repo.commit_changes()

   def process_item(self, item, spider):
      if isinstance(item, ResultItem):
         self.repo.insert_result_item(item)
      elif isinstance(item, EntryItem):
         self.repo.insert_entry_item(item)
      return item
