#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#递归版本

from math import *
import numpy as np

def FFT_check(x):#用0将x的长度补齐到2的幂
    x.extend([0 for i in range(2 ** (int(ceil(log(len(x), 2)))) - len(x))])
    return np.array(x)

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
    N = len(x)
    num = N // 2
    M = int(log(N,2))
    if N != 2:
        x = np.append(FFT(x[:num]),FFT(x[num:]))
    else:
        print("当前层数：",M)#Debug用
        print("初始",x)#Debug用
        k = x[1]
        x[1] = x[0]-k
        x[0] += k
        print("结束",x)#Debug用
        return x
    print("当前层数：", M)#Debug用
    print("初始", x)#Debug用
    for unit in range(num):
        #a = x[unit]
        #b = x[unit+1 << (M-1)]
        #W = complex(cos(2 * pi * unit / 1 << M), -sin(2 * pi * unit / 1 << M))
        #k = b*W
        k = x[unit+(1 << (M-1))]*complex(cos(2 * pi * unit / (1 << M)), -sin(2 * pi * unit / (1 << M)))#左移运算符的优先级好像比加号低，尴尬
        x[unit + (1 << (M - 1))] = x[unit] - k
        x[unit] += k
    print("结束", x)#Debug用
    return x

def IFFT(X):
    N = len(X)
    num = N // 2
    M = int(log(N,2))
    if N != 2:
        X = np.append(IFFT(X[:num]), IFFT(X[num:]))
        print(X)
    else:
        print("当前层数：",M)#Debug用
        print("初始",X)#Debug用
        k = X[1]
        X[1] = X[0]-k
        X[0] += k
        print("结束",X)#Debug用
        return X/2#这个2相当于DFT里最后除的N
    print("当前层数：", M)#Debug用
    print("初始", X)#Debug用
    for unit in range(num):
        #a = x[unit]
        #b = x[unit+1 << (M-1)]
        #W = complex(cos(2 * pi * unit / 1 << M), -sin(2 * pi * unit / 1 << M))
        #k = b*W
        k = X[unit+(1 << (M-1))]*complex(cos(2 * pi * unit / (1 << M)), sin(2 * pi * unit / (1 << M)))#左移运算符的优先级好像比加号低，尴尬
        X[unit + (1 << (M - 1))] = X[unit] - k
        X[unit] += k
    print("结束", X)#Debug用
    return X/2#这个2相当于DFT里最后除的N



def test3():
    # DFT测试
    # xreal = [i for i in range(8)]
    xreal = [0.0, 1.0, 0.0, 0.0]  # 初始化样例输入的实数部分
    #ximag = [0.0 for i in range(len(xreal))]  # 将虚数部分设为与实数部分等长的列表，全部为0
    ximag = [0.0, 0.0, 0.0, 0.0]
    x = [complex(xreal[i], ximag[i]) for i in range(len(xreal))]
    x = FFT_check(x)
    for i in range(len(x)):  # 打印x的实数与虚数部分，并四舍五入到整数，作为参照
        print(round(x[i].real), round(x[i].imag))
    print("----")

    FFT_order(x)
    X = FFT(x)  # 获取返回的X的实数部分和虚数部分分别保存
    for i in range(len(X)):  # 打印X的实数与虚数部分，并四舍五入到整数
        print(round(X[i].real), round(X[i].imag))
    print("----")

    FFT_order(X)
    x = IFFT(X)  # 将虚数部分设为与实数部分等长的列表，全部为0.并获取返回的x的实数部分和虚数部分分别保存
    for i in range(len(x)):  # 打印x的实数与虚数部分，并四舍五入到整数
        print(round(x[i].real), round(x[i].imag))
    print("----")

if __name__ == "__main__":
    test3()