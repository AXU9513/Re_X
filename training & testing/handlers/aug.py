import numpy as np
import random
from scipy.ndimage import rotate
import cv2


def augment_patch(x,y,patch_size):
    a = np.concatenate((x,y), axis=2)
    #Rotation
    angle = random.randint(0,30)*3
    if angle > 0:
        row_start = a.shape[1]//2-patch_size//2
        row_end = a.shape[1]//2+patch_size//2
        col_start = a.shape[0]//2-patch_size//2
        col_end = a.shape[0]//2+patch_size//2
        a = a[col_start:col_end,row_start:row_end,:]
    
    #Resize
    zoom = random.randint(75,100)/100
    a = np.resize(a, (int(a.shape[0]*zoom),int(a.shape[1]*zoom), a.shape[2]))
    a = cv2.resize(a,(patch_size,patch_size), interpolation = cv2.INTER_LINEAR)
    
    #Flipvert
    if random.randint(0,1) == 1:
        a = np.flipud(a)

    if random.randint(0,1) == 1:
        a = np.fliplr(a)

    # Histogram Equalization
    c1, c2, c3 = cv2.split(np.ubyte(a[:,:,:x.shape[2]]))
    img = cv2.merge((cv2.equalizeHist(c1), cv2.equalizeHist(c2), cv2.equalizeHist(c3)))
        
    return np.float64(img) ,a[:,:,x.shape[2]:]