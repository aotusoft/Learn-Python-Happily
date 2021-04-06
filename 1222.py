'''
fo = open("test.txt",'r',encoding = 'UTF-8')#UTF-8双 r只读
#路径要用\\
lines = list(fo)
#print(lines)
#fo.close()
#查找位置
str = fo.read(10)
print('读取到的字符串：'+str)
position = fo.tell()
print('当前位置：',position)
#再次读取10个字节
str = fo.read(10)
print('读取到的字符串：'+str)
#重新定位
position = fo.seek(0,0)#seek(0,0)从文件头开始  移动0个字节
#再次读取10个字节
str = fo.read(10)
print('读取到的字符串：'+str)
fo.close()
'''

#目录操作
import os
#获取目录
'''
p = os.getcwd() 
print(p)

#chdir(path) 改变工作目录到指定路径
os.chdir("C:\\")
p = os.getcwd()
print(p)
'''
#chdir(path)返回指定文件夹和文件
os.chdir("D:\\PY-Files")
print(os.listdir())
os.mkdir("./test")
#os.chdir("./test")
print('写入成功')

#remove(path)删除
#rmdir(path)退回到根目录
#removedirs(path)删除文件夹
"""
os.rmdir('D:\\PY-Files')
os.removedirs('./test')
print('删除成功')
"""
#rename重命名
os.rename('test.txt','Test.txt')
print(os.listdir())
os.rename('Test.txt','test.txt')




