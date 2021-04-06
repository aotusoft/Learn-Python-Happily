"""
for i in range(3):
    print("这是第%s次循环"%(i+1))
else:
    print("循环结束")
"""
"""
a = input(str("请输入注册用户名"))
b = len(a) #len测量字符串长度
if b > 8 or b < 6 :
    print("输入无效")
"""
#对象自身具备的函数，面向对象
#具备两种数值，属性（简称它的值）和方法
"""
#判断两个字符
a = "1234"
b = "1234"
if id(a) == id(b) :
    print("和使用了同一块内存")

a = "1234"*5000
b = "1234"*5000
if id(a) == id(b) :
    print("和使用了同一块内存")
"""
mail_str = input("请输入邮箱：")
if mail_str.find("@") > 0: #find 不存在某个字符的话，返回-1       count()计数
    print("正确")
else:
    print("错误")

