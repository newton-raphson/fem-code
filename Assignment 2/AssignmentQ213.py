##Assignment 2.13
##Samundra Karki 074 BME 634
import numpy as np
nel=3
nnd=4
D=np.zeros(nel)
L=np.zeros(nel)
E=np.zeros(nel)
for i in range(nel):
    print("")
    D[i]=float(input(f'Enter Diameter for {i+1}th element (mm): '))
    L[i]=float(input(f'Enter the length for {i+1}th element (mm): '))
    E[i]=float(input(f'Enter the Modulus of rigidity for {i+1}th element (GPa): '))
Ppos=3
Qpos=2
gstiff=np.zeros([nnd,nnd])
gload=np.zeros(nnd)
disp=np.zeros(nnd)   
gload[Ppos-1]=float(input("Load P: Provide node 3 corresponding loads (KN) :"))
gload[Qpos-1]=float(input("Load Q: Provide node 2 corresponding loads (KN) :"))
k=((np.pi/4*D**2)*E)/L
for i in range(nel):
     kel=np.array([[k[i],-k[i]],[-k[i],k[i]]])
     gstiff[np.ix_([i,i+1],[i,i+1])]=np.add(gstiff[np.ix_([i,i+1],[i,i+1])],kel)
disp1=np.linalg.solve(gstiff[1 : nnd-1,1 : nnd-1],gload[1 : nnd-1])
disp[1 : nnd-1]=disp1
Force=gstiff@disp
Fel=k*np.subtract(np.delete(disp,[0]),np.delete(disp,[len(disp)-1]))
stress=Fel/(np.pi/4*D**2*10**(-3))
print('Displacement of nodes')
print(disp)
print('Force KN at each nodes')
print(Force)
print('Force KN at each element')
print(Fel)
print('Stress MPa at each element')
print(stress)
