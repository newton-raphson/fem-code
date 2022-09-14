
import matplotlib.pyplot as plt
import numpy as np


print("\n The program computes deflection for 1 to 100 elements")
print("Diameter at left End(mm):")
D1=float(input())
print("Diameter at Right End(mm):")
D2=float(input())
print("Length of the bar (mm):")
L=float(input())
print("Magnitude of the Load(KN):")
P=float(input())
print("Modulus of Elasticity(GPa):")
E=float(input())

de_l=[]
elem=np.linspace(1,100,100)
k=0
for i in range(100):
    x=(np.linspace(0,i+1,i+2)*L)/(i+1)
    Dm=D1-((D1-D2)/L)*x
    AvD=0.5*np.add(np.append(Dm,0),np.append(0,Dm))
    AvD2=np.delete(AvD,[0,(len(AvD)-1)])
    Am=np.pi/4*np.square(AvD2)
    de=(P*L)/((i+1)*Am*E)
    deflection=de.sum()
    de_l.append(deflection) 

fig = plt.figure()
plt.plot(elem,de_l,'g')
fig.suptitle('Deflection vs no. Finite Elements')
plt.xlabel('Elements')
plt.ylabel('Deflection')
plt.show()   
ev=(4*P*L)/(np.pi*D1*D2*E)
print("The actual deflection is ")
print(ev)
