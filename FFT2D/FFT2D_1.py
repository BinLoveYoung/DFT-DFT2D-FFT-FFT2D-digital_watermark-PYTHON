#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#毫无头绪的总式计算

from math import *
import numpy as np

def FFT2D_check(x):
    length = 0
    for row in range(len(x)):
        l = len(x[row])
        if length < l:
            length = l
    N1 = 2 ** (int(ceil(log(length, 2))))
    print(N1)
    for row in range(len(x)):
        x[row] = np.append(x[row], [0 for i in range(N1-len(x[row]))])
    x = np.append(x,[[complex() for i in range(N1)] for j in range(2 ** (int(ceil(log(len(x), 2)))) - len(x))])
    print(x)