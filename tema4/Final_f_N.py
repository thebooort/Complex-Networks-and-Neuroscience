#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:25:30 2018

@author: booort
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import scipy as sp


def F_N_Model(X, t, phi, alpha, betta, I_iny):
    V, U = X
    
    dVdt = V-V**3/3-U+I_iny
    dUdt = phi*(V+alpha-betta*U)
    return dVdt, dUdt

def V_nullcline(V, I_iny):
    return V - 1./3*V**3 + I_iny

def U_nullcline(U,alpha, betta):
    return -alpha + betta*U

#Cte values from wikipedia
alpha=0.7
betta=0.8
phi=0.08
I_iny=[0.2,0.4,0.8,2.0]

for i in range(0,4):
    
    t = np.arange(0, 100, 0.1)
    X_0=[-0.5,-0.5]
    sol = odeint(F_N_Model, X_0, t,args=(phi,alpha,betta,I_iny[i]))
    
    # calculo y resolucion de las nulclinas
    x = sp.arange(-3, 3, 0.1)
    y = sp.arange(-4, 4, 0.1)
    v_nul= V_nullcline(x,I_iny[i])
    u_nul = U_nullcline(y,alpha,betta)
    
    
    #plot de las nulclinas
    fig, ax = plt.subplots(figsize=(6,9))
    ax.set_title("inyecte I value = %i" %I_iny[i])
    plt.subplot(211)
    plt.rc('grid', linestyle=":", color='black')
    plt.plot(x,v_nul,'grey',linestyle="--",linewidth=2,label='nulclina V')
    plt.plot(u_nul,y,'grey',linestyle=":",linewidth=2,label='nulclina U')
    plt.ylabel('u')
    plt.xlabel('v')
    #plot de la solucion
    plt.plot(sol[:, 0],sol[:, 1],  'b', label='trayectoria')
    plt.legend(loc='best')
    
    plt.grid()
    ax.set_title("inyecte I value = %i" %I_iny[i])
    plt.subplot(212)
    plt.plot(t,sol[:, 0],  'b', label='V')
    plt.xlabel('t')
    plt.legend(loc='best')
    ax.set_title("inyecte I value = %i" %I_iny[i])
    plt.show()



