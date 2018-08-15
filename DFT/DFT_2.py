#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#使用了内置的复数类型于numpy的ndarray

from math import *
import numpy as np

def DFT(x):#输入一个代表时域的复数列表
    N = len(x)#获取采样点的个数
    X = np.array([complex() for i in range(N)])#将频域初始化
    for k in range(N):#分别计算频域中每一个点的值
        for n in range(N):#对时域中的每一个点进行求和
            X[k] += x[n]*complex(cos(2 * pi * k * n / N), -sin(2 * pi * k * n / N))
        #print("----")#Debug用
    return X#返回频域

def IDFT(X):#输入一个代表频域的复数列表。其实这里的操作与DFT几乎相同，差别在于我们将1/N放在这里，需要乘上去
    N = len(X)#获取采样点的个数
    x = np.array([complex() for i in range(N)])#将时域初始化
    for k in range(N):#分别计算时域中每一个点的值
        for n in range(N):#对频域中的每一个点进行求和
            x[k] += X[n]*complex(cos(2 * pi * k * n / N), sin(2 * pi * k * n / N))
        #print("----")#Debug用
    x /= N
    return x#返回时域


def test1():
    # DFT测试
    xreal = [0.0, 1.0, 0.0, 0.0]  # 初始化样例输入的实数部分
    #ximag = [0.0 for i in range(len(xreal))]  # 将虚数部分设为与实数部分等长的列表，全部为0
    ximag = [0.0, 0.0, 0.0, 0.0]
    x = np.array([complex(xreal[i], ximag[i]) for i in range(len(xreal))])
    for i in range(len(x)):  # 打印x的实数与虚数部分，并四舍五入到整数，作为参照
        print(round(x[i].real), round(x[i].imag))
    print("----")

    X = DFT(x)  # 获取返回的X的实数部分和虚数部分分别保存
    for i in range(len(X)):  # 打印X的实数与虚数部分，并四舍五入到整数
        print(round(X[i].real), round(X[i].imag))
    print("----")

    x = IDFT(X)  # 将虚数部分设为与实数部分等长的列表，全部为0.并获取返回的x的实数部分和虚数部分分别保存
    for i in range(len(xreal)):  # 打印x的实数与虚数部分，并四舍五入到整数
        print(round(x[i].real), round(x[i].imag))
    print("----")

test1()