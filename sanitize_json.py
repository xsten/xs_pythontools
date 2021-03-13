#!/usr/bin/python

import json
import sys

# sanitize_json.py
#
# remove errors in json due to incorrect usage of sed for example...
# e.g.  input :
# {
#"mykey":{
#    "subkey":"subvalue",
# "subkey2","subvalue2"},
#   "bobo":"bibi",}
#
# output :
# {"my first key":{"first subkey":"subvalue","subkey2": "subvalue2"},"bobo":"bibi"}
#
# if input is really to far from json, error is returned
#


# remove whitespaces in a string, except quoted whitespaces
def stripwhite(text):
	lst=text.split('"')
	for i,item in enumerate(lst):
		if not i%2:
			lst[i]=lst[i].replace(' ','')
	return '"'.join(lst)


# puts everything on one line
# toto='{\n"my key":{\n    "subkey":"subvalue",\n "subkey2": "subvalue2"},\n   "bobo":"bibi",}'
toto=sys.stdin.read()
toto=toto.replace('\n','')
# removes white spaces
toto=stripwhite(toto)
# remove unuseful trailing ","
toto=toto.replace(',}','}')
toto=toto.replace(',]',']')

# now try to pretty print
try:
        toto_parsed=json.loads(toto)
        print(json.dumps(toto_parsed,indent=1,sort_keys=True))
except Exception as e:
        print('Error parsing:\n'+toto)
        print('\nException caught:\n'+str(e))
        exit(1)

exit(0)
