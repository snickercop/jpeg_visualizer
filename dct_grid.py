# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:19:32 2021

@author: Allegra Copland
"""

# Resources
    # https://www.youtube.com/watch?v=Q2aEzeMDHMA&t=1s video on JPEG compression from DCT onwards

from scipy.fftpack import dct, idct
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from utility import binim, grid_binim, recalibrate, recal_grid

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


# for debugging
# blank = np.zeros((4,4,4,4))

# Creates the DCT cosine basis grid
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
