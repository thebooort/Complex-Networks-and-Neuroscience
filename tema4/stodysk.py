#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:10:16 2018

@author: booort
"""

import scipy as sp
import pylab as plt
from scipy.integrate import odeint
import numpy as np
#constantes del articulo original de tsodysk
tau_rec = 800
tau_in = 3
tau_m =40
R_in = 500
A_SE = 150
t = np.arange(0, 100, 0.1)

def delta_(t):
    return 10*(t>9) - 10*(t>10) + 10*(t>12) - 10*(t>13) + 10*(t>16) - 10*(t>17) + 10*(t>20) - 10*(t>21) + 10*(t>24) - 10*(t>25)+ 10*(t>59) - 10*(t>60)+ 10*(t>69) - 10*(t>70)+ 10*(t>79) - 10*(t>80)+ 10*(t>89) - 10*(t>90)+ 10*(t>99) - 10*(t>100)                                                           


def T_M_Model(X, t, tau_in, tau_m, R_in, A_SE):
    x,y,z,V = X
    
    dxdt = z/tau_rec-V*x*delta_(t)
    dydt = -y/tau_in-V*x*delta_(t)
    dzdt = y/tau_in-z/tau_rec
    dVdt = 1/tau_m*(-V+R_in*A_SE*y)
    return dxdt,dydt,dzdt,dVdt

X_0=[0.02,0.02,0.02,0]
sol = odeint(T_M_Model, X_0, t, args=(tau_in, tau_m, R_in, A_SE))
V=sol[:,3]
x=sol[:,0]
y=sol[:,1]
z=sol[:,2]
plt.plot(t,V)
plt.plot(t,delta_(t))
plt.show()


