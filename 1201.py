"""
#内嵌函数
def outter():#第一层函数
    print("outter()被调用")
    def inner():#内嵌函数
        print("inner()被调用")
    inner()

outter()
#inner()外部不可见
"""
#闭包
"""
def make_adder(addend):
    def adder(augend):
        return augend + addend
    return adder

p = make_adder(23)
q = make_adder(44)
print(p(100))
print(q(100))
"""
#lambda
"""
def sum(a,b): #正常
    return a+b
x = sum(12,30)
print(x)

sum = lambda a,b:a+b #lambda 临时
x= sum(12,30)
print(x)
"""
#汉诺塔
"""
def move(n,a,b,c):
    if n == 1:
        print(a,"-->",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
a = input("请输入A上的个数:")
num = int(a)
print("把",num,"个盘子全部移动到C的顺序为")
move(num,"A","B","C")
"""

#阶乘
def fact(num):
    result = 1
    for i in range(1,num+1):
        result *= i
        return result

n = int(input("请输入整数："))
x = fact(n)
print(x)


def fact(num):
    if num == 1: #计算到num=1时，终止递归
        return 1
    else:
        return num*fact(num+1) #否则反复调用自己
n = int(input("请输入整数："))
x = fact(n)
print(x)















    
