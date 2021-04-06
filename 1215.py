#字典定义
empty = {} #空字典

#直接定义
dict1 = {'Name':'张三','Age':7,'Class':'2班'}
print(dict1)

#使用元组或列表，使用dict()进行转化
dict2 = dict((('奔驰',70),('宝马',105),(' 奥拓',115)))
print(dict2)

#使用等号进行定义
dict3 = dict(F = 70, i = 105, s = 115)
print(dict3)

dict3 = dict(奔驰 = 70, 宝马 = 105, 奥拓 = 115)
print(dict3)

#直接赋值的方式创建字典或
#修改字典的值
dict3['奔驰'] = 115
print(dict3)

#访问字典数据
print(dict1['Name'],dict1['Age'])
print(dict2['宝马'],dict2['奔驰'])

#清空字典  clear()可清空列表 元组 字典
dict1.clear()
print(dict1)

#删除字典的某个键k
dict1 = {'Name':'张三','Age':7,'Class':'2班'}
del dict1['Name']

#删除字典
del dict1

#print(dict1)
dict1 = {'Name':'张三','Age':7,'Class':'2班'}

#键出现多次，后边覆盖前边
dict4 = {'Name':'张三','Name':'李四',}

#字典内置方法
#len()计算字典项数
print(len(dict1))
#转换为字符串
#str()字符串
print(str(dict1))
#copy()浅复制
dict5 = dict1.copy()
print(dict5)
#fromkeys()将元组转换为字典
s = ('奔驰', '宝马', '奥拓')
dict2 =dict1.fromkeys(s)
print(dict1)
print(dict2)
#get()返回一个键的值，不存在返回缺省值
print(dict1.get('Name'))
#items()返回元组形式
print(dict1.items())
#keys()返回字典中所有的键
print(dict1.keys())
#pop()删除
dict1.pop('Name')
print(dict1)
dict1 = {'Name':'张三','Age':7,'Class':'2班'}
#随机删除
print(dict1.popitem())
print(dict1)
dict1 = {'Name':'张三','Age':7,'Class':'2班'}
#values()返回所有值
print(dict1.values())
查询是否存在
if 'name' in dict1:
    print("存在这个键值")








#定义用户密码表
user_pwd = {"root":"12346","Guset":"1111"}
