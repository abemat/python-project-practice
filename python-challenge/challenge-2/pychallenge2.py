import urllib2
#from collections import Counter

f = file('ocr_data.dat','r')
lines = [line for line in f]
one_line = ''.join(lines)
f.close()

unik_list = list(set(one_line))
counted = {item: False for item in unik_list}

key = ''
for char in one_line:
	if counted[char] is True:
		pass
	else: 
		total = one_line.count(char)
		counted[char] = True
		if total == 1:
			key = key + char

#key = ''.join([char for char in one_line if one_line.count(char) is 1]) <- original idea but TOO LONG to process !
#print Counter(one_line) <- counting using Counter is faster but the result is not in original order

print key
nexturl = 'http://www.pythonchallenge.com/pc/def/'+key+'.html'
if urllib2.urlopen(nexturl).getcode() == 200:
	print "YOU ARE FUCKING RIGHT! YEEEEHAAAAAA"




