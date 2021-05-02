# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:44:18 2021

@author: Allegra Copland
"""

import matplotlib.pyplot as plt
import numpy as np

# Prints an image in black and white
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

# Up or down-scales the colors in an image to fit between 0 and 1
def recalibrate(a):
    mx = np.ndarray.max(a)
    out = a/(2*mx)+.5
    return out

# Similar to recalibrate, but works on a 4d array (2d array of 2d images)
# It normalizes each image separately.
def recal_grid(a):
    out = np.ndarray(a.shape)
    for i in range(8):
        for j in range(8):
            out[i][j] = recalibrate(a[i][j])
    return out

def get_blocks(a): # only works on 2d arrays whose dimensions are divisible by 8
    h,w = a.shape
    blockh = int(h/8)
    blockw = int(w/8)
    blocks = np.ndarray((blockh,blockw))
    for i in range(blockh):
        for j in range(blockw):
            blocks[i][j] = a[i:i+8][j:j+8]
    return blocks
    
    