from pylab import *

result=[]
with open ('/Users/zhongqulong/Documents/SWCNT/swcnt84/absorption_eh.dat','r') as f:
     f.readline()
     f.readline()
     f.readline()
     f.readline()
     for line in f:
     	 result.append(list(map(float,line.split())))

x = []
y = []
for n in range(len(result)):
    x.append(result[n][0])
    y.append(result[n][1])


plot(x,y,'-b',label='32k 8v8c')
#plot(x2,y2,'-r',label='64k 8v8c')
#plot(x3,y3,'-g',label='64k 4v4c')
#plot(x4,y4,'-y',label='256k 4v4c')

xlabel('Omega')
ylabel('Epsilon2')
title('absorption spectrum')
legend()
show()



