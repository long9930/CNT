from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
x,y,z,xprime,yprime,nx,ny,nz=[],[],[],[],[],[],[],[]
dx,dy=3.0/2,sqrt(3)/2
#input
n=8.0
m=5.0
Nr=1.0
Ch=sqrt(3*(n**2+m**2+n*m))
T=sqrt(3)*Ch/Nr
theta=pi/6-arccos((2*n+m)*sqrt(3)*0.5/Ch)
costheta=cos(theta)
sintheta=sin(theta)
#print Ch,T
bxl=59.9
bxr=bxl+Ch
byu=0.1
byd=byu-T
r=Ch/(pi*2)
for i in range(0,100):
    for j in range (0,100):
        x.append(0+dx*(i+j)),x.append(1+dx*(i+j))
        y.append(0+dy*(i-j)),y.append(0+dy*(i-j))
        xprime.append(x[-2]*costheta+y[-2]*sintheta)
        xprime.append(x[-1]*costheta+y[-1]*sintheta)
        yprime.append(y[-2]*costheta-x[-2]*sintheta)
        yprime.append(y[-1]*costheta-x[-1]*sintheta)
#print xprime,yprime
plot(xprime,yprime)
show()
for i in range(len(xprime)):
    if bxl<=xprime[i]<bxr and byd<yprime[i]<=byu:
        nx.append(xprime[i]),ny.append((yprime[i]-byd)*1.42)
plot(nx,ny,'.')
show()

for i in range(len(nx)):
    alpha=(nx[i]-bxl)/r
    nx[i]=r*sin(alpha)*1.42
    nz.append(r*cos(alpha)*1.42)

f=open('SWCNT{}{}'.format(n,m),'w')
f.write('{}\n' .format(len(nx)))
for i in range(len(nx)):
    f.write('  C'+'   {}   {}   {}\n' .format(nx[i],nz[i],ny[i]))
f.close()
fig=figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot(nx,nz,ny,'bo')
#xlim(bxl,bxr)
#ylim(byd,byu)
show()
