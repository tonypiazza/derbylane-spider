# -*- coding: utf-8 -*-
from datetime import date
from mysql import connector

class Repository(object):
   def __init__(self, settings):
      self.con = connector.connect(
         user=settings.get('MYSQL_USER', 'root'),
         password=settings.get('MYSQL_USER', 'password'),
         host=settings.get('MYSQL_HOST', '127.0.0.1'),
         database=settings.get('MYSQL_DATABASE', 'PapaJim')
      )
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
                     %(behind)s, 
                     %(box)s, 
                     %(comments)s, 
                     %(distance)s, 
                     %(dogName)s, 
                     %(finish)s, 
                     %(grade)s, 
                     %(odds)s, 
                     %(raceDate)s, 
                     %(raceNumber)s,
                     %(schedule)s,
                     %(start)s,
                     %(stretch)s,
                     %(time)s,
                     %(track)s,
                     %(turn)s,
                     %(weight)s
                  )
            """
      self.cur.execute(sql, dict(item))

   def get_last_entry_date(self):
      sql = "SELECT MAX(raceDate) FROM dogentry"
      self.cur.execute(sql)
      value = self.cur.fetchone()[0]
      return value if value is None else value.date()

   def insert_entry_item(self, item):
      sql = """INSERT INTO dogentry (
                     birthDate, 
                     box, 
                     distance, 
                     dogName, 
                     gender, 
                     grade, 
                     raceDate, 
                     raceNumber, 
                     schedule, 
                     track
                  ) VALUES (
                     %(birthDate)s, 
                     %(box)s, 
                     %(distance)s, 
                     %(dogName)s, 
                     %(gender)s, 
                     %(grade)s, 
                     %(raceDate)s, 
                     %(raceNumber)s, 
                     %(schedule)s, 
                     %(track)s
                  )
            """
      self.cur.execute(sql, dict(item))

   def commit_changes(self):
      self.con.commit()
      self.con.close()
