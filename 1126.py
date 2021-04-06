#全局变量的测试
"""
num = 10
def demo1():
    #global 告诉解释器num是全局变量
    global num
    num = 100
    print(num)
def demo2():
    print("demo"+"-"*50)
    print(num)

demo1()
demo2()

print("over")
"""
"""
#温度计
def measure():
    '''返回当前温度'''
    print("开始测量")
    temp = 39
    print("测量结束")
    return temp
result = measure()
print(result)
"""
"""
def max(a,b):
    if a > b:
        print('max = a')
    else:
        print('max = b')

max(5,6)
max(6,5)
max(b=6,a=5)
max(a=6,b=5)

#函数可以有多个return
def max(a,b):
    if a > b:
        return a
    else:
        return b

temp = max(6,5)
print(temp)
"""

#默认参数的使用
def printinfo(name,age = 35):
    ""
    print("名字",name)
    print("年龄",age)
    return
#调用时，可少输入一个值，另一个就是默认
printinfo("张三")
printinfo("李四",18)

#两个参数都有默认值时，调用时可输入参数，也可不输入
def prin(a = 5,b = 6):
    print('a = ',a)
    print('b = ',b)
prin()         #不输入
prin(7,8)     #两个参数
prin(9)       #只输入a
prin(b = 4)#只输入b

#收集参数
def printinfo(arg1,*vartuple):
    ''''''
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return

#调用参数
printinfo(10)
printinfo(70,60,50)




























