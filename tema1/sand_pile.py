#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:55:48 2018

@author: booort
"""

import numpy
import matplotlib.pyplot as plt

# sandpile model 
def play_sand(a):
    xmax, ymax = a.shape
    b = a.copy() # copy grid
    for x in range(xmax-2):
        for y in range(ymax-2):
            if a[x, y]>=4:
                b[x,y]=0
                if (x>0 and y>0):
                    b[x+1,y] +=1
                    b[x-1,y] +=1
                    b[x,y+1] +=1
                    b[x,y-1] +=1
                """ # uncomment for additional features
                    b[x+1,y+1] +=1
                    b[x+1,y-1] +=0
                    b[x-1,y+1] +=0
                    b[x-1,y-1] +=1"""
  
    return(b)

# un comment to see random configuration
    
# sand = numpy.random.random_integers(0,4,(100,100))
    
# example of cascade
sand = numpy.zeros((100,100))
sand[49,49]=3
plt.figure(figsize=(7, 6))
plt.pcolormesh(sand)
plt.colorbar()
plt.show
# now let's play
""" #only adds sand if whole board is stable
for i in range(1000):
    sand[49,49]+=1
    sand_1 = play_sand(sand)
    if (sand_1==sand).all():
        sand[49,49]+=1
    else:
        sand = sand_1
    """
# adds every second

for i in range(5000):
    sand[49,49]+=1
    sand_1 = play_sand(sand)
    if (sand_1==sand).all():
        sand[49,49]+=1
    else:
        sand = sand_1
plt.figure(figsize=(7, 6))
plt.pcolormesh(sand)
plt.colorbar()
plt.show