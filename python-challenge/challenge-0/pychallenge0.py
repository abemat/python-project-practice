import re
import urllib2
link = str(2**38)
url0 = "http://www.pythonchallenge.com/pc/def/0.html"
new_link = re.sub(r'0', link, url0)
print new_link
