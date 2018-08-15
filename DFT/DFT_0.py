#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from math import *

def DFT(xreal):#分别输入一个实数列表代表时域
    N = len(xreal)#获取采样点的个数
    Xreal = [0 for i in range(N)]#将频域的实数与虚数部分分别初始化
    Ximag = [0 for i in range(N)]
    for k in range(N):#分别计算频域中每一个点的值
        for n in range(N):#对时域中的每一个点进行求和
            # 分别求和实数与虚数部分,依照(a+bi)(c+di)=(ac-bd)+(bc+ad)i进行分步处理,增强可读性，注意，这里的b不存在，即虚数部分为0
            a = xreal[n]
            c = cos(2 * pi * k * n / N)
            d = -sin(2 * pi * k * n / N)
            Xreal[k] += a*c
            Ximag[k] += a*d
        #print("----")#Debug用
    return Xreal, Ximag#分别返回实数与虚数部分

def IDFT(Xreal,Ximag):#分别输入频域的实数部分与虚数部分
    N = len(Xreal)#获取采样点的个数
    xreal = [0 for i in range(N)]#将时域的实数部分初始化，因为我们的DFT的输入只有实数部分，因此对结果进行逆运算自然也只有实数部分，并且对图像处理也只需要实数部分，如果产生了虚数部分将无法保存在图片中，必须舍弃
    for k in range(N):#分别计算时域中每一个点的值
        for n in range(N):#对频域中的每一个点进行求和
            # 分别求和实数与虚数部分,依照(a+bi)(c+di)=(ac-bd)+(bc+ad)i进行分步处理,增强可读性
            a = Xreal[n]
            b = Ximag[n]
            c = cos(2 * pi * k * n / N)
            d = sin(2 * pi * k * n / N)
            xreal[k] += (a*c-b*d) / N#这里可以考虑使用numpy的array，将除N的操作放在最后一起进行
        #print("----")#Debug用
    return xreal#返回时域

def test1():
    # DFT测试
    xreal = [0.0, 1.0, 0.0, 0.0]  # 初始化样例输入的实数部分
    for i in range(len(xreal)):  # 打印x的实数与虚数部分，并四舍五入到整数，作为参照
        print(round(xreal[i]))
    print("----")

    Xreal, Ximag = DFT(xreal)  # 获取返回的X的实数部分和虚数部分分别保存
    for i in range(len(Xreal)):  # 打印X的实数与虚数部分，并四舍五入到整数
        print(round(Xreal[i]), round(Ximag[i]))
    print("----")

    xreal = IDFT(Xreal, Ximag)  # 将虚数部分设为与实数部分等长的列表，全部为0.并获取返回的x的实数部分和虚数部分分别保存
    for i in range(len(xreal)):  # 打印x的实数与虚数部分，并四舍五入到整数
        print(round(xreal[i]))
    print("----")

test1()