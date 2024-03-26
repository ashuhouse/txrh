import numpy as np
import matplotlib.pyplot as plt
import cv2


def divide_method(img, m, n):  # 分割成m行n列
    m = m+1
    n = n+1
    h, w = img.shape[0], img.shape[1]
    grid_h = int(h * 1.0 / (m - 1) + 0.5)  # 每个网格的高
    grid_w = int(w * 1.0 / (n - 1) + 0.5)  # 每个网格的宽

    # 满足整除关系时的高、宽
    h = grid_h * (m - 1)
    w = grid_w * (n - 1)

    # 图像缩放
    img_re = cv2.resize(img, (w, h),cv2.INTER_LINEAR)  # 也可以用img_re=skimage.transform.resize(img, (h,w)).astype(np.uint8)
    # plt.imshow(img_re)
    gx, gy = np.meshgrid(np.linspace(0, w, n), np.linspace(0, h, m))
    gx = gx.astype(np.int_)
    gy = gy.astype(np.int_)
    if len(img.shape) == 3:
        divide_image = np.zeros([m - 1, n - 1, grid_h, grid_w, 3],np.uint8)  # 这是一个五维的张量，前面两维表示分块后图像的位置（第m行，第n列），后面三维表示每个分块后的图像信息
    elif len(img.shape) == 2:
        divide_image = np.zeros([m - 1, n - 1, grid_h, grid_w], np.uint8)

    for i in range(m - 1):
        for j in range(n - 1):
            divide_image[i, j] = img_re[gy[i][j]:gy[i + 1][j + 1], gx[i][j]:gx[i + 1][j + 1]]
    # print(divide_image.shape)
    return divide_image

def display_blocks(divide_image):
    m,n=divide_image.shape[0],divide_image.shape[1]
    for i in range(m):
        for j in range(n):
            plt.subplot(m,n,i*n+j+1)
            if len(divide_image.shape) == 5:
                plt.imshow(divide_image[i,j][:,:,::-1])
            elif len(divide_image.shape) == 4:
                plt.imshow(divide_image[i,j], cmap='gray')
            plt.axis('off')

    plt.show()

def img_read(img_name,a):
    img = cv2.imread(img_name,a)

    # cv2.imshow('1',img)
    # cv2.waitKey(0)
    # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #
    # h, w = img.shape[0], img.shape[1]
    # fig1 = plt.figure('原始图像')
    # plt.imshow(img[:,:,::-1])
    # plt.axis('off')
    # plt.title('Original image')
    # plt.show()
    return img
    # m = int(input("请输入行数:"))
    # n = int(input("请输入列数:"))
    # divide_image2 = divide_method(img, m+1, n+1)  # 该函数中m+1和n+1表示网格点个数，m和n分别表示分块的块数
    # fig3 = plt.figure('分块后的子图像:图像缩放法')
    # display_blocks(divide_image2)


