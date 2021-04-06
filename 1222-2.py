import os
while True:
    mulu = input('请输入目录：')
    if os.path.exists(mulu):
        os.chdir(mulu)
        ret = os.listdir(os.getcwd())
        print(ret)
        lst1 = []#保存文件名
        lst2 = []#保存目录中的子目录名
        for i in ret: #从ret中逐一获取文件名
            if os.path.isfile(i):#判断是否是文件
                lst1.append(i)#如果有则在lst1中追加一个文件名
            else:
                lst2.append(i)#如果不是则将目录名追加到目录列表中
        print('文件：{}'.format(lst1))#打印目前目录中所有文件名
        print('文件夹：{}'.format(lst2))#打印目前目录中所有子目录名
        ret1 = input('请选择：添加前缀(a)删除前缀(s)添加文件(d)删除文件(f)重命名(g)')
        if ret1.upper() == 'A':
            a= input('请输入要添加的前缀')
            for i in ret:#遍历所有文件
                os.rename(i,a + i)#使用字符串拼接
            print('添加成功')
        elif ret1.upper == 'S':
            a = input('请输入要添加的前缀：')
            for i in ret:
                os.rename(i,i.replace(a,'',i))
            print('删除前缀成功')
        elif ret1.upper == 'D':
            file_name = input('请输入要添加文件名称：')
            with open(file_name,mode = 'w')as f:
                pass
            print('添加文件成功')
        elif ret1.upper == 'F':
            del_name = input('请输入要删除的文件名：')
            os.remove(del_name)
            print()
        elif ret1.upper == 'G':
            name = input('请输入新的文件名[old new]：')
            name = name.split() #删除空格
            os.rename(name[0],name[1])
            print('删除成功')
        os.chdir('..')#留在当前文件夹，
    else:
        print('目录不存在，请新建')
        os.mkdir(mulu)
