# -*- codeing = utf-8 -*-
# @time : 2021/12/4 16:45
# @Author : PXY
# @File : demo3.py
# @Software: PyCharm


'''
#发生异常
print('----------test------1---')
f = open("123.txt", "r")      #用只读模式打开了一个不存在的文件，报错
print("----------test------2---")   #这句代码不会被执行
'''

'''
#捕获异常
try:
    print("----------test------1---")
    f = open("123.txt","r")
    print("----------test------2---")

except IOError:       #文件没找到，属于IO异常（输入输出异常）
    pass              #捕获异常后，执行的代码

'''

'''
try:
    print(num)
#except IOError:      #异常类型想要被捕获，需要一致
except NameError:
    print("产生错误了")
'''

'''
try:
    print("----------test------1---")
    f = open("123.txt","r")
    print("----------test------2---")

    print(num)
except (NameError,IOError):       #将可能产生的所有异常类型，都放到下面的小括号中
    print("产生错误了")
'''

'''
#获取错误描述
try:
    print("----------test------1---")
    f = open("123.txt","r")
    print("----------test------2---")

    print(num)
except (NameError,IOError) as result:       #将可能产生的所有异常类型，都放到下面的小括号中
    print("产生错误了")
    print(result)
'''

'''
#捕获所有的异常
try:
    print("----------test------1---")
    f = open("text1.txt","r")
    print("----------test------2---")

    print(num)
except Exception as result:       #Exception可以承接所有异常
    print("产生错误了")
    print(result)
'''


#仔细学习这个例子
#try      finally和嵌套
import time
try:
    f = open("text1.txt","r")
    try:
        while True:
            content = f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")

except Exception as result:
    print("发生异常。。。")





