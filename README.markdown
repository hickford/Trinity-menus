Trinity College hall menu script
==========
This script downloads the hall menus from Trinity College Cambridge's [Catering Department](http://www.trin.cam.ac.uk/index.php?pageid=52) and extracts the current day's meals.

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

Note PDFMiner-20100424 is best.

Cronjob
-------
This emails the menus (if the script is successful) to a [mailing list](http://www.srcf.ucam.org/mailman/listinfo/tchm-announce)
    30 5 * * * PYTHONPATH=~/lib/python:"${PYTHONPATH}"; export PYTHONPATH; PATH=~/bin:"${PATH}"; TMPFILE=`mktemp`; lunch.py > $TMPFILE && mail -s "Trinity College hall menu `date.py`" `if cam-term.py ; then echo "tchm-announce@srcf.ucam.org"; else echo "tchm-outofterm@srcf.ucam.org";fi;` < $TMPFILE

Mailing lists
-------

* tchm-outofterm@srcf.ucam.org
* tchm-announce@srcf.ucam.org

