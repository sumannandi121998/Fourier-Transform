#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:02:32 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x): #given box function
    if (-1<x<1):
        return 1
    else:
        return 0

xmin=-5 #minimum value of x
xmax=5 #maximum value of x
n=128 #no of discrete points
dx=(xmax-xmin)/(n-1) #distance between two consecutive points
x=np.zeros(n)
data1=np.zeros(n)

for i in range (n): #sampling the function in n discrete points
    x[i]=xmin+i*dx
    data1[i]=f(xmin+i*dx)
data2=np.pad(data1,(0,n-1)) #zero padding in sampled f(x) data
x=np.pad(x,(0,n-1)) #zero padding in x data
a=np.arange(64,192) #for shifting the graph along x axis
b=np.arange(n)
dft1=np.fft.fft(data2,norm='ortho') #dft of n points using numpy
data=dx*np.sqrt(2*n-1)*np.fft.ifft(dft1*dft1,norm='ortho') #convolution of box func with itself

plt.plot(x[b],data1,label='box function') #plotting box function
plt.plot(x[b],data.real[a],label='convolution of two box functions') #plotting convolution function
plt.title('x vs f(x) graph')
plt.xlabel('x', fontsize=13)
plt.ylabel('f(x)', fontsize=13)
plt.legend(fontsize=7,loc='upper left')
plt.show()
