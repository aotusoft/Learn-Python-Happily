#row行
#col列
"""
row = 1
while row <= 5:
    print("*" * row ,)#end = ""输出不会换行
    row += 1
"""
"""
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d  " %(row, col, row * col) ,end = "")
        col += 1
    print("")
    row += 1
"""
'''
i = 1
row = 1
while row <= 10:
    row += 1
    if 0 == x%row :
        break
        print("质因数为%d"%row)
    else:
        print("质数")
'''
'''
i = 2
while i <= 100:
    r = 2
    while r <= i:
        if  i%r == 0 and i != r:
            break
        if i%r == 0 and i == r:
            print(i)
        i += 1
    r += 1
'''
z = 2
while z <= 100:
    x = 2
    while x <= z:#如果不是质数 break
        if (z % x ==0) and (z != x):
            break#不是质数退出当前循环
        if (z %x == 0) and (z == x):
            print(z)#是质数，打印
        x += 1
    z += 1




        
