#!/usr/bin/python
import datetime
from BeautifulSoup import BeautifulSoup
import sys
import urllib2
import os.path
import tempfile
import urlparse
import tidy
import commands
import django.utils.dateformat
import re

today = datetime.date.today()		#+datetime.timedelta(days=-5)
#print today
monday = today - datetime.timedelta(days=today.weekday())
tomorrow = today + datetime.timedelta(days=1)

dotw = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

catering_url = "http://www.trin.cam.ac.uk/index.php?pageid=52"
page = urllib2.urlopen(catering_url)
neat = str(tidy.parseString(page.read()))
soup = BeautifulSoup(neat)

today2 = "%s %s" % ( str(django.utils.dateformat.format(today,"jS")), today.strftime("%B") )
tomorrow2 = "%s %s" % ( str(django.utils.dateformat.format(tomorrow,"jS")), tomorrow.strftime("%B") )

today1 = today.strftime("%A")
tomorrow1 = tomorrow.strftime("%A")

menu_urls = [urlparse.urljoin(catering_url,x.parent['href']) for x in soup.findAll(text="Hall Menu")]
print "%s %s" % (today1,today2)
for menu_url in reversed(menu_urls):
	#print menu_url
	f = tempfile.NamedTemporaryFile()
	g = urllib2.urlopen(menu_url)
	f.write(g.read())
	f.flush()

	cmd = "pdf2txt.py %s" % f.name
	status, output = commands.getstatusoutput(cmd)
#	print status,output
	f.close()

	if status != 0:
		raise Exception, output
	output=output.strip()

	filler = ["SHOULD YOU HAVE A FOOD ALLERGY PLEASE ADVISE THE CATERING MANAGER","DISHES MAY CONTAIN TRACES OF NUTS OR NUT BY-PRODUCTS","SOME OF THE FOOD PROVIDED AT THESE PREMISES CONTAINS INGREDIENTS PRODUCED FROM GENETICALLY MODIFIED SOYA BEANS AND MAIZE","FURTHER INFORMATION IS AVAILABLE FROM STAFF","Catering Department","MAY CONTAIN TRACES OF NUTS OR NUT BY-PRODUCTS"]

	for x in filler:
		output = output.replace(x,"")

	if today2 in output:

		pattern = "\D(?:%s)(.*?)(%s|$)" % (today2,"|".join(dotw))

		p = re.compile(pattern,re.IGNORECASE | re.DOTALL)

		x = p.search(output)
		if not x:
			continue

		words = x.groups()[0].strip()
		words = words.replace("\n \n \n \n","\n \n")
		print words
		import sys
		sys.exit()
		break
else:
	raise Exception
