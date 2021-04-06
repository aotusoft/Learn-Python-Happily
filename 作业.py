"""
#阶乘
i = int(input("请输入数字"))
a = 1
while i != 0:
    a = a * i
    i -= 1
print(a)
"""

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

while True:
    num1 = int(input("输入1："))
    fh = input()
    num2 = int(input("输入2："))
    if fh == "+":
        sum_num()
    elif fh == "-":
        sum_num2()
    elif fh == "*":
        sum_num3()
    elif fh == "/":
        sum_num4()