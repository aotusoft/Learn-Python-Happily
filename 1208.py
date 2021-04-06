example = [0,1,2,3,4,5,6,7,8,9]
print(example[:2]) #截取结果不包含结束位置

# example = [1,2,3,4,5]
# if 1 in example:
#     print("属于")

# example = [[1,2,3],2,3,4,5]
# if 1 in example:
#     print("属于")
# else:
#     print("不属于")

# for i in example[0]:#访问子列表
#     print(i)
# print(example[0][2])
"""
li = [123,"xyz","zara","abc",123,["abc",123]
print(li.count(123))
print(li.count("xyz"))
print(li.count("zara"))
print(li.count("abc"))
print(li.count(["abc",123]))
"""
"""
#元组
tup1 = (1,2,3,4,5)
tup2 = ("Google","runoob",1997,2000)
tup3 = "a","b","c","d"
tup4 = ()
tup5 = 9, #一个元素要加逗号
print(tup1)
print(tup2)
print(tup3)
print(tup4)
#下标
print(tup1[1])
#元组的乘法
*
"""

#元组元素的添加 在(1,2,3,4,5)的“2”前插入“6”
tup = (1,2,3,4,5)
tup1 = tup[:1]
tup2 = tup[1:]
tup = tup1 + (6,) + tup2

print(tup1)
print(tup2)
print(tup)

#元组元素的删除
tup =(1,2,3,4,5)
tup2 = tup[:1] + tup[3:]
print(tup2)

#更新元素
tup2 = [:1] + (6,) + tup[2:]
print(tup2)

str1 = "Hello World"
print(str1)
print(str[0])
print(str1[2:])
print(str1[:])
print([::-1])

casefold()
str1 = "Hello World"
print(str1.casefold())

str1 = "www.taobao.com"
sub "b"
print(str1.count(sub))
print(str1.count(tao,0,10))

#index()如果包含一个字串就返回1，不包含则出现一个异常
str1 = "Runoob example . . . wow!!!"
str2 = "exam"
print(str1.index(str2)) 
print(str1.index(str2,5)) #指定从第5个位置后查找
print(str1.index(str2,10)) #指定从第10个位置后查找

#join()拼接
seq1 = ("r","u","n","o","o","b")
print("".join(seq1)) 
# s = "*" *3 #变量做分隔符
# print(s.join(seq1)) 

#replace 替换
str1 = "Hellow world"
str2 = "Python"
print(str1.replace("world",str2))

#替换
print(str1.replace("o","q",2))#第三个参数表示替换次数
