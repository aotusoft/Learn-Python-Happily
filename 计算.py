"""
多行注释开始
1注释
2注释
多行注释结束

"""
import random
import time
import math
a = random.randint(0,10000)
print("产生的随机数" + "：%s"%a)    #取随机
num = int(input('请输入想要的数：'))    # 输入数据

time1=time.time()

b = math.sin(a)
c = math.cos(a)

print(b*a+c)

print(a+num)    # + 加法

print(a//80)    # // 取整数

print(a%80)    # % 取余数

print(a**80%100)    # ** 幂

print(a*(a+80)%44)    # 优先级

time2=time.time()

print("字符的运算示例 "*6)    #字符的运算

print('\n总共耗时：' + str(time2 - time1) + 's')
