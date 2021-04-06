
#replace代替
"""
s = "中国，中国，河北，保定"
t = s.replace("中国","中华人民共和国")
print(s) #对比
print(t)
"""
#split拆分
"""
s = "apple, peach,banana,pear"
t = s.split(",")
print(t)
"""
#def 函数
#def define 定义
#
#   函数封装的代码

"""
def hello_world():
    print("世界，你好。")
    return
    """
#调用
"""
s = hello_world()
"""
name = "小明"
#定义函数
"""
def say_hello():
    print("hello")
    print("hello")
    print("hello")
    return
print(name)
say_hello()
print(name)
"""
num1 = int(input("输入1："))
fh = input()
num2 = int(input("输入2："))
#加法
def sum_num():
    
    res = num1 + num2
    print("%d + %d = %d" %(num1,num2,res))
    return

#减法
def sum_num2():

    res = num1 - num2
    print("%d - %d = %d" %(num1,num2,res))
    return
#乘法
def sum_num3():

    res = num1 * num2
    print("%d * %d = %d" %(num1,num2,res))
    return
#除法
def sum_num4():

    res = float(num1 / num2) #小数？
    print("%d / %d = %d" %(num1,num2,res))
    return

if fh == "+":
    sum_num()
elif fh == "-":
    sum_num2()
elif fh == "*":
    sum_num3()
elif fh == "/":
    sum_num4()















