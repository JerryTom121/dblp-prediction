import numpy as np
t=np.loadtxt('features95.txt')
out=open('only_features95.txt','w')


for i in t:
	a,b,c=i[2:5]
	out.write(str(a)+' '+str(b)+' '+str(c)+'\n')

