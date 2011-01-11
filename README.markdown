Example cronjob:
30 5 * * * PYTHONPATH=~/lib/python:"${PYTHONPATH}"; export PYTHONPATH; PATH=~/bin:"${PATH}"; TMPFILE=`mktemp`; lunch.py > $TMPFILE && mail -s "Trinity College hall menu" tchm-announce@srcf.ucam.org < $TMPFILE

