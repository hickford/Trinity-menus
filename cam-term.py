#!/usr/bin/python
from datetime import date,timedelta
"The Michaelmas Term shall begin on 1 October and shall consist of eighty days, ending on 19 December. The Lent Term shall begin on 5 January and shall consist of eighty days, ending on 25 March or in any leap year on 24 March. The Easter Term shall begin on 10 April and shall consist of seventy days ending on 18 June, provided that in any year in which full Easter Term begins on or after 22 April the Easter Term shall begin on 17 April and end on 25 June."

def term():
    """Return current Cambridge term or False if out of term"""
    today = date.today()
    year = today.year
    if date(year,10,1)<=today<=date(year,12,19):
        return "Michaelmas"
    elif date(year,1,5)<=today<=date(year,1,5)+timedelta(days=80):
        return "Lent"
    elif date(year,4,22)<=today<=date(year,6,25):
        return "Easter"
    return False


if __name__=="__main__":
    import sys
    if term():
        sys.exit(0)
    else:
        sys.exit(1) # this goes to standard error
