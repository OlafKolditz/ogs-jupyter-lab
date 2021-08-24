import numpy as np
from scipy import special
import matplotlib.pyplot as plt

#Parameters
l2=np.log(2)
#tdt12=td/t12
tdt12=(0,1,30,120)
print('tdt12:',tdt12)
#ttd=t/td
ttd=np.logspace(-2,3,num=100)
print(ttd)
#Analytical solution
for t in tdt12:
	A=np.sqrt(t*l2)
	print('A:',A)
	#B=0.5*np.sqrt(1/ttd)
	B=0.5/np.sqrt(ttd)
	print('B:',B)
	C=np.sqrt(l2*ttd*t)
	print('C:',C)
	uexc=0.5*(np.exp(-A)*special.erfc(B-C) + np.exp(A)*special.erfc(B+C))
	print('uexc:',uexc)
	plt.plot(ttd,uexc,label="$t_d$/$t_{1/2}$="+str(t))

#Plots 
plt.xscale('log')
plt.yscale('log')
plt.ylim(1e-5)
plt.ylabel('$C(t,L)$/$C_0$')
plt.xlabel('$t$/$t_d$')
plt.title('Diffusion-Decay-Process (analytical solution)')
plt.legend()
plt.grid(linestyle='dotted')
plt.show()
plt.savefig('reference-diffusion-decay.png')#,dpi=300)