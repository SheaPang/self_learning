# -*- codeing = utf-8 -*-
# @time : 2021/12/4 14:42
# @Author : PXY
# @File : demo1.py
# @Software: PyCharm


'''
#函数的定义
def printinfo():
    print("----------------------")
    print("   人生苦短，我用python   ")
    print("----------------------")


#函数的调用
printinfo()
printinfo()
'''
'''
#带参数的函数

def add2num(a,b):
    c = a+b
    print(c)

add2num(11,22)
'''

#带返回值的函数
'''
def add2num(a,b):
    return a+b    #通过return来返回运算结果

print(add2num(11,22))
c

'''
'''
#返回多个值的函数

def divid(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu    #多个返回值用逗号分隔

sh,yu = divid(5,2)    #需要使用多个值来保存返回内容
print("商：%d,余数：%d"%(sh,yu))

'''

'''
#打印一条线
def printOneLine():
    print("-"*30)

#根据用户输入的数字，打印相应数量的线条
def printNumLine(num):
    i = 0
    while i <num:
        printOneLine()
        i+=1
printNumLine(4)

#printOneLine()
'''

'''
#求三个数的和

def sum3Number(a,b,c):
    return a+b+c
# print(sum3Number(10,20,30))
#完成3个数的平均值计算

def average3Number(a,b,c):
    sumResult=sum3Number(10,20,30)
    aveResult=sumResult/3.0
    return aveResult

result= average3Number(10,20,30)
print("平均值为：%d"%result)
'''

#全局变量与局部变量
'''
def test1():
    a = 300       #局部变量
    print("test1----------------修改前：a= %d"%a)
    a = 100
    print("test1----------------修改后：a= %d" % a)

def test2():
    a = 500      #不同的函数可以定义相同的名字，彼此无关
    print("test2----------------a= %d" % a)


test1()
test2()

'''
'''
a = 100    #全局变量

def test1():
    print(a)

def test2():
    print(a)     #调用全局变量a

test1()
test2()
'''

#全局变量和局部变量相同名字
'''
a=100
def test1():
    a = 300       #局部变量，优先使用
    print("test1----------------修改前：a= %d"%a)
    a = 200
    print("test1----------------修改后：a= %d" % a)

def test2():
    print("test2----------------a= %d" % a)    #没有局部变量，默认使用全局变量

test1()
test2()
'''

#在函数中修改全局变量

a=100

def test1():
    global a    #声明全局变量在函数中的标识符
    print("test1----------------修改前：a= %d"%a)
    a = 200
    print("test1----------------修改后：a= %d" % a)

def test2():
    print("test2----------------a= %d" % a)    #没有局部变量，默认使用全局变量

test1()
test2()