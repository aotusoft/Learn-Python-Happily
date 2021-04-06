#1.四舍五入
print("第一题")
a = float(input("请输入数字："))
b = a * 10
if b % 10 < 5 and b % 10 != 0: #四舍
    a = int(a)
elif b %10 >4 and b % 10 != 0: #五入
    a = int(a) + 1
else:
    a = int(a)
print(a)

print("")
#2.计算
print("第二题")
a = 10
a += a
print("1  ",a)
a = 10
a_=a
print("2  ",a)
a = 10
a *= 2+3
print("3  ",a)
a = 10
a /= 2+3
print("4  ",a)
a = 10
print("5  ",a)
a = 10
a//=a-3
print("6  ",a)
print("")

#3.假设a=7,b=-2,c=4,计算下列表达式的值并上机验证。
print("第三题")
a=7
b=-2
c=4
print("1  ",3*4**5/2)
a=7
b=-2
c=4
print("2  ",a*3%2)
a=7
b=-2
c=4
print("3  ",a%3+b*b-c//5)
a=7
b=-2
c=4
print("4  ",b**2-4*a*c)
print("")
"""
print("第四题")
#4、分析以下代码，测试当输入6789时的输出结果
num = int(input("please input a number:"))
while(num != 0):
    print(num %10,end='\n')
num = num // 10
print("")
"""
#5、阅读以下程序，分析程序功能及执行结果
print("第五题")
print("(1)",end="")
num = 5 
if num == 3: # 判断num的值 
    print ('boss')
elif num == 2: 
    print ('user')
elif num == 1: 
    print ('worker')
elif num < 0: # 值小于零时输出
    print ('error')
else: 
    print ('roadman') # 条件均不成立时输出
print("(2)",end="")
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15): 
    print ('hello')
else: 
    print ("undefine")
print("(3)",end="")
m = int(input("请输入整数m："))
n = int(input("请输入整数n："))
while(m != n):
    if(m>n):
        m = m-n
    else:
        n = n-m
print(m)
print("")

print("第六题")
#6、计算1~10的整数和
c = 0
d = 0
while d < 10 :
    d += 1
    c = c + d
print(c)
print("")

print("第七题")
#7.输入两个正整数，求它们的最大公约数。
e = int(input("输入1："))
f = int(input("输入2："))
#取整
if e <= f :
    g = f // e
else:
    g = e // f
