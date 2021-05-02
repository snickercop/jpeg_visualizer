# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:28:57 2021

@author: Allegra Copland
"""

# Here I will need you to make some functions that can help visually represent what happens during a YCbCr color transform, 
# as well as write a function to perform that transform.

import matplotlib.pyplot as plt
from skimage import data,color
import scipy.signal as sg
import numpy as np

# You can use any color image you want for testing, 
# but I've included one from the skimage library to start with.
# You can view an image by, e.g., running plt.imshow(astro)
astro = data.astronaut()
cwheel = data.colorwheel()

# Remember how in the imaging unit we split a picture into RGB color channels?
# Here is a function that plots the 3 channels of the given image a. 
# In this case, it colors the first channel red, and so on, so that it illustrates RGB channels in an image.
def plot_rgb(a):
    plt.figure()
    plt.subplot(1,3,1)
    plt.imshow(a[:,:,0] ,cmap=plt.cm.Reds)
    plt.subplot(1,3,2)
    plt.imshow(a[:,:,1] ,cmap=plt.cm.Greens)
    plt.subplot(1,3,3)
    plt.imshow(a[:,:,2] ,cmap=plt.cm.Blues)

# Here is a similar function for YCbCr channels
def plot_ycbcr(a):
    b = color.rgb2ycbcr(a) # we assume the input image is in RGB--if not, this will
                            # not give the correct output
    plt.figure()
    plt.subplot(1,3,1)
    plt.imshow(b[:,:,0], cmap=plt.cm.gray)
    plt.subplot(1,3,2)
    plt.imshow(b[:,:,1][::10,::10] ,cmap=plt.cm.Blues)
    plt.subplot(1,3,3)
    plt.imshow(b[:,:,2][::10,::10] ,cmap=plt.cm.Reds)
    
plot_ycbcr(astro)




