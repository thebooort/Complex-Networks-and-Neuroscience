#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:30:57 2018

@author: booort & stackoverflow answer
"""

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

# grid start
life = numpy.random.random_integers(0,1,(100,100))
plt.figure(figsize=(6, 6))
plt.pcolormesh(life)
plt.show
# evolution
for i in range(104):
    life = play_life(life)
plt.figure(figsize=(6, 6))
plt.pcolormesh(life)
plt.show
