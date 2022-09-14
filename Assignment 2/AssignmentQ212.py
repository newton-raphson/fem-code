##Assignment 2.12
##Samundra Karki 074 BME 634
import numpy as np

nel =10
k=np.zeros(nel)
print("\n Provide stiffness")
for i in range(nel):
    k[i]= float(input("Stiffness of the spring KN/m:"))
nod=8
Ppos=3
Qpos=5
gload=np.zeros(nod)
gload[Ppos-1]=float(input("Load P: Provide node 3 corresponding loads (N) :"))
gload[Qpos-1]=float(input("Load Q: Provide node 5 corresponding loads (N) :"))
disp=np.zeros(nod)
gstiff=np.zeros([nod,nod])
conn=np.array([[0,1],[1,2],[1,3],[2,3],[2,5],[3,4],[4,5],[4,6],[5,6],[6,7]])
for i in range(nel):
    j=conn[i,0]
    l=conn[i,1]
    kel=np.array([[k[i],-k[i]],[-k[i],k[i]]])
    gstiff[np.ix_([j,l],[j,l])]=np.add(gstiff[np.ix_([j,l],[j,l])],kel)
    
disp1=np.linalg.solve(gstiff[1 : nod-1,1 : nod-1],gload[1 : nod-1])
disp[1 : nod-1]=disp1
Force=gstiff@disp
Fel=np.zeros(nel)
for i in range(nel):
    j=conn[i,0]
    l=conn[i,1]
    Fel[i]=k[i]*(disp[l]-disp[j])
print('Displacement of nodes')
print(disp)
print('Force at each nodes')
print(Force)
print('Force at each element')
print(Fel)

