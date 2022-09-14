import matplotlib.pyplot as plt
import numpy as np


W1=float(input('Enter width of upper end (mm): \n'))
W2=float(input('Enter width of lower end (mm): \n'))
L=float(input('Enter the length of bar (mm):\n'))
t=float(input('Enter the thickness of bar (mm):\n'))
P=float(input('Enter the magnitude of load (kN):\n'))
r=float(input('Enter the speicific weight of the bar material (kN/m3):\n'))
r=r*1e-3
E=float(input('Enter the modulus of elasticity of the bar material (GPa):\n'))
ne=int(input('Maximum Number of Elements:'))
de_l=[]
elem=np.linspace(0,ne,ne)
k=0 
for i in range(ne):
    x=(np.linspace(0,i+1,i+2)*L)/(i+1)     
    Wm=W2-((W1-W2)/L)*x
    AvW=0.5*t*np.add(np.append(Wm,0),np.append(0,Wm))
    AvW2=np.delete(AvW,[0,(len(AvW)-1)])
    de_self=r*L**2/(2*E*(i+1))
    de_ex=0
    for j in range(i):
        tmp=(r*(L/(i+1))**2*AvW2[j+1 :].sum())/(E*AvW2[j])
        de_ex=de_ex+tmp+(P*(L/(i+1)))/(Wm[j]*t*E)
    deflection=de_self+de_ex
    de_l.append(deflection)
print(de_l[ne-1])
fig = plt.figure()
plt.plot(elem,de_l,'g')
fig.suptitle('Deflection vs no. Finite Elements')
plt.xlabel('Elements') 
plt.ylabel('Deflection')
plt.show()   
ev=(r/(2*E))*((L*W2/(W1-W2)*(L-(L*W2/(W1-W2)*np.log(W1/W2))))+L**2/2)
print("The actual deflection is ")
print(ev)
