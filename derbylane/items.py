# -*- coding: utf-8 -*-
import scrapy


class ResultItem(scrapy.Item):
   track = scrapy.Field()
   raceDate = scrapy.Field()
   schedule = scrapy.Field()
   raceNumber = scrapy.Field(serializer=int)
   grade = scrapy.Field()
   distance = scrapy.Field(serializer=int)
   dogName = scrapy.Field()
   weight = scrapy.Field(serializer=float)
   box = scrapy.Field(serializer=int)
   start = scrapy.Field(serializer=int)
   stretch = scrapy.Field(serializer=int)
   turn = scrapy.Field(serializer=int)
   finish = scrapy.Field(serializer=int)
   behind = scrapy.Field(serializer=float)
   time = scrapy.Field(serializer=float)
   odds = scrapy.Field(serializer=float)
   comments = scrapy.Field()

class EntryItem(scrapy.Item):
   track = scrapy.Field()
   raceDate = scrapy.Field()
   schedule = scrapy.Field()
   raceNumber = scrapy.Field(serializer=int)
   grade = scrapy.Field()
   distance = scrapy.Field(serializer=int)
   dogName = scrapy.Field()
   box = scrapy.Field(serializer=int)
   birthDate = scrapy.Field()
   gender = scrapy.Field()
