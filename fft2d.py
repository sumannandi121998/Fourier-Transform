#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:59:42 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

def f(x,y): #given gaussian function
    return np.exp(-((x*x)+(y*y)))

xmin=ymin=-50 #minimum values of x and y
xmax=ymax=50 #maximum values of x and y
n=128 #no of discrete points
dx=(xmax-xmin)/(n-1) #distance between two consecutive points
data=np.zeros((n,n))
for i in range (n): #sampling the function in n^2 discrete points
    for j in range (n):
        data[i,j]=f(xmin+i*dx,ymin+j*dx)
dft=np.fft.fft2(data,norm='ortho') #2d dft using numpy
k1=2*np.pi*np.fft.fftfreq(n,d=dx) #values of k_x in fourier space
k2=2*np.pi*np.fft.fftfreq(n,d=dx) #values of k_y in fourier space
X,Y = np.meshgrid(k1, k2) #n^2 no of points in fourier space
factor=np.exp(-1j*(X*xmin+Y*ymin))
ft=dx*dx*(n/(2*np.pi))*factor*dft #numerical FT of that function
fig = plt.figure()
ax = plt.axes(projection='3d') #for 3d plot
ax.scatter(X, Y, ft.real,s=0.1,label='numerical FT of gaussian function',color='r') #plotting the result
def g(x, y): #analytical FT of the given function
    return 0.5*np.exp(-0.25*((x*x)+(y*y)))
ax.scatter(X, Y, g(X,Y),s=0.05,label='analytical FT of gaussian function',color='c') #plotting analytical FT function
ax.set_title('3D plot of FT function')
ax.set_xlabel('k1')
ax.set_ylabel('k2')
ax.set_zlabel('f(k1,k2)')
ax.legend(fontsize=5,loc='upper left')
plt.show()