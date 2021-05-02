# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:01:16 2021

@author: Yuchen Ye
"""
import matplotlib.pyplot as plt
from skimage import data,color
import scipy as sp
import numpy as np
astro = data.astronaut()

def compress_ycbcr(a,k): # k is downsample factor
    b = color.rgb2ycbcr(a) # we assume the input image is in RGB--if not, this will
                            # not give the correct output
    
    
    x = b[:,:,0]
    
    y = b[:,:,1][::k,::k].repeat(k,axis=0).repeat(k,axis=1)
    
    z = b[:,:,2][::k,::k].repeat(k,axis=0).repeat(k,axis=1)
    
    img1 = np.dstack((x,y,z))
    img = color.ycbcr2rgb(img1)
    plt.figure()
    plt.imshow(img,)

compress_ycbcr(astro,1) #Original RGB color
compress_ycbcr(astro,4) #Downsampled x4
compress_ycbcr(astro,16) #Downsampled x16
compress_ycbcr(astro,64) #Downsampled x64



#Just random attempts below

b = color.rgb2ycbcr(astro)

k = 4
    
    
y = b[:,:,0]
    
cb = b[:,:,1][::k,::k].repeat(k,axis=0).repeat(k,axis=1)
    
cr = b[:,:,2][::k,::k].repeat(k,axis=0).repeat(k,axis=1)








y1 = sp.fftpack.dct(y)

cb1 = sp.fftpack.dct(cb)

cr1 = sp.fftpack.dct(cr)

yi = sp.fftpack.dct(y1/1000,type=3)

cbi = sp.fftpack.dct(cb1/1000,type=3)

cri = sp.fftpack.dct(cr1/1000,type=3)