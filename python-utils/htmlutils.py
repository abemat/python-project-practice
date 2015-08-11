
import requests
#from bs4 import BeautifulSoup, Comment

r = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")

if r.status_code == 200:
	f = open('banner.dat', 'w')
	f.write(r.text)
	f.close()
	##comment = soup.findall(text=lambda text:isinstance(text,Comment))
	#print comment
	#print type(comment)
else:
	print "something is wrong with the connection"

'''
soup = BeautifulSoup(open("equality.html"))
comment = soup.findAll(text=lambda text:isinstance(text,Comment))

f = open('equality.dat','w')
f.write(comment[0])
f.close()
'''
