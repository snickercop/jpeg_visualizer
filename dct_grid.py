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
from utility import binim, recalibrate, recal_grid, normalize, LOCAL_IMAGE, get_blocks, grid_im
from color_transform import plot_rgb

np.seterr(all='warn')

def fit(a):
    a /= np.max(np.abs(a))
    a = (a+1)/2
    return a

#from here https://stackoverflow.com/questions/34890585/in-scipy-why-doesnt-idctdcta-equal-to-a
nrm=None
def dct2(a):
    return dct(dct(a.T,norm=nrm).T,norm=nrm)

def idct2(a):
    return idct(idct(a.T,norm=nrm).T,norm=nrm)


# for debugging
# blank = np.zeros((4,4,4,4))

def dct_on_grid(blocks):
    out = np.zeros((blocks.shape))
    for i in range(blocks.shape[0]):
        for j in range(blocks.shape[1]):
            out[i][j] = dct2(blocks[i][j])
    return out

def idct_on_grid(blocks):
    out = np.zeros((blocks.shape))
    for i in range(blocks.shape[0]):
        for j in range(blocks.shape[1]):
            out[i][j] = idct2(blocks[i][j])
    return out

# Creates the DCT cosine basis grid
def bases_grid(): # makes reverse engineered dct grid
    grid = np.zeros((8,8,8,8))
    spot = np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            spot[i][j] = 1
            grid[i][j] = idct2(spot)
            spot[i][j] = 0
            #binim(grid[i][j])
    return grid



