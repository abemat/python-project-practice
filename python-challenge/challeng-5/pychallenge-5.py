from collections import Counter

f = open("banner.dat",'r')
lines = [line for line in f]
lines.sort()
f.close()

analyse = Counter(lines)
print analyse

g = open('new_banner.dat','w')
for line in lines:
	g.write(line)
g.close()

