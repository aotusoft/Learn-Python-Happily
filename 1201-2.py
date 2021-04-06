#list列表
"""
my_list = ["张三","李四","王五","赵六"]
for i in my_list:
    print(i) #遍历打印
print(my_list[2])#使用下标访问具体值
print(my_list[5])

def menu(): #菜单函数
    menu_list = ["+","-","*","/"]
    print("简易计算器")

    for i in menu_list:
        print(i)

    return
menu()
menu_list = ["+","-","*","/"]
x = len(menu_list)
print(x)
"""
#append追加元素

name_list = [] #定义空列表
for i in range(1,4):
    temp = input("请输入人名：")
    name_list.append(temp)

    print("列表上有三个人",len(name_list))
for i in name_list:
    print(i)

#insert插入列表

name_list = [1,2,3,4]
for i in name_list:
    print(i)
name_list.insert(2,"大仙")
for i in name_list:
    print(i)

#修改
    
name_list = [1,2,3,4]
print(name_list)
name_list[1] = 22
print(name_list)

#extend合并

my_list = ["张三","李四","张三","王五","赵六"]
my_list2 = [5,6]
my_list.extend(my_list2)
print(my_list)

#del删除
del my_list[3]

#remove删除
#my_list.remove["张三"]

#pop弹出

my_list.pop(2)

#clear清空

my_list2.clear

#len统计

num = len(my_list)
print(num)

#count统计

x = my_list.count("张三")
print(x)

#sort 排序1 升序

my_list = [100,33,99,1,2,3]
my_list.sort()
print(my_list)

#sort(reverse = True) 排序2 降序

my_list.sort(reverse = True)
print(my_list)

#reverse 倒序

my_list.reverse()
print(my_list)
















