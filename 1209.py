#split()

str1 = "this is string example...wow!!!"
print(str1)
print(str1.split())

"""
str1 = '''
    白日依山尽
    黄河入海流
    欲穷千里目
    更上一层楼
        ‘'''
print(str1)
print(str1.split())
"""
"""
while True:
    s = input("输入变量名：")
    if s == "exit":
        print("欢迎下次使用")
        break
    if s[0].isalpha() or s[0] == "_":
        for i in s[:]:
            if not(i.isalnum() or i == "_"):
                   print("%s变量名不合法" %s)
                   break
        else:
            print("%s变量名合法" %s)
    else:
        print("%s变量名不合法" %s)
"""
"""
str1 = input("")
str2 = str1.split()
str3 = str2[::-1]
print(str3)
print(" ".join(str3))

print(" ".join(input().split()[::-1]))
"""
"""
str1,str2 = input("第一个串："),input("第二个串：")
#str2 = input("第二个串"）
for i in str2:
    str1 = str1.replace(i,"")
print(str1)
"""
s = input("输入字母：")
for i in range(len(s)):
    if s[i] <= "A" and s[i] >= "Z":  #ASCII 码。。。。。。。。。。。
        print("DISLIKE")
        break
    else:
        if i < len(s)-1 and s[i] == s[i+1]:
            print("DISLIKE")
            break
else:
    print("LIKE")
        


















    
