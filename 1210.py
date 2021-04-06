#字符串
print("{0} {1}".format("hello","world")) #
print("{a} {b}".format(a = "hello",b = "world")) #

import random
count = 0
right = 0
while True:
    a = random.randint(0,9)
    b = random.randint(0,9)
    op = ['-','+','*','/']
    s = random.choice(op)
    if s == '+':
        result = a+b
    elif s == '-':
        if a < b:
            c = a
            a = b
            b = c
        result = a-b
    elif s == '*':
        result = a*b
    elif s == '/':
        if a%b != 0 :
            continue
        res = a/b
        result = int(res)
    if s == '/' and b == 0:
        continue
    else:
        print("%d%s%d "%(a,s,b))
    r = str(input("输入答案："))
    if str(result) == r:
        count += 1
        right += 1
        print("正确")
    elif r == "q":
        break
    else:
        print("错误")
        count += 1
print("共答题%d,正确%d道"%(count,right))
if count == 0:
    exit()
else:
    percent = right/count
    print("正确率为%·2f"%(percent))

















        
