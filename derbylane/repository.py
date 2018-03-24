# -*- coding: utf-8 -*-
from datetime import date
from mysql import connector

class Repository(object):
   def __init__(self, settings):
      self.connection = connector.connect(
         user=settings.get('MYSQL_USER', 'root'),
         password=settings.get('MYSQL_PASSWORD', 'password'),
         host=settings.get('MYSQL_HOST', '127.0.0.1'),
         database=settings.get('MYSQL_DATABASE', 'derbylane')
      )
      self.insert_cursor = self.connection.cursor(prepared=True)
      self.insert_dogresult = self.get_insert_dogresult()
      self.insert_dogentry = self.get_insert_dogentry()

   def get_last_result_date(self):
      cursor = self.connection.cursor()
      sql = "SELECT MAX(raceDate) FROM dogresult"
      cursor.execute(sql)
      value = cursor.fetchone()[0]
      return value if value is None else value.date()

   def insert_result_item(self, item):
      self.insert_cursor.execute(self.insert_dogresult, 
                                 [item[key] for key in sorted(item)])

   def get_last_entry_date(self):
      cursor = self.connection.cursor()
      sql = "SELECT MAX(raceDate) FROM dogentry"
      cursor.execute(sql)
      value = cursor.fetchone()[0]
      return value if value is None else value.date()

   def insert_entry_item(self, item):
      self.insert_cursor.execute(self.insert_dogentry, 
                                 [item[key] for key in sorted(item)])

   def commit_changes(self):
      self.connection.commit()
      self.connection.close()

   def get_insert_dogresult(self):
      return """INSERT INTO dogresult (
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
               ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                          %s, %s, %s, %s, %s, %s, %s, %s )"""

   def get_insert_dogentry(self):
      return """INSERT INTO dogentry (
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
               ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
