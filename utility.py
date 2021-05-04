# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:44:18 2021

@author: Allegra Copland
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from skimage import data,color
from skimage.transform import rescale
astro = data.astronaut()
normalize = matplotlib.colors.Normalize(vmin=0.0,vmax=1.0)
LOCAL_IMAGE = plt.imread("bernal_medium.jpg") # change to use your own image. styles.png is included in this repo.

# Up or down-scales the colors in an image to fit between 0 and 1
def recalibrate(a):
    mx = np.ndarray.max(a)
    mn = np.ndarray.min(a)
    if mx == mn:
        return 1
    shifted = a + (0-mn)
    out = shifted/(mx-mn)
    return out

# Similar to recalibrate, but works on a 4d array (2d array of 2d images)
# It normalizes each image separately.
def recal_grid(a):
    out = np.ndarray(a.shape)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            out[i][j] = recalibrate(a[i][j])
    return out

# Prints an image in black and white
def binim(a):
    plt.figure()
    plt.axis("off")
    plt.imshow(recalibrate(a),cmap=plt.cm.gray)

# def grid_binim(rawa):
#     a = recalibrate(rawa)
#     bweight = 1
#     bcolor = .8
#     #shift = 0
#     blsize = a.shape[3] # size of each block
#     bldim = a.shape[:2]
#     pixdim = [(bldim[i]*a.shape[i] + 2*bldim[i]*bweight) for i in range(2)]
#     out = np.zeros((pixdim[0],pixdim[1]))
#     for i in range(bldim[0]):
#         pixeli = blsize*i+(i)*bweight*2
#         out[pixeli,:] = bcolor
#         out[pixeli+blsize+1,:] = bcolor
#         for j in range(bldim[1]):
#             pixelj = blsize*j+(j)*bweight*2
#             out[pixeli:pixeli+blsize+1,pixelj] = bcolor
#             out[pixeli:pixeli+blsize+1,pixelj+blsize+1] = bcolor
#             out[pixeli+1:pixeli+blsize+1,pixelj+1:pixelj+blsize+1] = a[i][j]
         
#     binim(out)
#     return out

def grid_im(a, cmap=None, recal=True, dtype=None, show=True, title=None):
    if recal:
        a = recal_grid(a)
    bweight = 1
    bcolor = 0
    #shift = 0
    blsize = a.shape[3] # size of each block
    bldim = a.shape[:2]
    pixdim = [(bldim[i]*blsize + 2*bldim[i]*bweight) for i in range(2)]
    out = np.zeros((pixdim[0],pixdim[1]),dtype=dtype)
    for i in range(bldim[0]):
        pixeli = blsize*i+(i)*bweight*2
        out[pixeli,:] = bcolor
        out[pixeli+blsize+1,:] = bcolor
        for j in range(bldim[1]):
            pixelj = blsize*j+(j)*bweight*2
            out[pixeli:pixeli+blsize+1,pixelj] = bcolor
            out[pixeli:pixeli+blsize+1,pixelj+blsize+1] = bcolor
            out[pixeli+1:pixeli+blsize+1,pixelj+1:pixelj+blsize+1] = a[i][j]
    if show:
        plt.figure()  
        plt.title(title)
        plt.imshow(out,cmap=cmap)
    return out



def get_blocks(a, dtype=None): # only works on 2d arrays whose dimensions are divisible by 8
    h,w = a.shape
    blockh = int(h/8)
    blockw = int(w/8)
    blocks = np.ndarray((blockh,blockw,8,8),dtype='uint8')
    for i in range(blockh):
        for j in range(blockw):
            blocks[i][j] = a[i*8:i*8+8,j*8:j*8+8]
    return blocks
    
# debug zone
styles = plt.imread("styles.jpg")
ycbcr = color.rgb2ycbcr(styles)
blocks = [get_blocks(ycbcr[:,:,i]) for i in range(3)]
# grid_im(blocks[0], cmap=plt.cm.gray)
testblock = blocks[0][5][6]
# binim(testblock)
# print(recalibrate(testblock))