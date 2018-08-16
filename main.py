#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from matplotlib import pyplot as plt
from matplotlib import image as mpimg

if __name__ == "__main__":
    watermark = mpimg.imread('watermark.png')
    watermark_0 = watermark[:, :, 0]
    plt.imshow(watermark_0, cmap='Greys_r')
    plt.show()