import numpy as np
import matplotlib.pyplot as plt

#Function
def initialBell(x):
	return np.where(x%1.<0.5, np.power(np.sin(2*x*np.pi),2),0)


#Variables
nt=50
nx=50
coeffdiff=15
dx=1./nx
dt=1./nt

x=np.linspace(0.0,1.0,nx+1)
t=np.linspace(0.0,1.0,nt+1)

phi=initialBell(x)
phiNew=phi.copy()
phiOld=phi.copy()

#############################################################

#Energy equation

#FTCS for the first time-step
#loop over space

coeff=(coeffdiff*dt)/(dx**2)

for j in xrange(1,nx):
	phi[j]=phiOld[j]-coeff*(phiOld[j+1]-2*phiOld[j]+phiOld[j-1])

#Apply periodic boundary condition

phi[0]=phiOld[0]-coeff*(phiOld[1]-2*phiOld[0]+phiOld[nx-1])
phi[nx]=phi[0]


for n in xrange(1,nt):
#loop over space
	for j in xrange(1,nx):
		phiNew[j]=phiOld[j]-coeff*(phi[j+1]-2*phi[j]+phi[j-1])

#Apply periodic boundary condition

	phiNew[0]=phiOld[0]-coeff*(phi[1]-2*phi[0]+phi[nx-1])
	phiNew[nx]=phiNew[0]

#update phi for the next time-step

	phiOld=phi.copy()
	phi=phiNew.copy()

#Plot the solution in comparison to the analitic solution

#plt.plot(x, initialBell(x-t), 'k',label='analytic')
plt.plot(x,phi,'b',label='CTCS')
plt.legend('x')
plt.legend(loc='best')
plt.ylabel('$\phi$')
plt.axhline(0,linestyle=':',color='black')
plt.show()
