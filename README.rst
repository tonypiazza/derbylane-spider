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

There are 2 spiders in this project: entries and results. There are also corresponding 
scrapy.Item subclasses defined for each type of data being scraped. A Pipeline has been 
defined that uses an instance of the Repository class to insert data into the database.

Setup the environment
#####################

We assume you already have installed Python3, PIP and MySQL. If not, you need to do that. 
After that, be sure to start the MySQL server on your machine. Now you are ready to setup 
the environment by following these steps:

1. Use the mysql command-line tool to create the schema:

.. code-block:: shell

  mysql -u username -p password < schema.sql

*where username and password are the MySQL credentials to use when connecting*

2. For those running on Windows, you will need to install the `Build Tools for Visual Studio 
   <https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15>`_.

   .. image:: https://i.imgur.com/uCUgro3.png

3. Use pip to install all of the dependencies:

.. code-block:: shell

  pip install -r requirements.txt

4. Modify derbylane/settings.py to specify your MySQL connection details:

.. code-block:: python

  MYSQL_USER = 'root'
  MYSQL_PASSWORD = 'password'
  MYSQL_HOST = 'localhost'
  MYSQL_DATABASE = 'derbylane'

*uncomment only the ones you need to modify*

Running the application
#######################

From the project folder, you can execute Scrapy as follows:

.. code-block:: shell

  scrapy crawl results
  scrapy crawl entries

I welcome all comments and suggestions. Happy scraping!
