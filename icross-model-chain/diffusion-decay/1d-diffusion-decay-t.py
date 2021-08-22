import numpy as np
from scipy import special
import matplotlib.pyplot as plt

#Parameters
C0=1
D=1e-11
rho=2394 #kg/m3
Kd=0.5
Kd=0
porosity=0.12
R=1+(rho*Kd/porosity)
print('R:',R)
t12=2.3e+6 * 365*86400 #in seconds
L=20
td=L*L*R/D
print('td:',td)
print('td/t12:',td/t12)
l=np.log2(2)/t12
la=np.absolute(l)
#Time
years = (100,1000,10000,1e+5,1e+6)
#Geometry
N=250;x0=0.;xN=20;
x=np.linspace(x0,xN,N)
#Analytical solution
A=np.sqrt(la*R/D)
print('A:',A)
for t in years:
	ts=t*365*86400
	print('ts/td:',ts/td)
	B=C0/2*np.sqrt(R/D/ts)
	#B=0.5*np.sqrt(R/D/T)
	print('B:',B)
	C=np.sqrt(la*ts)
	print('C:',C)
	uexc=C0/2*(np.exp(-x*A)*special.erfc(x*B-C) + np.exp(x*A)*special.erfc(x*B+C))
	plt.plot(x,uexc,label="t in [a] = "+str(t))
#Plots 
plt.ylabel('C')
plt.xlabel('x')
plt.title('Diffusion-Decay-Process (analytical solution)')
plt.legend()
plt.grid(linestyle='dotted')
plt.show()
plt.savefig('reference-diffusion-decay.png',dpi=300)