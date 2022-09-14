import numpy as np
import matplotlib.pyplot as plt
nel=4
nnd=5
k=np.array([1000,2000,3000,1500])
conn=np.array([[0,1],[1,2],[2,3],[3,4]])
gstiff=np.zeros([nnd,nnd])
gload=np.zeros(nnd)
disp=np.zeros(nnd)
P=10

for i in range(nel):
    j=conn[i,0]
    l=conn[i,1]
    kel=np.array([[k[i],-k[i]],[-k[i],k[i]]])
    gstiff[np.ix_([j,l],[j,l])]=np.add(gstiff[np.ix_([j,l],[j,l])],kel)
    
print(gstiff)
gload[2]=P
gstiff1=gstiff[1:4,1:4]
gload1=gload[1:4]
disp1=np.linalg.solve(gstiff1,gload1)
disp[1:4]=disp1
Force=gstiff@disp
print(Force)
print(disp)