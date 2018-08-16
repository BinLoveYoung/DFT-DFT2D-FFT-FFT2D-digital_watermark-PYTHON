#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#使用了内置的复数类型于numpy的ndarray
#使用了两个分式调用DFT从行列分别计算

from math import *
import numpy as np

from DFT.DFT_2 import DFT,IDFT

def DFT2D_check(x):
    length = 0
    for row in x:
        l = len(row)
        if length < l:
            length = l
    for row in x:
        row.extend([0 for i in range(length-len(row))])
    return np.array(x)

def DFT2D(x):
    N2 = len(x)#获取行数，即y值（要是觉得横竖分不清先后的话也没问题，只要逆运算的时候顺序相反即可，此处是为了与文档对应）
    N1 = len(x[0])#获取列数，即x值
    X = np.array([[complex() for n2 in range(N2)] for n2 in range(N1)])#初始化一个N1行N21列的二维复数矩阵(原因是后面的翻转)
    M = np.array([[complex() for n1 in range(N1)] for n2 in range(N2)])#初始化一个N2行N1列的二维复数矩阵作为中介
    for k2 in range(N2):#遍历X中的行
        M[k2] = DFT(x[k2])
    for k1 in range(N1):  # 遍历X中的列
        X[k1] = DFT(M.transpose()[k1])
                #print("comp=",comp)#Debug
            #print("Xreal=", Xreal[k2][k1], "Ximag=", Ximag[k2][k1])#Debug
    return X.transpose()

def IDFT2D(X):
    N2 = len(X)#获取行数，即y值（要是觉得横竖分不清先后的话也没问题，只要逆运算的时候顺序相反即可，此处是为了与文档对应）
    N1 = len(X[0])#获取列数，即x值
    x = np.array([[complex() for n2 in range(N2)] for n1 in range(N1)])#初始化一个N1行N2列的二维复数矩阵(原因是后面的翻转)
    m = np.array([[complex() for n1 in range(N1)] for n2 in range(N2)])#初始化一个N2行N1列的二维复数矩阵作为中介
    for n2 in range(N2):#遍历x中的行
        m[n2] = IDFT(X[n2])
    for n1 in range(N1):  # 遍历x中的列
        x[n1] = IDFT(m.transpose()[n1])
             #print("xreal=", xreal[k2][k1], "ximag=", ximag[k2][k1])#Debug
    #x /= N1*N2#因为在IDFT中我们已经对数据进行过这一步处理，所以这里就不需要处理了
    return x.transpose()

def test2():
    # 2D DFT测试
    #xreal = [[1.0, 0.0], [0.0, 0.0]]
    #ximag = [[0.0 for n1 in range(len(xreal[0]))] for n2 in range(len(xreal))]  # 将虚数部分设为与实数部分等大的列表，全部为0
    #ximag = [[0.0, 0.0], [0.0, 0.0]]
    #x = np.array([[complex(xreal[n2][n1], ximag[n2][n1]) for n1 in range(len(xreal[0]))]for n2 in range(len(xreal))])
    x = [[1.0+0.0j,0.0+0.0j,0],[0.0+0.0j,0.0+0.0j]]
    x = DFT2D_check(x)
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

if __name__ == "__main__":
    test2()