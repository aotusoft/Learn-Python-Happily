from __future__ import division
import time
print("\n欢迎来到圆周率计算器！\n")
number = int(input('请输入想要计算到小数点后的位数:'))
print("\n正在计算...\n")
time1=time.time()
b = 10**number
x1 = b*4//5
x2 = b// -239
he = x1+x2
number *= 2
for i in range(3,number,2):
  x1 //= -25
  x2 //= -57121
  x = (x1+x2) // i
  he += x
pai = he*4
paistring=str(pai)
result=paistring[0]+str('.')+paistring[1:len(paistring)]
print("计算结果：\n\n%s"%result)
time2=time.time()
print('\n总共耗时：' + str(time2 - time1) + 's')
