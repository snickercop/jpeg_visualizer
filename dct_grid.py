# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:19:32 2021

@author: Allegra Copland
"""

from scipy.fftpack import dct, idct
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

np.seterr(all='warn')

def plot_rgb(a):
    plt.figure()
    plt.subplot(1,3,1)
    plt.imshow(a[:,:,0] ,cmap=plt.cm.Reds)
    plt.subplot(1,3,2)
    plt.imshow(a[:,:,1] ,cmap=plt.cm.Greens)
    plt.subplot(1,3,3)
    plt.imshow(a[:,:,2] ,cmap=plt.cm.Blues)

#custom colormaps:

def rgb(a):
        if len(a.shape)==2:
            return "Sorry, this is a grayscale image!"
        return a[:,:] #returns [R,G,B]
    
def fit(a):
    a /= np.max(np.abs(a))
    a = (a+1)/2
    return a

#from here https://stackoverflow.com/questions/34890585/in-scipy-why-doesnt-idctdcta-equal-to-a
nrm="ortho"
def dct2(a):
    return dct(dct(a.T,norm=nrm).T,norm=nrm)

def idct2(a):
    return idct(idct(a.T,norm=nrm).T,norm=nrm)

def binim(a):
    plt.figure()
    plt.axis("off")
    plt.imshow(a,cmap=plt.cm.gray,vmin=0.0,vmax=1.0)

def grid_binim(a):
    bweight = 1
    bcolor = .8
    #shift = 0
    n = a.shape[0]
    size = n*n + 2*n*bweight
    out = np.zeros((size,size))
    for i in range(n):
        pixeli = n*i+(i)*bweight*2
        out[pixeli,:] = bcolor
        out[pixeli+n+1,:] = bcolor
        for j in range(n):
            pixelj = n*j+(j)*bweight*2
            out[pixeli:pixeli+n+1,pixelj] = bcolor
            out[pixeli:pixeli+n+1,pixelj+n+1] = bcolor
            out[pixeli+1:pixeli+n+1,pixelj+1:pixelj+n+1] = a[i][j]
         
    binim(out)
    return out

blank = np.zeros((4,4,4,4))
def dct_grid():
    grid = np.full((8,8,8,8),0.0)
    f = 1
    for i in range(0,8):
        for j in range(0,8):
            for x in range(0,8):
                for y in range(0,8):
                    # got equation from https://www.dspguide.com/ch8/4.htm#:~:text=The%20basis%20functions%20are%20a,form%20the%20time%20domain%20signal.
                    grid[i][j][x][y] += ((np.cos(f*np.pi*x*i/8.0) + np.cos(f*np.pi*y*j/8.0))/4)+0.5
    return grid

def recalibrate(a):
    mx = np.ndarray.max(a)
    out = a/(2*mx)+.5
    return out

def recal_grid(a):
    out = np.ndarray(a.shape)
    for i in range(8):
        for j in range(8):
            out[i][j] = recalibrate(a[i][j])
    return out

def dct_grid_re(): # reverse engineered dct grid
    grid = np.zeros((8,8,8,8))
    spot = np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            spot[i][j] = 1
            grid[i][j] = idct2(spot)
            spot[i][j] = 0
            #binim(grid[i][j])
    return grid

grid = dct_grid_re()
grid_binim(recalibrate(grid)) # outputs dct coefficient grid
