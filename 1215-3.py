'''
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
lis[0][1][1] = '100' #20
lis[0][1][3] = '100' #89
lis[0][1][2]['k1'][1] = '100'
lis[0][1][2]['k1'][2] = 101
print(lis)
'''
import random
li1 = [] #容器
d = dict()#容器或 d = {}
for i in range(1000):
    li1.append(random.randint(20,100))
for i in li1:
    if i not in d:
        d[i] = 1#产生键值
    else:
        d[i] += 1#键值加一
li1.sort()
print(li1)
print(d)

print('管理员登陆界面'.center(50, '*'))
users = ['westos', 'linux']  # 初始会员信息
passwds = ['123', '234']
inuser = input("用户名：")
inpasswd = input("密码：")
if inuser == 'admin':
    if inpasswd == 'admin':
        print("管理员%s登陆成功" % (inuser))
        while True:
            print("""
            *************操作目录************
            1.添加会员信息
            2.删除会员信息
            3.查看会员信息
            4.退出""")
            option = input('请输入你想执行的操作：')
            if option == '1':
                print('调价会员信息'.center(50, '*'))
                adduser = input('用户名：')
                addpasswd = input('密码：')
                if adduser in users:
                    print('添加失败，该会员信息已经存在！')
                else:
                    users.append(sdduser)
                    passwds.append(addpasswd)
                    print('添加信息成功')
            elif option == '2':
                print('删除会员信息'.center(50, '*'))
                deluser = input('用户名：')
                if deluser not in users:
                    print('删除失败，该会员信息不存在')
                else:
                    delindex = users.index(deluser)
                    users.remove(deluser)
                    passwds.pop(delindex)
                    print('删除信息成功')
            elif option == '3':
                print('查看会员信息'.center(50, '*'))
                count = len(users)
                for i in range(0, count):
                    print('用户名：%s  密码：%s' % (users[i], passwds[i]))
            elif option == '4':
                exit()
            else:
                print('请输入正确的操作指令')

    else:
        print("%s登陆失败：密码错误！" % (inuser))
else:
    print("用户%s不存在" % (inuser))


