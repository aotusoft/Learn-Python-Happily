import random
"""
has_ticket = True
knife_length = 20
if has_ticket:
    print("有车票，可以开始安检。。。")
    if knife_length >= 20:
        print("不允许携带 %d 厘米长的刀上车" %knife_length)
    else:
        print("安检通过，祝您旅行愉快。。。")
else:
    print("大哥，您要先买票啊")
"""
num = True
while num :
    player = int(input("请出拳，石头(1)/剪刀(2)/布(3)："))
    computer = random.randint(1,3)
    if((player == 1 and computer == 2 ) or
       (player == 2 and computer == 3) or
       (player == 3 and computer == 1)):
        print("噢噢，电脑弱爆了")
    elif player == computer:
        print("心有灵犀，再来一盘")
    elif player < 9:
        print("输入无效")
    elif player == 9:
        num = False
    else:
        print("不行，我要和你决战到天亮")
    #print(player,computer)

"""
i = 1
while i <= 5 :
    print("Hello Python")
    i = i + 1
"""
