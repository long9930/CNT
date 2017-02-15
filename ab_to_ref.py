from numpy import *
from matplotlib.pyplot import *
energy,absorp=[],[]
index=[]
print("start")
f=open('./abs_data','r')
for line in f.readlines():
    newline=line.split()
    energy.append(float(newline[0]))
    absorp.append(float(newline[1]))
f.close()
x=range(500,2000)
for singular in x:
    summ=0
    for i in range(1,len(energy)):
        if energy[i]<(singular-5) or energy[i]>(singular+5):  
            summ+=log(1.0-absorp[i])/(energy[i]**2-singular**2)*(energy[i]-energy[i-1])
    fact=1239.84/(2*pi**2*20)
    n=1-fact*summ*1000
    index.append(n)
print("finish")
plot(x,index)
show()
