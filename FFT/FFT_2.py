#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#迭代版本

from math import *

def FFT_check(x):#用0将x的长度补齐到2的幂
    x.extend([0 for i in range(2 ** (int(ceil(log(len(x), 2)))) - len(x))])

def FFT_order(x):#此处改自他人代码用于为输入排序
    num = len(x)
    j = num // 2
    for i in range(1, num - 2):
        if (i < j):
            x[i], x[j] = x[j], x[i]
        k = num / 2
        while (j >= k):
            j -= k
            k /= 2
        j = int(j + k)

def FFT(x):
    FFT_check(x)
    FFT_order(x)
    N = len(x)
    M = int(log(N,2))
    for layer in range(M):#共有log[2]N层
        units = 1 << layer#通过位运算计算2的幂。将相交叉的蝶形单元分为一组,每组中有2^layer个蝶形单元
        i = 0#当前下标
        for group in range(0, N, units << 1):#总共N个，每组的长度为每组中蝶形单元的两倍，因为一个蝶形单元有两个数据
            i += units
            for unit in range(units):
                a = x[i]
                b = x[i+1<<layer]
                W = complex(cos(2 * pi * unit / 1 << layer), -sin(2 * pi * unit / 1 << layer))
                x[B]
                i += 1
