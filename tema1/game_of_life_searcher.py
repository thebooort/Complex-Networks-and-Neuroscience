#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:42:40 2018

@author: booort
"""

#game of life, life searcher


import numpy
import matplotlib.pyplot as plt

# rules
def play_life(a):
    xmax, ymax = a.shape
    b = a.copy() # copy grid & Rule 2
    for x in range(xmax):
        for y in range(ymax):
            n = numpy.sum(a[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - a[x, y]
            if a[x, y]:
                if n < 2 or n > 3:
                    b[x, y] = 0 # Rule 1 and 3
            elif n == 3:
                b[x, y] = 1 # Rule 4
    return(b)

# space ship searcher: compares 3x3 grid searching for the same pattern
def check_life(a,b):
    xmax, ymax =a.shape
    result=False
    for x in range(xmax-2):
        for y in range(ymax-2):
                sample_1=a[numpy.ix_([x,x+1,x+2],[y,y+1,y+2])]
                sample_2=(sample_1==b).all()
                if sample_2==True:
                    result=True
    return result

# initial conditions
experiment=numpy.zeros((6,6))
experiment[0,2]=1
experiment[1,2]=1
experiment[1,0]=1
experiment[2,2]=1
experiment[2,1]=1

plt.figure(figsize=(6, 6))
plt.title('initial conditions time={}'.format(0))
plt.pcolormesh(experiment,cmap='binary')
plt.show           

# our spaceship that is hopefully alive 
space_ship=numpy.zeros((3,3))
space_ship[0,2]=1
space_ship[1,2]=1
space_ship[1,0]=1
space_ship[2,2]=1
space_ship[2,1]=1            

plt.figure(figsize=(6, 6))
plt.title('spaceship')
plt.pcolormesh(space_ship,cmap='binary')
plt.show 

# temporal evolution + searching

for i in range(100):
    experiment = play_life(experiment)
    detection = check_life(experiment,space_ship)
    print(detection)
    if detection==True:
        plt.figure(figsize=(6, 6))
        plt.title('found! time: {}' .format(i))
        plt.pcolormesh(experiment,cmap='binary')
        plt.show  

plt.figure(figsize=(6, 6))
plt.title('finals conditions')
plt.pcolormesh(experiment,cmap='binary')
plt.show          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            