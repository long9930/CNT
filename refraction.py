from scipy.integrate import quad
#from scipy.special import 
from numpy import inf,pi,sqrt
import matplotlib.pyplot as plt
def integrand(x,y,gamma):
    return (x+1.27-y)/(x**0.5*((x+1.27-y)**2+gamma**2))
result1,result2,result3,result4=[],[],[],[]
z=[]
ecut=0.2 #eV
gamma1=0.02
gamma2=0.05
gamma3=0.1
gamma4=0.2
def refraction(x):
    return sqrt(1+4*pi*x)
    
for i in range (1,400):
    result1.append(refraction(quad(integrand,0,ecut,args=(i/100.0,gamma1))[0]*1.18))
    result2.append(refraction(quad(integrand,0,ecut,args=(i/100.0,gamma2))[0]*1.18))
    result3.append(refraction(quad(integrand,0,ecut,args=(i/100.0,gamma3))[0]*1.18))
    result4.append(refraction(quad(integrand,0,ecut,args=(i/100.0,gamma4))[0]*1.18))
    z.append(i/100.0)
#print result1[126],z[126]
plt.plot(z,result1,label='gamma=0.02 eV')
plt.plot(z,result2,label='gamma=0.05 eV')
plt.plot(z,result3,label ='gamma=0.1 eV')
plt.plot(z,result4,label='gamma=0.2 eV')
plt.xlabel('hw in eV')
plt.ylabel('index of refraction')
plt.legend()
plt.show()
