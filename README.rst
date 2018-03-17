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

+--------------------------------------------+--------------------------------------------+
| DogEntry                                   | DogResult                                  |
+--------------------------------------------+--------------------------------------------+
| .. image:: https://i.imgur.com/m75PZBY.png | .. image:: https://i.imgur.com/O26h0Co.png |
+--------------------------------------------+--------------------------------------------+

Setup the environment
#####################

We assume you already have Python3 and MySQL installed and running. If not,
you need to do that. To setup the environment for this application, you need 
to do the following:

1. Use the mysql command-line tool to create the schema for this application:

.. code-block:: shell

  mysql -u username -p password < schema.sql

*Where username and password are the MySQL credentials to use when connecting*

2. Use pip to install all of the dependencies for this project:

.. code-block:: shell

  pip install -r requirements.txt

There are 2 spiders in this project: entries and results. There are
also corresponding scrapy.Item subclasses defined for each type of
data being scraped. A Pipeline has been defined that uses an instance
of the  Repository class to insert data into the database.

Running the application
#######################

.. code-block:: shell

  source bin/activate
  scrapy crawl results
  scrapy crawl entries
  deactivate

I welcome all comments and suggestions. Happy scraping!
