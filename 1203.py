def add_info():
        print('调出信息'.center(50, '*'))
        adduser = input('姓名：')
        addpasswd = input('号码：')
        if adduser in users:
            print('添加失败，该信息已经存在！')
        else:
            users.append(sdduser)
            passwds.append(addpasswd)
            print('添加信息成功')

def del_info():
    print('删除信息'.center(50, '*'))
    deluser = input('用户名：')
    if deluser not in users:
        print('删除失败，该信息不存在')
    else:
        delindex = users.index(deluser)
        users.remove(deluser)
        passwds.pop(delindex)
        print('删除信息成功')

def mod_info():
    findname = input("修改：")
    x = users.count(findname)
    users[x] = input("新姓名为：")
    passwds[x] = input("新密码为：")

def chk_info():
    print('查看信息'.center(50, '*'))
    count = len(users)
    for i in range(0, count):
        print('姓名：%s  电话：%s' % (users[i], passwds[i]))

def fin_info():
    findname = input("请输入你要查找的姓名：")
    x = users.count(findname)
    print("号码为：",passwds[x])

users = ["westos", "linux","1","2"]  # 初始信息
passwds = ["123", "234","345","456"]
while True:
    print("""
        *************通讯录管理系统************
            1.添加信息
            2.删除信息
            3.修改信息
            4.查看信息
            5.根据姓名查找号码
            6.退出""")
    option = input('请输入你想执行的操作：')
    if option == '1':   #添加信息
        add_info()
    elif option == '2': #删除信息
        del_info()
    elif option == '3':
        mod_info()
    elif option == '4': #查看信息
        chk_info()
    elif option == '5':
        fin_info()
    elif option == '6': #
        exit()
    else:
        print('请输入正确的操作指令')

