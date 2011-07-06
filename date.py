#!/usr/bin/python
import datetime
from django.conf import settings
settings.configure(USE_I18N=False)
import django.utils.dateformat
today = datetime.date.today()
print str(django.utils.dateformat.format(today,"l jS F Y")) 
#print "%s %s %s %s" % (django.utils.dateformat.format(today,"M"), django.utils.dateformat.format(today,"jS"), django.utils.dateformat.format(today,"M"), django.utils.dateformat.format(today,"Y"))
