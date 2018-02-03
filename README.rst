Using Scrapy to extract dog racing data from the Derby Lane website
===================================================================

This project contains 2 spiders that can be used to extract entries 
and results data from the `Derby Lane website <http://www.derbylane.com/>`_.

My goal with this project was to replace a Java desktop app I wrote 10 
years ago. The app still works fine but the constant hassle of constantly
updating the local JRE encouraged me to look for an alternative solution.
In particular, I hoped to find a Pythonic solution since I have been using
it more and more in recent years. I was quite happy to discover `Scrapy <https://scrapy.org/>`_.

Scraping data off the Derby Lane website is made possible by the fact that
they post both PDF and TXT format versions. The spiders in this project
just use a known URL pattern to extract raw data, parse it and then generate
CSV format.
