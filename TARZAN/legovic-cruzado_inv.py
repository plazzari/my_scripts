# Legovic-Cruzado Model: dynamics of biological systems in which one species growth according to droop quota model in function of two resources.

# Using:

#dN1/dt  = D*(No1-N1)      - V1*N1/(N1+k1)*B
#dN2/dt  = D*(No2-N2)      - V2*N2/(N2+k2)*B

#dPN1/dt = V1*N1/(N1+k1)*B - D*PN1  
#dPN2/dt = V2*N2/(N2+k2)*B - D*PN2  

#dB/dt   = (mu*[1-max(q1/(PN1/B),q2/(PN2/B))] -D) * B

#with the following notations:
#N1  = Resource1
#N2  = Resource2
#PN1 = Resource1 conc in Phytoplankton
#PN2 = Resource2 conc in Phytoplankton
#B   = cell biomass

# We will use X = [N1,N2,PN1,PN2,B] to describe the state of the system

from numpy import *
import pylab as p
#Definition of parameters
D   = 0.59        ;
No1 = 3           ; No2 = 30; 
V1  = 12.3*10**(-9); V2  = 341*10**(-9);
k1  = 0.2           ; k2  = 5.6;
mu  = 1.35          ;
q1  = 1.64*10**(-9); q2  =45.4*10**(-9);

def dX_dt(X, t=0):
    """ Return the growth rate of quota model. """
    return array([ D*(No1-X[0])           - V1*X[0]/(X[0]+k1)*X[4],
                   D*(No2-X[1])           - V2*X[1]/(X[1]+k2)*X[4],
                   V1*X[0]/(X[0]+k1)*X[4] - D*X[2]                ,
                   V2*X[1]/(X[1]+k2)*X[4] - D*X[3]                ,
                   (mu*(1-max(q1/(X[2]/X[4]),q2/(X[3]/X[4]))) -D) * X[4] ])
# Now we will use the scipy.integrate module to integrate the ODEs. This module offers a method named odeint, which is very easy to use to integrate ODEs: 
def dY_dt(Y, t=0):
    """ Return the growth rate of quota model. """
    return array([ - (D*(No1-Y[0])           - V1*Y[0]/(Y[0]+k1)*Y[4]),
                   - (D*(No2-Y[1])           - V2*Y[1]/(Y[1]+k2)*Y[4]),
                   - (V1*Y[0]/(Y[0]+k1)*Y[4] - D*Y[2]                ),
                   - (V2*Y[1]/(Y[1]+k2)*Y[4] - D*Y[3]                ),
                   - (mu*(1-max(q1/(Y[2]/Y[4]),q2/(Y[3]/Y[4]))) -D) * Y[4] ])
# Now we will use the scipy.integrate module to integrate the ODEs. This module offers a method named odeint, which is very easy to use to integrate ODEs: 

from scipy import integrate
t = linspace(0, 40,  1000)              # time
t2 = linspace(0, 20,  500)              # time
t_r = linspace(40, 0,  1000)            # time reverse
t_r2 = linspace(20, 0,  500)            # time reverse
X0 = array([No1,No2,q1,q2,100000])                     # initial conditions: 10 rabbits and 5 foxes
X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)
infodict['message']                     # >>> 'Integration successful.'
Y0 = array([No1,No2,q1,q2,100000])                     # initial conditions: 10 rabbits and 5 foxes
print(Y0)
nut1,nut2,qt1,qt2,cells = X.T
Y0=array([nut1[-1],nut2[-1],qt1[-1],qt2[-1],cells[-1]])
print(Y0)
Y,infodict = integrate.odeint(dY_dt, Y0, t, full_output=True)
infodict['message']                     # >>> 'Integration successful.'
Z0=array([nut1[500],nut2[500],qt1[500],qt2[500],cells[500]])
print(Z0)
Z,infodict = integrate.odeint(dY_dt, Z0, t2, full_output=True)
infodict['message']                     # >>> 'Integration successful.'


# infodict is optional, and you can omit the full_output argument if you don't want it. Type "info(odeint)" if you want more information about odeint inputs and outputs.
R1=q1*D*mu*k1/(V1*(mu-D)-q1*D*mu)
R2=q2*D*mu*k2/(V2*(mu-D)-q2*D*mu)

# We can now use Matplotlib to plot the evolution of the system: 
nut1,nut2,q1,q2,cells = X.T
nut1_r,nut2_r,q1_r,q2_r,cells_r =Y.T
nut1_r2,nut2_r2,q1_r2,q2_r2,cells_r2=Z.T

print(cells[-1])
print(cells_r[0])
print(cells_r2[0])
f1 = p.figure()
p.subplot(3, 1, 1)
p.plot(t, cells, 'r-', label='nut1')
#p.plot(t_r, cells_r, 'g-', label='nut1')
p.plot(t_r2, cells_r2, 'm-', label='nut1')
p.grid()
p.xlabel('time(days)')
p.ylabel('biomass B')
p.yscale('log')
p.xlim([0.,11.])
p.subplot(3, 1,2)
p.plot(nut1,nut2, 'k-', label='nut1',alpha=0.3)
#p.plot(nut1_r,nut2_r, 'k.', label='nut1')
p.plot(nut1_r2[0:350],nut2_r2[0:350], 'g:', label='nut1')
p.plot([R1,R1],[R2,30],'r--',lw=2)
p.plot([R1,3 ],[R2,R2],'r--',lw=2)

p.xlabel(r'$R_p (\mu mol P L^{-1})$')
p.ylabel(r'$R_n (\mu mol N L^{-1})$')
p.subplot(3, 1,3)
p.plot(t,q2/q1, 'k-', label='nut1',alpha=0.3)
p.plot(t_r2,q2_r2/q1_r2, 'g:', label='nut1')
p.ylim([0.,30.])
p.xlabel('time(days)')
p.ylabel(r'$phytoplankton N:P, Q_N/Q_P$')
p.tight_layout()
f1.savefig('Lego_1.png')
p.show()


