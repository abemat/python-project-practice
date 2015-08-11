import requests
import re
import time

first_key = '63579'
key_list = [first_key]

baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nexturl = baseurl+first_key

for i in range(143,420):
	#print "link no (",i,") :",nexturl
	time.sleep(0.1)
	r = requests.get(nexturl)
	write_string = "link no (" + str(i) + ") :" + nexturl + " " + r.text
	print write_string
	next_key = re.findall(r'\d+', r.text)
	#print next_key[0]
	if next_key:
		nexturl = baseurl+next_key[0]
		#key_list.append(next_key[0])
	else:
		next_key = re.findall(r'\d+', nexturl)
		nexturl = baseurl+str(int(next_key[0])/2) 

	

