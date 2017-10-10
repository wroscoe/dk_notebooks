
# coding: utf-8

# In[ ]:


#base.py - default modules and variables imported by notebooks

import os
import glob

import pandas as pd
import numpy as np
import cv2

get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plt
from matplotlib import pylab
%pylab inline
pylab.rcParams['figure.figsize'] = (10, 6)

from PIL import Image




#http://docs.opencv.org/3.0-beta/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html?highlight=initundistortrectifymap

#camera matrix [fx, _,  cx], [_, fy, cy[, [_, _, _]]

class default:
    pass

default.camera_img_size = (640, 480)

default.camera_mtx = np.array([[ 193.06670785,    0.        ,   75.9227073 ],
                               [   0.        ,  194.50832782,   60.13050291],
                               [   0.        ,    0.        ,    0.25      ]])

#camera distortion coefficients (k1, k2, k3, k4)
default.camera_dist = np.array([[ -1.65260527],
                               [  5.7104838 ],
                               [-23.89860722],
                               [ 55.40237623]])





def show_imgs(array_plots, cmap=None):
    """
    Convenience function to show many images in a single plot
    """
    
    plot_count = len(array_plots)
    
    fig, ax = plt.subplots(1, plot_count, figsize=(15, 6), squeeze=False,
                             subplot_kw={'adjustable': 'box-forced'})

    axoff = np.vectorize(lambda ax:ax.axis('off'))
    axoff(ax)

    for i, data in enumerate(array_plots):        
        ax[0, i].imshow(data['array'], cmap=cmap)
        ax[0, i].set_title(data.get('name', ' '))