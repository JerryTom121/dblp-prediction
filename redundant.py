from collections import defaultdict
hashnodes = {}
file=open('edgelist95.txt','r')
outfile= open('weightedlist95.txt','w')
for line in file:
	nodelist = line.split(' ')
	a,b= nodelist
	s=str(a)+' '+str(b)
	if s not in hashnodes:
		hashnodes[s] =  1
	else:
		hashnodes[s] =  hashnodes[s] + 1
			
#end

print(len(hashnodes))
for item in hashnodes:
	c,d = item.split(' ')
	c=c.strip('\n')
	d=d.strip('\n')
	#print(c +' '+ d+'  '+ str(hashnodes[item]))
	if (hashnodes[item] > 1):
		outfile.write(c+ ' ' + d + ' ' + str(hashnodes[item]) +'\n')
	#print(" fdf ")


			
	
	
	
