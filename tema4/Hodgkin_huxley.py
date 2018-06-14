#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hodgkin-Huxley Model

@author: booort
"""

import scipy as sp
import pylab as plt
from scipy.integrate import odeint

# Constantes
C_m = 1.0  
g_l = 0.3
g_K = 36.0
g_Na = 120.0
V_l = -54.402
V_K = -77.0
V_Na = 50.0


def alpha_m(V):
    return 0.1*(V+40.0)/(1.0 - sp.exp(-0.1*(V+40.0)))


def alpha_n(V):
    return 0.01*(V+55.0)/(1.0 - sp.exp(-0.1*(V+55.0)))


def beta_h(V):
    return 1.0/(1.0 + sp.exp(-0.1*(V+35.0)))


def alpha_h(V):
    return 0.07*sp.exp(-0.05*(V+65.0))


def beta_m(V):
    return 4.0*sp.exp(-0.0556*(V+65.0))


def beta_n(V):
    return 0.125*sp.exp(-0.0125*(V+65))


#Definicion de F

def I_Na(V, m, h):
    return g_Na*m**3*h*(V-V_Na)


def I_K(V, n):
    return g_K*n**4*(V-V_K)


def I_L(V):
    return g_l*(V-V_l)

#  suma de la corrientes
#  externas y sinapticas entrando en la celula, cada una de ellas por unidad de
#  area de la membrana celular
def I_inj(t): 
    return 10*(t>20) - 10*(t>40) + 5*(t>65) - 5*(t>85) + 2.5*(t>105) - 2.5*(t>125) + 2.2*(t>140) - 2.2*(t>160)
    

#Tiempo donde vamos a integrar
t = sp.arange(0.0, 200.0, 0.1)

# Integracion numerica
def dALLdt(X, t):
    V, m, h, n = X
    
    dVdt = (I_inj(t) - I_Na(V, m, h) - I_K(V, n) - I_L(V)) / C_m
    dmdt = alpha_m(V)*(1.0-m) - beta_m(V)*m
    dhdt = alpha_h(V)*(1.0-h) - beta_h(V)*h
    dndt = alpha_n(V)*(1.0-n) - beta_n(V)*n
    return dVdt, dmdt, dhdt, dndt

X = odeint(dALLdt, [-65, 0.05, 0.6, 0.32], t)

#  Rescatamos el valor que nos interesa teniendo en cuenta el output de odeint

V = X[:,0]

plt.figure()
plt.plot(t, V, label=r'V (mV)')
plt.plot(t, I_inj(t),'r', label=r'I_iny ($\mu A/cm^2$)')
plt.xlabel('Time(msec)')
plt.legend(loc='upper right' )

plt.show()

plt.plot(V, (alpha_m(V)/(alpha_m(V)+beta_m(V))), label=r'V (mV)')
plt.show()



