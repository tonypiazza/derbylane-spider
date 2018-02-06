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
      repo = Repository(self.settings)
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
            urls.append(base_url.format(date=fetch_date, schedule='e'))
         day = day + timedelta(days=1)

      for url in urls:
         yield scrapy.Request(url=url, callback=self.parse)

   def parse(self, response):
      lines = response.selector.xpath('///pre/text()').extract_first().split('\r\n')

      n = 0
      racedate = None
      exp = re.compile("^\d.*")
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
         distance = int(parts[10][0:3])
         n = n + 2

         while True:
            line = lines[n].rstrip()
            if exp.match(line) and not line.endswith("Empty Post"):
               item = EntryItem()
               item['track'] = "DerbyLane"
               item['raceDate'] = racedate
               item['schedule'] = schedule
               item['raceNumber'] = racenumber
               item['grade'] = grade
               item['distance'] = distance
               item['dogName'] = line[0:16].rstrip()
               item['box'] = line[0:1]

               parenPos = line.find("(")
               endPos = parenPos if parenPos > 0 else 25
               item['dogName'] = line[2:endPos].rstrip()
               n = n + 2
               line = lines[n].rstrip()
               moreParts = line.split("|")
               item['gender'] = moreParts[1]
               item['birthDate'] = datetime.strptime(moreParts[2], "%M/%d/%Y").date()
               yield item
            elif line.startswith("=================="):
               break
            n = n + 1

      self.log("Processed entries for {0}".format(racedate_str))
