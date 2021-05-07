# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:43:53 2021

@author: Allegra Copland
"""
import matplotlib.pyplot as plt
from skimage import data,color
import numpy as np
astro = data.astronaut()
from utility import get_blocks,grid_im,LOCAL_IMAGE
from dct_grid import dct_on_grid,dct2,idct_on_grid

# before qmatrix application, the qmatrix is pre-scaled by multiplying by some int btw 1 and 112.

# 0: "for a quality of 50% as specified in from the original JPEG Standard". 
#     https://en.wikipedia.org/wiki/JPEG
# 1: "default matrix" https://web.archive.org/web/20111031231449/http://www.john-wiseman.com/technical/multifig_2.htm
qlist_dict = {0:[ 16, 11, 10, 16, 24, 40, 51, 61,
                  12, 12, 14, 19, 26, 58, 60, 55,
                  14, 13, 16, 24, 40, 57, 69, 56,
                  14, 17, 22, 29, 51, 87, 80, 62,
                  18, 22, 37, 56, 68,109,103, 77,
                  24, 35, 55, 64, 81,104,113, 92,
                  49, 64, 78, 87,103,121,120,101,
                  72, 92, 95, 98,112,100,103, 99],
              1:[  8, 16, 19, 22, 26, 27, 29, 34,
                  16, 16, 22, 24, 27, 29, 34, 37,
                  19, 22, 26, 27, 29, 34, 34, 38,
                  22, 22, 26, 27, 29, 34, 37, 40,
                  22, 26, 27, 29, 32, 35, 40, 48,
                  26, 27, 29, 32, 35, 40, 48, 58,
                  26, 27, 29, 34, 38, 46, 56, 69,
                  27, 29, 35, 38, 46, 56, 69, 83]}

def qmatrix(index):
    oglist = qlist_dict.get(index)
    out = np.zeros((8,8))
    for i in range(64):
        dig1 = int(i/8)
        dig2 = i % 8 # "digits" of the base 8 number equal to i
        out[dig1,dig2] = oglist[i]
    return out

