#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:19:02 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x): #constant function
    return 1
xmin=-50 #minimum value of x
xmax=50 #maximum value of x
n=512 #no of discrete points
dx=(xmax-xmin)/(n-1) #distance between two consecutive points
x=np.zeros(n)
data=np.zeros(n)
data2=np.zeros(n)

for i in range (n): #sampling the function in n discrete points
    x[i]=xmin+i*dx
    data[i]=f(xmin+i*dx)

dft=np.fft.fft(data,norm='ortho') #dft of n points using numpy
k=2*np.pi*np.fft.fftfreq(n,d=dx) #values of k in fourier space
i = np.argsort(k) #aranging the values of k in ascending order

factor=np.exp(-1j*k*xmin)
ft=dx*np.sqrt(n/(2*np.pi))*factor*dft #numerical FT of the sinc function
plt.plot(k[i],ft.real[i],label='numerical FT of sinc function') #plotting the result
plt.xlim(-5,5)
plt.title('k vs f(k) graph')
plt.xlabel('k', fontsize=13)
plt.ylabel('f(k)', fontsize=13)
plt.legend(fontsize=8,loc='upper left')
plt.show()