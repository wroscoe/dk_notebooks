
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
get_ipython().magic('pylab inline')
pylab.rcParams['figure.figsize'] = (10, 6)

from PIL import Image




#http://docs.opencv.org/3.0-beta/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html?highlight=initundistortrectifymap

#camera matrix [fx, _,  cx], [_, fy, cy[, [_, _, _]]

class default:
    pass

default.camera_img_size = (160, 120)

default.camera_K = np.array([
    [ 85.14204933,   0.        ,  76.75324351],
    [  0.        ,  79.80749069,  59.4252282 ],
    [  0.        ,   0.        ,   1.        ]])

#camera distortion coefficients (k1, k2, k3, k4)
default.camera_D = np. array([
    [-0.02025494],
    [ 0.00573737],
    [-0.02515587],
    [ 0.01317606]
])

#camera distortion coefficients (k1, k2, k3, k4)
default.camera_R = np.eye(3) * np.array([1,1,1.5])

class cv_util:
    
    @staticmethod
    def undistort(distorted_img, K, D, undistorted_size=None, R=np.eye(3)):
        """Undistort an image using the fisheye model"""

        if undistorted_size is None:
            undistorted_size = (distorted_img.shape[1], distorted_img.shape[0])

        map1, map2 = cv2.fisheye.initUndistortRectifyMap(
            K,
            D,
            R,
            K,
            undistorted_size, 
            cv2.CV_16SC2
        )

        undistorted_img = cv2.remap(
            distorted_img,
            map1,
            map2,
            interpolation=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_CONSTANT
        )

        return undistorted_img




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