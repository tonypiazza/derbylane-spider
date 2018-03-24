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

   def get_last_result_date(self):
      cursor = self.connection.cursor()
      sql = "SELECT MAX(raceDate) FROM dogresult"
      cursor.execute(sql)
      value = cursor.fetchone()[0]
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
                  ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                             %s, %s, %s, %s, %s, %s, %s, %s )
            """
      self.insert_cursor.execute(sql, [item[key] for key in sorted(item)])

   def get_last_entry_date(self):
      cursor = self.connection.cursor()
      sql = "SELECT MAX(raceDate) FROM dogentry"
      cursor.execute(sql)
      value = cursor.fetchone()[0]
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
                  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
      self.insert_cursor.execute(sql, [item[key] for key in sorted(item)])

   def commit_changes(self):
      self.connection.commit()
      self.connection.close()
