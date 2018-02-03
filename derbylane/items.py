# -*- coding: utf-8 -*-

import scrapy


class ResultItem(scrapy.Item):
   track = scrapy.Field()
   raceDate = scrapy.Field()
   schedule = scrapy.Field()
   raceNumber = scrapy.Field()
   grade = scrapy.Field()
   distance = scrapy.Field()
   dogName = scrapy.Field()
   weight = scrapy.Field()
   box = scrapy.Field()
   start = scrapy.Field()
   stretch = scrapy.Field()
   turn = scrapy.Field()
   finish = scrapy.Field()
   behind = scrapy.Field()
   time = scrapy.Field()
   comments = scrapy.Field()

class EntryItem(scrapy.Item):
   track = scrapy.Field()
   raceDate = scrapy.Field()
   schedule = scrapy.Field()
   raceNumber = scrapy.Field()
   grade = scrapy.Field()
   distance = scrapy.Field()
   dogName = scrapy.Field()
   box = scrapy.Field()
   birthDate = scrapy.Field()
   gender = scrapy.Field()
