#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:21:45 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x): #given sinc function
    if x==0:
        return 1
    else:
        return np.sin(x)/x
xmin=-50 #minimum value of x
xmax=50 #maximum value of x
n=1024 #no of discrete points
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
def g(x): #analytical FT function
    if -1<x<1:
        return np.sqrt(np.pi/2)
    else:
        return 0
for j in range (n):
    data2[j]=g(k[j]) #values of analytical FT function at different k 
plt.plot(k[i],data2[i],label='analytical FT of sinc function') #plotting analytical FT function
plt.xlim(-4,4)
plt.title('k vs f(k) graph')
plt.xlabel('k', fontsize=13)
plt.ylabel('f(k)', fontsize=13)
plt.legend(fontsize=6,loc='upper left')
plt.show()