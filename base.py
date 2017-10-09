
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
from PIL import Image



#http://docs.opencv.org/3.0-beta/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html?highlight=initundistortrectifymap

#camera matrix [fx, _,  cx], [_, fy, cy[, [_, _, _]]

class default:
    pass

default.camera_img_size = (640, 480)

default.camera_mtx = np.array([[352.819, 0.0, 309.883], 
                                 [0.0, 330.388, 241.680], 
                                 [0.0, 0.0, 1.0]])

#camera distortion coefficients (k1, k2, k3, k4)
default.camera_dist = np.array([[-0.04651275799849617], 
                                  [-0.00205612795823227], 
                                  [-0.017685697995019633], 
                                  [0.012977195205127278]])

