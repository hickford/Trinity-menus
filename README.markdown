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
2. Copy/link the two .py scripts to ~/bin
3. Install [PDFMiner-20100424](http://pypi.python.org/pypi/pdfminer/20100424) locally, ie. `python setup.py install --home=~`
4. Test `lunch.py`
5. Test the cronjob command
6. Install the cronjob below `crontab -e`

Cronjob
-------
This emails the menus (if the script is successful) to a [mailing list](http://www.srcf.ucam.org/mailman/listinfo/tchm-announce)

    30 5 * * * export PYTHONPATH=~/lib/python:"${PYTHONPATH}"; export PATH=~/bin:"${PATH}"; TMPFILE=`mktemp`; lunch.py > $TMPFILE && mail -s "Trinity College hall menu `date.py`" `if cam-term.py ; then echo "tchm-announce@srcf.ucam.org"; else echo "tchm-outofterm@srcf.ucam.org";fi;` < $TMPFILE

Mailing lists
-------

* tchm-announce@srcf.ucam.org - subscribe at http://www.srcf.ucam.org/mailman/listinfo/tchm-announce
* tchm-outofterm@srcf.ucam.org - subscribe at http://www.srcf.ucam.org/mailman/listinfo/tchm-outofterm
