##Assignment 2.14
##Samundra Karki 074 BME 634
##The problem requires to have a node always in the midpoint
import matplotlib.pyplot as plt
import numpy as np


print("\n The program computes deflection for 1 to 100 elements")
print("Length at left End(mm):")
H1=float(input())
print("Length at Right End(mm):")
H2=float(input())
print("Length of the bar (mm):")
L=float(input())
print("Magnitude of the Load(KN):")
P=float(input())
print("Modulus of Elasticity(GPa):")
E=float(input())
MaxN=int(input('Even Number of Elements:'))
de_l=[]
pos=[]
ReL=[]
ReR=[]
for nel in range(2,MaxN,2):
    nnd=nel+1
    gstiff=np.zeros([nnd,nnd])
    gload=np.zeros(nnd)
    disp=np.zeros(nnd)
    gload[int(nel/2)]=P
    x=(np.linspace(0,nel,nel+1)*L)/(nel)
    el=L/(nel)
    Hm=H1-((H1-H2)/L)*x
    AvH=0.5*np.add(np.append(Hm,0),np.append(0,Hm))
    AvH2=np.delete(AvH,[0,(len(AvH)-1)])
    k=(np.square(AvH2)/el)*E
    for i in range(nel):
        kel=np.array([[k[i],-k[i]],[-k[i],k[i]]])
        gstiff[np.ix_([i,i+1],[i,i+1])]=np.add(gstiff[np.ix_([i,i+1],[i,i+1])],kel)
    disp1=np.linalg.solve(gstiff[1 : nnd-1,1 : nnd-1],gload[1 : nnd-1])
    disp[1 : nnd-1]=disp1
    Force=gstiff@disp
    de_l.append(disp[int(nel/2)])
    pos.append(nel)
    ReL.append(Force[0])
    ReR.append(Force[nel])
print("The reaction at left end is:\n")
print(ReL)
print("The reaction at right end is:\n")
print(ReR)
fig = plt.figure()
plt.plot(pos,de_l,'g')
fig.suptitle('Deflection vs no. Finite Elements')
plt.xlabel('Elements')
plt.ylabel('Deflection')
plt.show() 