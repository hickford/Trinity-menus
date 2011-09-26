#!/usr/bin/python
import datetime
today = datetime.date.today()

try:
  from django.conf import settings
  settings.configure(USE_I18N=False)
  from django.utils import dateformat
  print str(dateformat.format(today,"l jS F Y")) 
except ImportError:
  print today.isoformat()
