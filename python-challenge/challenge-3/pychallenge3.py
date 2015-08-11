import re
import requests

key =''
f = open('equality.dat','r')

for line in f:
	match = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', line)
	if match:
		key = key + match[0]

f.close()

nexturl = 'http://www.pythonchallenge.com/pc/def/'+key+'.html'
print nexturl

r = requests.get(nexturl)
if r.status_code == 200:
	print "successful : ", nexturl
else:
	print "not successful : ", nexturl