"""
a = y
if a == "n":
    else:
        scores = []
        count = int(input("请输入人数："))
        for i in range(0,count):
            scores.append(0)
            scores[i] = int(input("请输入第%d位评委的得分："%(i+1)))
            if scores[i] < 0 or scores[i] > 10:
                scores[i] = int(input("输入错误，请输入第%d位评委的得分："%(i+1)))
        scores.sort()
        num = (sum(scores) - scores[0] - scores[-1])/(count-2)
        print("去掉一个最高分%d分，去掉一个最低分%d分，最终得分：%.2f"%(scores[-1],scores[0],num))
    a  = 
"""
"""
list1 = [1,2,[3,4],5,6]
print(list1)
list1[2][0] = 6
print(list1)

list1.append(["zhulin","xiaoxi"])
list1.extend(["zhulin","xiaoxi"])
list1.insert(2,"zhulin")
"""
#列表分段
"""
a = [1,2,3,4,5,6,7,8]
print(a[:])
print(a[:4]) #后边为截止位，取0—4
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])
print(a[::-1]) #::步长
print(a[:2])
print(a[1::2])
print(a[::-2])
"""
"""
month = int(input("month:"))
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]

if month in spring:                     #in判断，不存在返回True
    print("%s月是春天"%(month))
elif month in summer:
    print("%s月是夏天"%(month))
elif month in autumn:
    print("%s月是秋天"%(month))
elif month in winter:
    print("%s月是冬天"%(month))
else:
     print("请输入正确月份")
"""

users = ["root","westos"]
pwds = ["123","456"]

trycount = 0

while trycount < 3:
    inuser = input("用户名：")
    inpwd = input("密码：")
    trycount += 1
    if inuser in users:
        index = users.index(inuser)#先找出用户所对应的索引值，它在哪个位置
        pwd = pwds[index]#找出对应索引值的密码
        #判断密码是否正确
        if inpwd == pwd:
            print("%s登录成功"%(inuser))
            break
        else:
            print("%s登陆失败，密码错误！"%(inuser))
    else:
        print("%s用户不存在"%(inuser))
else:
    print("已经超过三次")













    




