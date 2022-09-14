##This program is for linearly connected spring
##Assignment 2.11
##Samundra Karki 074 BME 634
import numpy as np

nel =int(input("Enter number of springs:"))
k=np.zeros(nel)
print("\n Provide stiffness")
for i in range(nel):
    k[i]= float(input("Stiffness of the spring KN/m:"))
nod=nel+1
gload=np.zeros(nod)
print("\n Provide nodes  and corresponding loads")
tmp=input("Node with load: ")
while tmp!='':
    pos=int(tmp)
    gload[pos-1]=float(input("Corresponding Load(N): "))
    tmp=input("Node with load: ")
disp=np.zeros(nod)
gstiff=np.zeros([nel+1,nel+1])
for i in range(nel):
     kel=np.array([[k[i],-k[i]],[-k[i],k[i]]])
     gstiff[np.ix_([i,i+1],[i,i+1])]=np.add(gstiff[np.ix_([i,i+1],[i,i+1])],kel)

disp1=np.linalg.solve(gstiff[1 :,1 :],gload[1 :])
disp[1 :]=disp1
Force=gstiff@disp
Fel=k*np.subtract(np.delete(disp,[0]),np.delete(disp,[len(disp)-1]))
print('Displacement of nodes')
print(disp)
print('Force at each nodes')
print(Force)
print('Force at each element')
print(Fel)

