Trinity College hall menu script
==========
The script `lunch.py` downloads the hall menus from Trinity College Cambridge's [Catering Department](http://www.trin.cam.ac.uk/index.php?pageid=52) and prints the current day's meals. Usefully, a cronjob can email daily menus to a mailing list.

Usage
-------
    Usage: lunch.py [options]
    
    Options:
      -h, --help            show this help message and exit
      -f FORWARD, --forward=FORWARD
                            simulate n days in the future
      -v, --verbose         extra output useful for debugging

Python modules imported
-------
BeautifulSoup, tidy and [PDFMiner](http://www.unixuser.org/~euske/python/pdfminer/index.html)

N.B. The layout analysis in PDFMiner changed between versions. I found PDFMiner-20100424 worked well.

Installation on the [SRCF](http://www.srcf.ucam.org/)
-------
1. Clone this repository
2. Link (or copy) the .py scripts to `~/bin`
3. Install [PDFMiner-20100424](http://pypi.python.org/pypi/pdfminer/20100424) locally, ie. `python setup.py install --home=~`
4. Export some environment variables, append `export PYTHONPATH=~/lib/python:"${PYTHONPATH}"; export PATH=~/bin:"${PATH}";` to `~/.profile`
5. Test `lunch.py`
6. Test the cronjob command below
7. Install the cronjob `crontab -e`
8. Through the administrative interface of the mailing list (links below) permit your email address to post to the list

Cronjob
-------
This emails the menus (assuming the `lunch.py` is successful) to either the in-term or out-of-term mailing list

    30 5 * * * export PYTHONPATH=~/lib/python:"${PYTHONPATH}"; export PATH=~/bin:"${PATH}"; TMPFILE=`mktemp`; lunch.py > $TMPFILE && mail -s "Trinity College hall menu `date.py`" `if cam-term.py ; then echo "tchm-announce@srcf.ucam.org"; else echo "tchm-outofterm@srcf.ucam.org";fi;` < $TMPFILE

Mailing lists
-------

* In term: tchm-announce@srcf.ucam.org - subscribe at http://www.srcf.ucam.org/mailman/listinfo/tchm-announce , admin at http://www.srcf.ucam.org/mailman/admin/tchm-announce
* Out of term: tchm-outofterm@srcf.ucam.org - subscribe at http://www.srcf.ucam.org/mailman/listinfo/tchm-outofterm , admin at http://www.srcf.ucam.org/mailman/admin/tchm-outofterm
