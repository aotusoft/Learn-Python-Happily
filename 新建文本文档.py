users = ["root","westos","admin"]
pwds = ["123","456","admin"]

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
            if inuser == "admin" :
                while True:
                    print("""管理员登陆
                        *************操作目录************
                        1.添加会员信息
                        2.删除会员信息
                        3.查看会员信息
                        4.退出""")
                    a = input("选择功能：")
                    if a == "1":
                        temp = input("用户名")
                        temp2 = input("密码：")
                        users.append(temp)
                        pwds.append(temp2)
                    elif a == "2":
                        print(users)
                        print(pwds)
                        b = input("删除用户名")
                        x = users.count(b)
                        del pwds[x]
                        users.remove(b)
                    elif a == "3":
                        print(users)
                        print(users)
                    elif a == '4':
                        exit()
            break
        else:
            print("%s登陆失败，密码错误！"%(inuser))
    else:
        print("%s用户不存在"%(inuser))
else:
    print("已经超过三次")



