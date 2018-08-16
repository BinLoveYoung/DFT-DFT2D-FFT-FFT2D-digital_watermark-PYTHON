#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#清晰DFT2D，去除了数据检测

from math import *

def DFT2D_check(xreal,ximag):
    pass

def DFT2D(xreal,ximag):
    N2 = len(xreal)#获取行数，即y值（要是觉得横竖分不清先后的话也没问题，只要逆运算的时候顺序相反即可，此处是为了与文档对应）
    N1 = len(xreal[0])#获取列数，即x值
    Xreal = [[0 for x in range(N1)] for y in range(N2)]#初始化一个列表，由N2个含有N1个0的列表组成，即一个N2行N1列的列表
    Ximag = [[0 for x in range(N1)] for y in range(N2)]
    for k1 in range(N1):#遍历X中的每个点
        for k2 in range(N2):
            for n1 in range(N1):#遍历x中的每个点
                real = 0#用于保存内部求和的值
                imag = 0
                for n2 in range(N2):
                    a = xreal[n2][n1]#取第n2行的第n1个点
                    b = ximag[n2][n1]
                    c = cos(2 * pi * k2 * n2 / N2)
                    d = -sin(2 * pi * k2 * n2 / N2)
                    #print("real+=",a * c - b * d,"imag+=", b * c + a * d)#Debug
                    real += a * c - b * d
                    imag += b * c + a * d
                #print("real=",real,"imag=",imag)#Debug
                a = real
                b = imag
                c = cos(2 * pi * k1 * n1 / N1)
                d = -sin(2 * pi * k1 * n1 / N1)
                #print("Xreal+=", a * c - b * d, "Ximag+=", b * c + a * d)#Debug
                Xreal[k2][k1] += a * c - b * d
                Ximag[k2][k1] += b * c + a * d
            #print("Xreal=", Xreal[k2][k1], "Ximag=", Ximag[k2][k1])#Debug
    return Xreal, Ximag

def IDFT2D(Xreal,Ximag):
    N2 = len(Xreal)#获取行数，即y值（要是觉得横竖分不清先后的话也没问题，只要逆运算的时候顺序相反即可，此处是为了与文档对应）
    N1 = len(Xreal[0])#获取列数，即x值
    xreal = [[0 for x in range(N1)] for y in range(N2)]#初始化一个列表，由N2个含有N1个0的列表组成，即一个N2行N1列的列表
    ximag = [[0 for x in range(N1)] for y in range(N2)]
    for n1 in range(N1):#遍历X中的每个点
        for n2 in range(N2):
            for k1 in range(N1):#遍历x中的每个点
                real = 0#用于保存内部求和的值
                imag = 0
                for k2 in range(N2):
                    a = Xreal[k2][k1]#取第n2行的第n1个点
                    b = Ximag[k2][k1]
                    c = cos(2 * pi * k2 * n2 / N2)
                    d = sin(2 * pi * k2 * n2 / N2)
                    #print("real+=",a * c - b * d,"imag+=", b * c + a * d)#Debug
                    real += a * c - b * d
                    imag += b * c + a * d
                #print("real=",real,"imag=",imag)
                a = real
                b = imag
                c = cos(2 * pi * k1 * n1 / N1)
                d = sin(2 * pi * k1 * n1 / N1)
                #print("xreal+=", a * c - b * d, "ximag+=", b * c + a * d)#Debug
                xreal[n2][n1] += (a * c - b * d)/(N1*N2)
                ximag[n2][n1] += (b * c + a * d)/(N1*N2)
            #print("xreal=", xreal[k2][k1], "ximag=", ximag[k2][k1])#Debug
    return xreal, ximag

def test2():
    # 2D DFT测试
    xreal = [[1.0, 0.0], [0.0, 0.0]]
    ximag = [[0.0 for x in range(len(xreal[0]))] for y in range(len(xreal))]
    for y in range(len(xreal)):
        for x in range(len(xreal[0])):
            print(round(xreal[y][x]), round(ximag[y][x]), end='|')
        print()
    print("----")

    Xreal, Ximag = DFT2D(xreal, ximag)
    for y in range(len(Xreal)):
        for x in range(len(Xreal[0])):
            print(round(Xreal[y][x]), round(Ximag[y][x]), end='|')
        print()
    print("----")

    xreal, ximag = IDFT2D(Xreal, Ximag)
    for y in range(len(xreal)):
        for x in range(len(xreal[0])):
            print(round(xreal[y][x]), round(ximag[y][x]), end='|')
        print()
    print("----")

test2()