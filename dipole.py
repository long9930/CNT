from pylab import *
nk=64
factor=0.529**2/nk
result=[]
with open ('/Users/zhongqulong/Documents/SWCNT/swcnt_8-0_1632/8-absorption/eigenvalues.dat','r') as f:
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
    y.append(result[n][1]*factor)
    if y[n]>2: print(y[n],x[n])
    

plot(x,y,'b.',label='64k 16v17c')
#plot(x2,y2,'r.',label='64k 8v8c')
#plot(x3,y3,'g.',label='64k 4v4c')
#plot(x4,y4,'y.',label='256k 4v4c')
xlabel('Eigenvalues in eV')
ylabel('Dipole Square in $\AA^2$')
title('Eigenstates of exciton')
legend()
show()

