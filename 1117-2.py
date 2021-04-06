'''
for letter in "python":#依次循环，把字母装入python装入letter中
    print("当前字母",letter)
'''
"""
for row in range(0,10):
    for col in range(1,row):
        print("%d * %d = %d   " %(row, col, row*col),end="")
    print("")
"""
"""
#等腰直角三角形
rows = int(input("输入列数："))
#声明变量，i用于控制外层循环(图形行数)，j用于控制空格的个数，
i = j = k = 1
print("等腰直角三角形")
for i in range (0,rows):
    for k in range (0,rows - i):
        print("   *   ",end = "")
        k += 1
    i+= 1
    print("\n")
"""
#空心三角形
rows = int(input("输入列数："))
print("仅宋体可用，打印空心三角形，去掉if-else变为实心")
for i in range(0,rows + 1):
    for j in range(0,rows - i):
        print( " ",end="")
        j +=1
    for k in range(0,2 * i - 1):
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
               if k % 2 == 0:
                    print( "*",end="")
            else:
                print( "*",end="")
        else:
            print(" ",end="")
        k +=1
    print("\n")
    i +=1


rows = int(input("请输入列数:"))
print("打印空心菱形")
for i in range(0, rows + 1):
    for j in range(0, rows - i):
        print(" ",end="")
        j += 1
    for k in  range(0,2*i-1):
        if k == 0 or k == 2 * i -2 or i == rows:
            if i == rows:
                if k % 2 == 0:
                    print("*",end = "")
                else:
                    print(" ",end = "")
            else:
                print("*",end="")
        else:
            print(" ",end="")
        k += 1
    print("\n")
    i += 1
for i in range(rows):
    for j in range(i):
        print (" ",end="")
        j += 1
    for k in range(2 * (rows - i) - 1):
        if k == 0 or k == 2 * (rows - i) - 2:
            print ("*",end="")
        else:
            print (" ",end="")
        k += 1
    print ("\n")
    i += 1
