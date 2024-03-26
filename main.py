import img_divide
import img_divide as imdiv
import SESF as SF
import numpy as np
import cv2 as cv
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # image read
    img1 = imdiv.img_read("gray_mwg_clock_1.png",0)
    img2 = imdiv.img_read('gray_mwg_clock_2.png',0)

    m , n = input("请输入n x n:").split("x")
    m=int(m)
    n=int(n)
    TH = int(input('请输入阈值：'))
    M = int(img1.shape[0]/int(m))
    N = int(img1.shape[1]/int(n))
    dived_img1 = imdiv.divide_method(img1, M, N)
    dived_img2 = imdiv.divide_method(img2, M, N)
    image = np.zeros_like(dived_img1)

    for i in range(dived_img1.shape[0]):
        for j in range(dived_img2.shape[1]):
            img1_SF = SF.SF_cal(dived_img1, i, j, m, n)
            img2_SF = SF.SF_cal(dived_img2, i, j, m, n)

            if img1_SF > img2_SF + TH:
                image[i,j] = dived_img1[i,j]
            elif img1_SF < img2_SF - TH:
                image[i,j] = dived_img2[i,j]
            else:
                image[i,j] = (dived_img1[i,j] + dived_img2[i,j])/2
    img_divide.display_blocks(dived_img1)
    img_divide.display_blocks(dived_img2)
    img_divide.display_blocks(image)

    # divided image show
    # imdiv.display_blocks(dived_img1)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
