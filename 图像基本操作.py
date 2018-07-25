# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:41:37 2018

@author: ai
"""

import cv2
from PIL import Image
import numpy as np




#PIL加载图片
pil_im = Image.open('lena.jpg')

#opencv加载图片
cv2_im = cv2.imread('lena.jpg')

#PIL显示图片
#Image._show(pil_im)

#opencv显示图片
#cv2.imshow('cv2_img',cv2_im)
#key = cv2.waitKey(0)  #设置一个延迟，<=0
#if key == 27:  
#    cv2.destroyAllWindows()
#
#PIL保存图片
#pil_im.save('pil_im.jpg')
#
##opencv保存图片
#cv2.imwrite('cv2_im.jpg',cv2_im)



#cv2操作
#rows,cols,ch=cv2_im.shape  #image行、列、通道
##
#b,g,r=cv2.split(cv2_im)   #image通道拆分  耗费时间内存 建议使用如下操作
#cv2.imshow("g_img",g)
#cv2.waitKey(0)
#
# b = cv2_im[:,:,0] #分离出的蓝色通道 使用numpy索引
# g = cv2_im[:,:,1]
# r = cv2_im[:,:,2]
# cv2_im = cv2.merge(b,g,r) #把独立通道合成一张新的图片




#image=cv2.merge([r,g,b]) #image通道合并
#cv2.imshow("merge_img",image)
#cv2.waitKey(0)
#
#gray = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2GRAY) #image转灰度图
#cv2.imshow("gray",gray)
#cv2.waitKey(0)

#im = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB) #image bgr通道转rgb通道
#im = Image.fromarray(im)
#Image._show(im)

##重置大小
#resize_img = cv2.resize(cv2_im, dsize=(400,400), interpolation=cv2.INTER_CUBIC)
#cv2.imshow("resize_image",resize_img)
#cv2.waitKey(0)




#均值滤波
#aver = cv2.blur(cv2_im,(3,3))
#cv2.imshow("aver_image",aver)
#cv2.waitKey(0)


#中值滤波
#median = cv2.medianBlur(cv2_im,3)
#cv2.imshow("median_image",median)
#cv2.waitKey(0)


#高斯滤波
#高斯核函数在Y方向上的标准偏差，如果sigmaY是0，则函数会自动将sigmaY的值设置为与sigmaX相同的值，如果sigmaX和sigmaY都是0，这两个值将由ksize.width和ksize.height计算而来。
#gaussian = cv2.GaussianBlur(cv2_im, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
#cv2.imshow("gaussian_image",gaussian)
#cv2.waitKey(0)
















