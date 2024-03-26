import math
import cv2 as cv
import numpy as np

# SF calcuate
def SF_cal(image,i,j,m,n):
    # k = m * n
    rf = image[i, j, :, 1:n-1] - image[i, j, :, 0:n-2]
    cf = image[i, j, 1:m-1, :] - image[i, j, 0:m-2, :]

    rf = np.square(rf)
    cf = np.square(cf)
    rf = rf.sum()
    cf = cf.sum()

    sf = math.sqrt((rf + cf) / (m * n))
    print(sf)
    return sf
    # RF_2 = 0
    # CF_2 = 0
    # m,n = img1.shape[0] , img1.shape[1]
    # for i in range(m-1) :
    #     for j in range(n-1) :
    #         RF_1 =np.square(img1[i,j] - img1[i,j - 1])
    #         RF_2 += RF_1
    #         return RF_2
    #
    # for j in range(n-1):
    #     for i in range(m-1) :
    #         CF_1 =np.square(img1[i,j] - img1[i - 1,j])
    #         CF_2 += CF_1
    #         return CF_2
    #
    # SF = np.sqrt()






