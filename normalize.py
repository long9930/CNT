
from scipy.integrate import quad
from scipy.special import gamma
from numpy import exp,inf,sqrt
import matplotlib.pyplot as plt
mr=4.5
a0=10.6
R=4.14
E0=0.68
Pgamma=0.6
lambda0=0.575
lzeta=2*Pgamma*R/(a0*lambda0)
def integrand1(x,Vlambda,zeta):
    return exp(-x-zeta/2)*(1+zeta/x)**Vlambda/gamma(1-Vlambda) 
def integrand2(zeta):
    return quad(integrand1,0,inf,args=(lambda0,zeta))[0]**2
result=quad(integrand2,lzeta,inf)
print result
x=[]
result1=[]

for zeta in range(int(lzeta*1000),2000):
    result1.append(integrand2(zeta/1000.0)*(2/(lambda0*a0*result[0])))
    x.append((zeta/1000.0-int(lzeta*1000)/1000.0)*lambda0*a0/2)
print result1[0]
plt.plot(x,result1,'.')
plt.show()

