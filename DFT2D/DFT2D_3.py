#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#使用了内置的复数类型与numpy的ndarray
#使用了两个分式从行列分别计算

from math import *
import numpy as np

def DFT2D_check(x):
    length = 0
    for row in range(len(x)):
        l = len(x[row])
        if length < l:
            length = l
    for row in range(len(x)):
        x[row] = np.append(x[row], [0 for i in range(length-len(x[row]))])

def DFT2D(x):
    N2 = len(x)#获取行数，即y值（要是觉得横竖分不清先后的话也没问题，只要逆运算的时候顺序相反即可，此处是为了与文档对应）
    N1 = len(x[0])#获取列数，即x值
    X = np.array([[complex() for n1 in range(N1)] for n2 in range(N2)])#初始化一个N2行N1列的二维复数矩阵
    M = np.array([[complex() for n1 in range(N1)] for n2 in range(N2)])#初始化一个N2行N1列的二维复数矩阵作为中介
    for k1 in range(N1):#遍历X中的每个点
        for k2 in range(N2):
            for n2 in range(N2):
                M[k2][k1] += x[n2][k1] * complex(cos(2 * pi * k2 * n2 / N2), -sin(2 * pi * k2 * n2 / N2))
    for k2 in range(N2):  # 遍历X中的每个点
        for k1 in range(N1):
            for n1 in range(N1):
                X[k2][k1] += M[k2][n1] * complex(cos(2 * pi * k1 * n1 / N1), -sin(2 * pi * k1 * n1 / N1))
                #print("comp=",comp)#Debug
            #print("Xreal=", Xreal[k2][k1], "Ximag=", Ximag[k2][k1])#Debug
    return X

def IDFT2D(X):
    N2 = len(X)#获取行数，即y值（要是觉得横竖分不清先后的话也没问题，只要逆运算的时候顺序相反即可，此处是为了与文档对应）
    N1 = len(X[0])#获取列数，即x值
    x = np.array([[complex() for n1 in range(N1)] for n2 in range(N2)])#初始化一个N2行N1列的二维复数矩阵
    for n1 in range(N1):#遍历X中的每个点
        for n2 in range(N2):
            for k2 in range(N2):
                x[n2][n1] += X[k2][n1] * complex(cos(2 * pi * k2 * n2 / N2), sin(2 * pi * k2 * n2 / N2))
    for n2 in range(N2):  # 遍历X中的每个点
        for n1 in range(N1):
            for k1 in range(N1):
                x[n2][n1] += X[n2][k1] * complex(cos(2 * pi * k1 * n1 / N1), sin(2 * pi * k1 * n1 / N1))
                #print("comp=",comp)#Debug
            #print("xreal=", xreal[k2][k1], "ximag=", ximag[k2][k1])#Debug
    x /= N1*N2
    return x

def test2():
    # 2D DFT测试
    #xreal = [[1.0, 0.0], [0.0, 0.0]]
    #ximag = [[0.0 for n1 in range(len(xreal[0]))] for n2 in range(len(xreal))]  # 将虚数部分设为与实数部分等大的列表，全部为0
    #ximag = [[0.0, 0.0], [0.0, 0.0]]
    #x = np.array([[complex(xreal[n2][n1], ximag[n2][n1]) for n1 in range(len(xreal[0]))]for n2 in range(len(xreal))])
    x = np.array([[1.0+0.0j,0.0+0.0j,0],[0.0+0.0j,0.0+0.0j]])
    DFT2D_check(x)
    for n2 in range(len(x)):
        for n1 in range(len(x[0])):
            print(round(x[n2][n1].real), round(x[n2][n1].imag), end='|')

        print()
    print("----")

    X = DFT2D(x)
    for k2 in range(len(X)):
        for k1 in range(len(X[0])):
            print(round(X[k2][k1].real), round(X[k2][k1].imag), end='|')
        print()
    print("----")

    x = IDFT2D(X)
    for n2 in range(len(x)):
        for n1 in range(len(x[0])):
            print(round(x[n2][n1].real), round(x[n2][n1].imag), end='|')
        print()
    print("----")

test2()