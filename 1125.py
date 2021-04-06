"""
def test1():
    print("*"* 50)
    print("test 1 模块")
    print("*"* 50)

def test2():
    print("-"* 50)
    print("test 2 模块")
    test1() #函数的嵌套
    print("-"* 50)

#主程序
test2()
"""
"""
char = "="
time = 50
#
def line_printer(char):
    print("*"* 50)
line_printer(char)
#任意字符组成的分割线
def line_printer(char):
    print(char* 50)
line_printer(char)
#任意重复次数的分割线
def line_printer(char,times):
    print(char*times)
#
def line_printers(char,times):
    row = 0
    while row < 5:
        line_printer(char,times)
        row += 1
        
#主程序
char = "="
times = 50
line_printers(char,times)
char = "*"
times = 50
line_printer(char,times)
"""

"""
def multiple_table():
    #
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            #print("*",end = "")
            print("%d * %d = %d   " %(col,row,col*row),end = "")
            col += 1
        #print("%d" %row)
        print("")
        row += 1

multiple_table()
multiple_table_copy = multiple_table
print(id(multiple_table))
print(id(multiple_table_copy))
"""
#函数参数的引用
def test(num):
    print("-" * 50)
    print("%d 的内存地址为 %x"%(num,id(num)))
    result = 100
    print("返回值  %d 的内存地址为 %x"%(result,id(result)))
    print("-" * 50)
    return result
a = 10
print("调用函数前的内存地址为 %x"%id(a))
r = test(a)
print("调用函数后实参的内存地址为 %x"%id(a))
print("调用函数后返回值的内存地址为 %x"%id(r))















