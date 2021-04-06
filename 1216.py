"""
b = {}
c = input('请输入句子:  ')
for i in c.split(' '):
    if i not in b:
        b[i] = 1#产生键值
    else:
        b[i] += 1#键值加一
print(b)
"""
#生成银行卡
"""
b = {}
print("卡号             密码")
a = 6102009000
for i in range(1,101):
    print(a+i,"redhat")
    b[a+i] = "redhat"

s = []
for i in range(100):
    s1 = '6101009%.3d'%(i+1)#%.3d三个0
    s.append(s1)
s2 = {}.fromkeys(s,'redhat')#从s直接生成字典
print('银行卡号\t\t\t密码')
for key, value, in s2.items():#格式化输出
    print('%s\t\t\t%s'%(key,value))
"""

#模拟轮盘
import random
a = {'first':0,'second':0,'third':0}
def win():
    b= random.uniform(0,1)
    if b <= 0.08:
        a['first'] += 1
    if b > 0.08 and b <= 0.3:
        a['second'] += 1
    if b > 0.3 and b <= 1:
        a['third'] += 1
for i in range(1,1001):
    win()
print(a)

#模拟轮盘抽奖的游戏
from random import random

#轮盘赌lpd,奖项分布jxfb,本次转盘读数bclpds,中奖情况zjqk,本次战况bczk,
def lpd(jxfb):       #定义轮盘赌函数
    bclpds = random()   #random() 随机生成0-1之间的小数
    for k, v in jxfb.items():
        if v[0]<=bclpds<v[1]:
            return k

jxfb = {'一等奖':(0,0.08),
        '二等奖':(0.08,0.3),
        '三等奖':(0.3,1.0)}
zjqk = dict()

#模拟玩1000次，统计中奖情况
for i in range(1000):
    bczk = lpd(jxfb)#本轮战况
    zjqk[bczk] = zjqk.get(bczk,0)+1#存在的话+1

for item in zjqk.items():
    print(item)
