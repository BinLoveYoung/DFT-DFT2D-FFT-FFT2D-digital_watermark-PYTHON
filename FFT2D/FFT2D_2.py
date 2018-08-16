#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#从行列方向调用FFT分别计算

from math import *
import numpy as np
from FFT.FFT_2 import FFT,IFFT

def FFT2D_check(x):
    length = 0
    for row in range(len(x)):
        l = len(x[row])
        if length < l:
            length = l
    N1 = 2 ** (int(ceil(log(length, 2))))
    for row in range(len(x)):
        x[row] = np.append(x[row], [0 for i in range(N1-len(x[row]))])
    x = np.append(x,[[complex() for i in range(N1)] for j in range(2 ** (int(ceil(log(len(x), 2)))) - len(x))])

def FFT2D(x):
    N2 = len(x)#获取行数，即y值
    N1 = len(x[0])#获取列数，即x值
    X = np.array([[complex() for n2 in range(N2)] for n1 in range(N1)])#初始化一个N1行N2列的二维复数矩阵(原因是后面的翻转)
    M = np.array([[complex() for n1 in range(N1)] for n2 in range(N2)])#初始化一个N2行N1列的二维复数矩阵作为中介
    for k2 in range(N2):#遍历X中的行
        M[k2] = FFT(x[k2])
    for k1 in range(N1):  # 遍历X中的列
        X[k1] = FFT(M.transpose()[k1])
                #print("comp=",comp)#Debug
            #print("Xreal=", Xreal[k2][k1], "Ximag=", Ximag[k2][k1])#Debug
    return X.transpose()

def IFFT2D(X):
    N2 = len(X)#获取行数，即y值
    N1 = len(X[0])#获取列数，即x值
    x = np.array([[complex() for n2 in range(N2)] for n1 in range(N1)])#初始化一个N1行N2列的二维复数矩阵(原因是后面的翻转)
    m = np.array([[complex() for n1 in range(N1)] for n2 in range(N2)])#初始化一个N2行N1列的二维复数矩阵作为中介
    for n2 in range(N2):#遍历x中的行
        m[n2] = IFFT(X[n2])
    for n1 in range(N1):  # 遍历x中的列
        x[n1] = IFFT(m.transpose()[n1])
    #x /= N1*N2#因为在IFFT中我们已经对数据进行过这一步处理，所以这里就不需要处理了
    return x.transpose()

def test4():
    # 2D DFT测试
    #xreal = [[1.0, 0.0], [0.0, 0.0]]
    #ximag = [[0.0 for n1 in range(len(xreal[0]))] for n2 in range(len(xreal))]  # 将虚数部分设为与实数部分等大的列表，全部为0
    #ximag = [[0.0, 0.0], [0.0, 0.0]]
    #x = np.array([[complex(xreal[n2][n1], ximag[n2][n1]) for n1 in range(len(xreal[0]))]for n2 in range(len(xreal))])
    x = np.array([[1.0+0.0j,0.0+0.0j,0],[0.0+0.0j,0.0+0.0j]])
    FFT2D_check(x)
    for n2 in range(len(x)):
        for n1 in range(len(x[0])):
            print(round(x[n2][n1].real), round(x[n2][n1].imag), end='|')

        print()
    print("----")

    X = FFT2D(x)
    for k2 in range(len(X)):
        for k1 in range(len(X[0])):
            print(round(X[k2][k1].real), round(X[k2][k1].imag), end='|')
        print()
    print("----")

    x = IFFT2D(X)
    for n2 in range(len(x)):
        for n1 in range(len(x[0])):
            print(round(x[n2][n1].real), round(x[n2][n1].imag), end='|')
        print()
    print("----")

test4()