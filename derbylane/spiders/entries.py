# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
import re
import scrapy
import sys
from derbylane.items import EntryItem
from derbylane.repository import Repository


class EntrySpider(scrapy.Spider):
   name = "entries"
   allowed_domains = ['derbylane.com']

   def start_requests(self):
      base_url = "http://www.derbylane.com/EntriesResult/SP{date}{schedule}ENT.HTM"
      repo = Repository()
      today = date.today()
      final_day = today + timedelta(days=1)
      day = repo.get_last_entry_date()
      if day is None:
         day = today - timedelta(days=1)
      elif day < today:
         day = day + timedelta(days=1)
      else:
         self.log("No entries to download")
         sys.exit(0)

      urls = []
      while day < final_day:
         day_of_week = day.weekday()
         if day_of_week < 6:
            fetch_date = "{:%m-%d-%Y}".format(day)
            urls.append(base_url.format(date=fetch_date, schedule='a'))
            if day_of_week > 0:
               urls.append(base_url.format(date=fetch_date, schedule='e'))
         day = day + timedelta(days=1)

      for url in urls:
         yield scrapy.Request(url=url, callback=self.parse)

   def parse(self, response):
      pass
