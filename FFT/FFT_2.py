#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#迭代版本

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
    FFT_order(x)
    N = len(x)
    M = int(log(N,2))
    for layer in range(M):#共有log[2]N层
        units = 1 << layer#通过位运算计算2的幂。将相交叉的蝶形单元分为一组,每组中有2^layer个蝶形单元
        i = 0#当前下标
        for group in range(0, N, units << 1):#总共N个，每组的长度为每组中蝶形单元的两倍，因为一个蝶形单元有两个数据
            for unit in range(units):
                #print(i,i+(1<<layer))
                #print("初始：", x[i], x[i + (1 << layer)])
                #a = x[i]
                #b = x[i+(1<<layer)]
                #W = complex(cos(2 * pi * unit / (1 << (layer+1))), -sin(2 * pi * unit / (1 << (layer+1))))
                #k = b*W
                k = x[i+(1<<layer)] * complex(cos(2 * pi * unit / (1 << (layer+1))), -sin(2 * pi * unit / (1 << (layer+1))))
                x[i + (1 << layer)] = x[i] - k
                x[i] += k
                #print("结束：",x[i],x[i+(1<<layer)])
                i += 1
            i += units
    return x

def IFFT(X):
    FFT_order(X)
    N = len(X)
    M = int(log(N,2))
    for layer in range(M):#共有log[2]N层
        units = 1 << layer#通过位运算计算2的幂。将相交叉的蝶形单元分为一组,每组中有2^layer个蝶形单元
        i = 0#当前下标
        for group in range(0, N, units << 1):#总共N个，每组的长度为每组中蝶形单元的两倍，因为一个蝶形单元有两个数据
            for unit in range(units):
                #print(i,i+(1<<layer))
                #print("初始：", X[i], X[i + (1 << layer)])
                #a = x[i]
                #b = x[i+(1<<layer)]
                #W = complex(cos(2 * pi * unit / (1 << (layer+1))), -sin(2 * pi * unit / (1 << (layer+1))))
                #k = b*W
                k = X[i+(1<<layer)] * complex(cos(2 * pi * unit / (1 << (layer+1))), sin(2 * pi * unit / (1 << (layer+1))))
                X[i + (1 << layer)] = X[i] - k
                X[i] += k
                #print("结束：",X[i],X[i+(1<<layer)])
                i += 1
            i += units
    X /= N


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

    X = FFT(x)  # 获取返回的X的实数部分和虚数部分分别保存
    for i in range(len(X)):  # 打印X的实数与虚数部分，并四舍五入到整数
        print(round(X[i].real), round(X[i].imag))
    print("----")

    x = IFFT(X)  # 将虚数部分设为与实数部分等长的列表，全部为0.并获取返回的x的实数部分和虚数部分分别保存
    for i in range(len(x)):  # 打印x的实数与虚数部分，并四舍五入到整数
        print(round(x[i].real), round(x[i].imag))
    print("----")

if __name__ == "__main__":
    test3()