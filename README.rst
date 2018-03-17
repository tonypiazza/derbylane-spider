Using Scrapy to extract dog racing data
=======================================

This project contains 2 spiders that can be used to extract entries 
and results data from the `Derby Lane website <http://www.derbylane.com/>`_.

My goal with this project was to replace a Java desktop app I wrote 10 
years ago. The app still works fine but the hassle of constantly updating 
the local JRE encouraged me to look for an alternative solution. In 
particular, I hoped to find a Pythonic solution since I have been using
it more and more in recent years. I was quite happy to discover 
`Scrapy <https://scrapy.org/>`_.

I was surprised how much simpler the Python version of this app turned
out to be. That can be attributed to Python syntax being much simpler
and the power of the Scrapy framework.

Scraping off the Derby Lane website is possible because they post data
in TEXT format. The spiders in this project just use a known 
URL pattern to extract raw data, parse it and then insert it into the
appropriate table in a MySQL database. The schema consists of the
following 2 tables:

* DogEntry
  .. image:: https://i.imgur.com/m75PZBY.png

* DogResult
  .. image:: https://i.imgur.com/m75PZBY.png

There are 2 spiders in this project: entries and results. There are
also corresponding scrapy.Item subclasses defined for each type of
data being scraped. A Pipeline has been defined that uses an instance
of the  Repository class to insert data into the database.

I welcome all comments and suggestions. Happy scraping!
