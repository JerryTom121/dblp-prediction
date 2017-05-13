import networkx as nx


f=open('weightedlist95.txt','r')
out=open('features95.txt','w')

g = nx.read_weighted_edgelist("weightedlist95.txt", delimiter=' ', encoding='utf-8')
print("graph created")


out1=open('labels95.txt','w')
f1=f.readlines()
'''for x in f1:
	a,b,c=x.split(' ')
	fet= ''
	pred1 = nx.adamic_adar_index(g,[(a,b)])
	pred2 = nx.jaccard_coefficient(g, [(a, b)])
	pred3 = nx.preferential_attachment(g, [(a, b)])
	
	for item in pred1:
		x,y,z=item
		fet=fet+str(z)+' '
		#print x + ' '+ y +' ' + str(z)
	
	for item in pred2:
		x,y,z=item
		fet=fet+str(z)+' '
		#print x + ' '+ y +' ' + str(z) 
	
	
	for item in pred3:
		x,y,z=item
		fet=fet+str(z)
		#print x + ' '+ y +' ' + str(z) 
	 
	out.write( a + ' '+ b +' '+fet +'\n')'''
	
auth1=[]
auth2=[]
	
for x in f1:
	a,b,c=x.split(' ')
	auth1.append(a)
	
	auth2.append(b)

length=len(auth1)
print length

for i in range(0,length):
	for j in range(0,length):
		lab=0
		if (auth1[i]!=auth2[j]):
			
			fet= ''
			d=0
			f=0
			
			pred1 = nx.adamic_adar_index(g,[(auth1[i],auth2[j])])
			pred2 = nx.jaccard_coefficient(g,[(auth1[i],auth2[j])])
			pred3 = nx.preferential_attachment(g,[(auth1[i],auth2[j])])
		
			for item in pred1:
				x,y,z=item
				if(z==0.0):
					d=1
				fet=fet+str(z)+' '
				#print x + ' '+ y +' ' + str(z)
			
			for item in pred2:
				x,y,z=item
				if(z==0.0):
					f=1
				fet=fet+str(z)+' '
				#print x + ' '+ y +' ' + str(z) 
			
			
			for item in pred3:
				x,y,z=item
				fet=fet+str(z)+' '
				#print x + ' '+ y +' ' + str(z) 
			
			 
			if(d==0 and f==0):
				if (i==j):
					lab=1
					out1.write(str(lab)+'\n')
				else:
					out1.write('0\n')
			
				out.write( x + ' '+ y +' '+fet +'\n')
		
		






