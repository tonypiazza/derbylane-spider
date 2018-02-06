# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
import re
import scrapy
from derbylane.items import ResultItem
from derbylane.repository import Repository


class ResultSpider(scrapy.Spider):
   name = "results"
   allowed_domains = ['derbylane.com']

   def start_requests(self):
      base_url = "http://www.derbylane.com/EntriesResult/SP{date}{schedule}RES.HTM"
      repo = Repository(self.settings)
      today = date.today()
      day = repo.get_last_result_date()
      if day is None:
         day = today - timedelta(days=30)
      elif day < today:
         day = day + timedelta(days=1)
      else:
         self.log("No results to download")
         return

      urls = []
      while day < today:
         day_of_week = day.weekday()
         if day_of_week < 6:
            fetch_date = "{:%m-%d-%Y}".format(day)
            urls.append(base_url.format(date=fetch_date, schedule='a'))
            urls.append(base_url.format(date=fetch_date, schedule='e'))
         day = day + timedelta(days=1)

      for url in urls:
         yield scrapy.Request(url=url, callback=self.parse)

   def parse(self, response):
      lines = response.selector.xpath('///pre/text()').extract_first().split('\r\n')

      n = 0
      racedate = None
      exp = re.compile("^.{43}\d\d\.\d\d\s.*")
      while n < len(lines):
         while True:
            done = False
            try:
               line = lines[n].rstrip()
            except IndexError:
               done = True
               break
            if re.match("^Derby Lane.*", line):
               break
            n = n + 1
         if done:
            break

         parts = line[29:].split()
         if racedate is None:
            racedate_str = "{month} {day} {year}".format(month=parts[1], 
                                                         day=parts[2], 
                                                         year=parts[3])
            racedate = datetime.strptime(racedate_str, "%b %d %Y").date()
            schedule = parts[4][:1]
         racenumber = int(parts[6])
         grade = parts[8]
         distance = int(parts[9][1:4])
         n = n + 2

         while True:
            line = lines[n].rstrip()
            if exp.match(line):
               item = ResultItem()
               item['track'] = "DerbyLane"
               item['raceDate'] = racedate
               item['schedule'] = schedule
               item['raceNumber'] = racenumber
               item['grade'] = grade
               item['distance'] = distance
               item['dogName'] = line[0:16].rstrip()
               item['weight'] = self.parse_float(line[17:20])
               item['box'] = line[21:22]
               item['start'] = line[23:24]
               item['stretch'] = line[25:26]
               item['turn'] = line[30:31]
               item['finish'] = line[35:36]
               item['behind'] = self.parse_float(line[37:39])
               item['time'] = self.parse_float(line[43:48])
               item['odds'] = self.parse_float(line[49:55])
               item['comments'] = line[55:].rstrip() if len(line) > 55 else None
               yield item
            else:
               break
            n = n + 1

      self.log("Processed results for {0}".format(racedate_str))

   def parse_float(self, value):
      result = value.replace(u"½", ".5") \
                    .replace(u"¾", ".75") \
                    .replace("*", "") \
                    .rstrip()
      if len(result) > 0:
         try:
            return float(result)
         except ValueError:
            return 0.0
      return 0.0
