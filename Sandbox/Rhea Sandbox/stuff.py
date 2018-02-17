"""
	$Id$
	
	Just checking out some modules
"""

import datetime
from datetime import date
import logging

# set a logging level
logging.getLogger().setLevel (logging.DEBUG)
logging.basicConfig(format='%(created)s %(funcName)s:%(lineno)s [%(levelname)s] %(message)s')

import time

logging.info ("This is fyi - starting my stuff program")

'''
def foo():
	logging.debug ("Doing date now")
	print datetime.date.today()
	print date.today()
	print datetime.datetime.now()

foo()
logging.debug ("Doing time now")
print time.time()
time.sleep (1)
print time.time()

logging.debug ("Ending my stuff program")
'''

from lxml import html
import urllib2,urllib

url = 'https://www.last.fm/music/+free-music-downloads'
logging.info ("Getting page : %s", url)
response = urllib2.urlopen (url)
response = response.read()
tree = html.fromstring(response)
dls = tree.find_class ("chartlist-download-button")
for dl in dls:
	href =  dl.get ("href")
	logging.info ("Downloading %s", href)
	(filename,header) = urllib.urlretrieve(href)
	logging.info ("Downloaded %s", filename)
	break
#print tree
#print response
#music = "https://dl.last.fm/static/1518885423/131211148/db05047c9154656424108164fd991f6254a13537bfa2ce750807a5079ed23f3b/Death+Grips+-+Get+Got.mp3"
#(fileName,header) = urllib.urlretrieve(music, "downloaded.mp3")
#logging.info ("Downloaded file %s with header:%s", fileName, header)

