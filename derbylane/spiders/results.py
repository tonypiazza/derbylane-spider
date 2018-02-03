# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
import re
import scrapy
from derbylane.items import ResultItem


class ResultSpider(scrapy.Spider):
   name = "results"
   allowed_domains = ['derbylane.com']

   def start_requests(self):
      fetch_date = "{:%m-%d-%Y}".format(date.today() - timedelta(days=1))
      base_url = "http://www.derbylane.com/EntriesResult/SP{date}{schedule}RES.HTM"
      urls = []
      urls.append(base_url.format(date=fetch_date, schedule='a'))
      urls.append(base_url.format(date=fetch_date, schedule='e'))
      for url in urls:
         yield scrapy.Request(url=url, callback=self.parse)

   def parse(self, response):
      lines = response.selector.xpath('///pre/text()').extract_first().split('\r\n')
      n = 0
      racedate = None
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
            racedate = "{month} {day} {year}".format(month=parts[1], day=parts[2], year=parts[3])
            schedule = parts[4][:1]
         racenumber = int(parts[6])
         grade = parts[8]
         distance = int(parts[9][1:4])
         n = n + 2

         exp = re.compile("^.{43}\d\d\.\d\d\s.*")
         while True:
            line = lines[n].rstrip()
            if exp.match(line):
               item = ResultItem()
               item['track'] = "DerbyLane"
               item['raceDate'] = datetime.strptime(racedate, "%b %d %Y").date()
               item['schedule'] = schedule
               item['raceNumber'] = racenumber
               item['grade'] = grade
               item['distance'] = distance
               item['dogName'] = line[0:16].rstrip()
               item['weight'] = self.parse_float(line[17:20])
               item['box'] = int(line[21:22])
               item['start'] = int(line[23:24])
               item['stretch'] = int(line[25:26])
               item['turn'] = int(line[30:31])
               item['finish'] = int(line[35:36])
               item['behind'] = self.parse_float(line[37:39])
               item['time'] = self.parse_float(line[43:48])
               if len(line) > 55:
                  item['comments'] = line[55:].rstrip()
               yield item
            else:
               break
            n = n + 1

      self.log("Processed results for {0}".format(racedate))

   def parse_float(self, value):
      result = value.replace("½", ".5").replace("¾", ".75").rstrip()
      return float(result) if len(result) > 0 else 0.0
