words = {
    'str':'change the number to string',
    'list':'to form a list',
    'lstrip':'delete the left blank in the string',
    'range':'to form a series of number between'+
    'the first number and the end number',
    'swapcase':'change the upper to lower or reverse'}
for key,value in words.items():
    print("\n" + key.title()+':'+value.title()+'.') #title 标题内容

#练习
dict = {'Name':'张三','Age':7,'Class':'2班'}
for k in dict:
    print(dict[k])

#遍历
for k in dict:
    print(k,dict[k])

#删除
dict = {'k1':'v1','k2':'v2','k3':'v3'}
dict['k4'] = 'v4'
print("添加后: ",dict)

#添加
dict.pop('k1')
print("删除后: ",dict)

#删除k5键值对，不存在则不报错，返回None
dict = {'k1':'v1','k2':'v2','k3':'v3','k4':'v4'}
print('删除不存在的k5，返回值：',dict.pop('k5',None))

#请获取字典中k2的值

#删除k6对应值，不存在则不报错，返回None

#使dict2 = {'k1':'v1','k2':'v2','k3':'v3','a':'b'}
dict = {'k1':'v1','k2':'v2','k3':'v3'}
dict2 = {'k1':'v11','a':'','b'}
dict2.update(dict)
print('dict :  ',dict)
print('dict2 : ',dict2)



