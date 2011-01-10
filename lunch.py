#!/usr/bin/python
import datetime
from BeautifulSoup import BeautifulSoup
import urllib2
import urlparse
import tidy
import commands
import django.utils.dateformat
import re

#print "Hello lunchers! I presume most of you are going home this weekend so I will cease to send menus to this list. If you would like to receive hall menus after the end of term then subscribe to this second list http://www.srcf.ucam.org/mailman/listinfo/tchm-outofterm . Thank you."
#print "-Matt"
#print

today = datetime.date.today()
#print today
monday = today - datetime.timedelta(days=today.weekday())
tomorrow = today + datetime.timedelta(days=1)

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
	f = open("menu.pdf", "w")
	g = urllib2.urlopen(menu_url)
	f.write(g.read())
	f.close()

	cmd = "./pdf2txt.py menu.pdf"
	status, output = commands.getstatusoutput(cmd)

	output=output.strip()

	filler = ["SHOULD YOU HAVE A FOOD ALLERGY PLEASE ADVISE THE CATERING MANAGER","DISHES MAY CONTAIN TRACES OF NUTS OR NUT BY-PRODUCTS","SOME OF THE FOOD PROVIDED AT THESE PREMISES CONTAINS INGREDIENTS PRODUCED FROM GENETICALLY MODIFIED SOYA BEANS AND MAIZE","FURTHER INFORMATION IS AVAILABLE FROM STAFF","Catering Department"]

	for x in filler:
		output = output.replace(x,"")

	#print output

#	today2 = "%s %s" % ( str(django.utils.dateformat.format(today,"jS")), today.strftime("%B") )
#	tomorrow2 = "%s %s" % ( str(django.utils.dateformat.format(tomorrow,"jS")), tomorrow.strftime("%B") )

#	today1 = today.strftime("%A")
#	tomorrow1 = tomorrow.strftime("%A")

	if today2 not in output:
		continue
	else:
#		print "%s %s" % (today1,today2)
		
		pattern = "\D(?:%s)(.*)(?:%s)" % (today2, tomorrow1)
		if today.isoweekday() == 7:
			pattern = pattern = "\D(?:.*)(?:%s)(.*)$" % (today2)
		p = re.compile(pattern,re.IGNORECASE | re.DOTALL)

		x = p.search(output)
		if not x:
			continue

		words = x.groups()[0].strip()
		words = words.replace("\n \n \n \n","\n \n")
		print words
		break
