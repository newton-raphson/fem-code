import numpy as np
import matplotlib.pyplot as plt
nel=7
nnd=5
E=200e9 #Pa
A=2.5e-3 #m^2
k=np.array([400,800,400])*1e3
conn=np.array([[0,1],[1,2],[2,3]])
gstiff=np.zeros([nnd,nnd])
gload=np.zeros(nnd)
disp=np.zeros(nnd)
de=12e-3
P=10

for i in range(nel):
    j=conn[i,0]
    l=conn[i,1]
    kel=np.array([[k[i],-k[i]],[-k[i],k[i]]])
    gstiff[np.ix_([j,l],[j,l])]=np.add(gstiff[np.ix_([j,l],[j,l])],kel)
    
print(gstiff)
disp[3]=de
F=gstiff@disp

gstiff1=gstiff[np.ix_([1,2],[1,2])]
F2=gload-F
gload1=F2([2,3])

disp1=np.linalg.solve(gstiff1,gload1)
disp[1:4]=disp1 
Force=gstiff@disp
print(Force)
print(disp)