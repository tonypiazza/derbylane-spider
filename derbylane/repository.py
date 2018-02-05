# -*- coding: utf-8 -*-
from datetime import date
from mysql import connector

class Repository(object):
   def __init__(self):
      self.con = connector.connect(
                  user='root', 
                  password='password',
                  host='127.0.0.1',
                  database='PapaJim')
      self.cur = self.con.cursor()

   def get_last_result_date(self):
      sql = "SELECT MAX(raceDate) FROM dogresult"
      self.cur.execute(sql)
      value = self.cur.fetchone()[0]
      return value if value is None else value.date()

   def insert_result_item(self, item):
      sql = """INSERT INTO dogresult (
                     behind, 
                     box, 
                     comments, 
                     distance, 
                     dogName, 
                     finish, 
                     grade, 
                     odds, 
                     raceDate, 
                     raceNumber,
                     schedule,
                     start,
                     stretch,
                     time,
                     track,
                     turn,
                     weight
                  ) VALUES (
                     %behind, 
                     %box, 
                     %comments, 
                     %distance, 
                     %dogName, 
                     %finish, 
                     %grade, 
                     %odds, 
                     %raceDate, 
                     %raceNumber,
                     %schedule,
                     %start,
                     %stretch,
                     %time,
                     %track,
                     %turn,
                     %weight
                  )"""
      self.cur.execute(sql, item.values())

   def get_last_entry_date(self):
      sql = "SELECT MAX(raceDate) FROM dogentry"
      self.cur.execute(sql)
      value = self.cur.fetchone()[0]
      return value if value is None else value.date()

   def commit_changes(self):
      self.con.commit()
