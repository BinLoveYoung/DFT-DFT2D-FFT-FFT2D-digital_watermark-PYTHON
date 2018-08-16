#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#清晰DFT

from math import *

def DFT(xreal,ximag):#分别输入实数部分与虚数部分
    N = len(xreal)#获取采样点的个数
    Xreal = [0 for i in range(N)]#将频域的实数与虚数部分分别初始化
    Ximag = [0 for i in range(N)]
    for k in range(N):#分别计算频域中每一个点的值
        for n in range(N):#对时域中的每一个点进行求和
            # 分别求和实数与虚数部分,依照(a+bi)(c+di)=(ac-bd)+(bc+ad)i,简化对浏览代码的人的脑子的负担
            a = xreal[n]
            b = ximag[n]
            c = cos(2 * pi * k * n / N)
            d = -sin(2 * pi * k * n / N)
            Xreal[k] += a*c-b*d
            Ximag[k] += b*c+a*d
        #print("----")#Debug用
    return Xreal, Ximag#分别返回实数与虚数部分

def IDFT(Xreal,Ximag):#分别输入实数部分与虚数部分。其实这里的操作与DFT几乎相同，差别在于我们将1/N放在这里，需要乘上去
    N = len(Xreal)#获取采样点的个数
    xreal = [0 for i in range(N)]#将时域的实数与虚数部分分别初始化
    ximag = [0 for i in range(N)]
    for k in range(N):#分别计算时域中每一个点的值
        for n in range(N):#对频域中的每一个点进行求和
            # 分别求和实数与虚数部分,依照(a+bi)(c+di)=(ac-bd)+(bc+ad)i,简化对浏览代码的人的脑子的负担
            a = Xreal[n]
            b = Ximag[n]
            c = cos(2 * pi * k * n / N)
            d = sin(2 * pi * k * n / N)
            xreal[k] += (a*c-b*d) / N#这里可以考虑使用numpy的array，将除N的操作放在最后一起进行
            ximag[k] += (b*c+a*d) / N
        #print("----")#Debug用
    return xreal, ximag#分别返回实数与虚数部分

def test1():
    # DFT测试
    xreal = [0.0, 1.0, 0.0, 0.0]  # 初始化样例输入的实数部分
    ximag = [0.0 for i in range(len(xreal))]  # 将虚数部分设为与实数部分等长的列表，全部为0
    for i in range(len(xreal)):  # 打印x的实数与虚数部分，并四舍五入到整数，作为参照
        print(round(xreal[i]), round(ximag[i]))
    print("----")

    Xreal, Ximag = DFT(xreal, ximag)  # 获取返回的X的实数部分和虚数部分分别保存
    for i in range(len(Xreal)):  # 打印X的实数与虚数部分，并四舍五入到整数
        print(round(Xreal[i]), round(Ximag[i]))
    print("----")

    xreal, ximag = IDFT(Xreal, Ximag)  # 将虚数部分设为与实数部分等长的列表，全部为0.并获取返回的x的实数部分和虚数部分分别保存
    for i in range(len(xreal)):  # 打印x的实数与虚数部分，并四舍五入到整数
        print(round(xreal[i]), round(ximag[i]))
    print("----")

test1()