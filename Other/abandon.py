#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from math import *
#运算稍微慢了一些，也很快，但是不及另一个快
def invert_order(bit):
    rev = [0 for i in range(2**bit)]
    for i in range(1<<bit):
        rev[i]=(rev[i>>1]>>1)|((i&1)<<(bit-1))
    return rev

def FFT_order(x):
    order = invert_order(int(log(len(x),2)))
    for i in range(len(x)):
        j = order[i]
        if(i<j):
            x[i],x[j] = x[j],x[i]