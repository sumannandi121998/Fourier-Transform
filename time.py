#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:16:13 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np
import time

def f(n): #this function returns first n integer
    return np.arange(n)
t1=np.zeros(96)
t2=np.zeros(96)
for i in range (4,100):
    start = time.time()
    fft=np.fft.fft(f(i)) #fft using numpy function
    t1[i-4] = (time.time() - start) #counting time for each loop
l=np.arange(4,100) #range of n
for n in range (4,100):
    g=np.zeros(n)
    start = time.time()
    for i in range (n):
        for k in range (n):
            g[i]=g[i]+k*np.exp(-1j*2*np.pi*i*k/n) #dft using direct code
    t2[n-4] = (time.time() - start) #counting time for each loop
plt.plot(l,t1,label='time taken using numpy fft') #plotting the result for np.fft
plt.plot(l,t2,label='time taken using direct code') #plotting the result for direct code
plt.title('n vs time graph')
plt.xlabel('n', fontsize=13)
plt.ylabel('time', fontsize=13)
plt.legend(fontsize=8,loc='upper left')
plt.show()