from numpy import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import *

f=open('/Users/zhongqulong/Documents/SWCNT/structures/SWCNT65','r')
f.readline()
x,y,z=[],[],[]
for content in f.readlines():
    print content
    content=content.split()
    x.append(float(content[1]))
    y.append(float(content[2]))
    z.append(float(content[3]))
f.close()

fig=figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot(x,y,z,'bo')
show()
