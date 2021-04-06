#文件
#读
'''
f = open("test.txt",'r')#文件变量，句柄
#f1 = f.read()
f2 = f.readline()#读一行 磁带特性
print(f2)
f3 = f.readline(5) #字符
print(f3)
f4 = f.readlines(1) #行 列表返回
print(f4)
f.close()
'''
#写
"""
f = open("test.txt",'r+')
f.write('Hello world!\n中文')
f.close()
"""

with open('test.txt','r') as f:
    sent = f.readlines()#读取多行,用分隔符换行

    for i in range(len(sent)):#用\n以局单位分割
        if sent[i] != '':
            sent[i] =sent[i][0].upper() + sent[i][1:-1] #首字母大写转小写
            #[1:-1]从第一到最后一行

        with open ('test.txt', 'w') as w:#逐行写,最后关闭
            for j in range(len(sent)):
                if sent[j] != '':
                    w.write(sent[j] + '\n')
            f.close()
f.close()





















    
