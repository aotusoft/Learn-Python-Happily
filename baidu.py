# 第好几个方法实例
import requests #先导入爬虫的库，不然调用不了爬虫的函数
response = requests.get( "http://www.zhihu.com")  #第一次访问知乎，不设置头部信息
print( "第一次,不设头部信息,状态码:"+str(response.status_code ))# 没写headers，不能正常爬取，状态码不是 200
#下面是可以正常爬取的区别，更改了User-Agent字段
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}#设置头部信息,伪装浏览器
response = requests.get( "http://www.baidu.com" , headers=headers )  #get方法访问,传入headers参数，
print( "状态码:"+str(response.status_code) ) # 200！访问成功的状态码
response.encoding = "utf-8" #设置接收编码格式
print("\nr的类型" + str( type(response) ) )
print("\n状态码是:" + str( response.status_code ) )
print("\n头部信息:" + str( response.headers ) )
#print( "\n响应内容:" )
print( response.text )
#保存文件
file = open("./百度.html","w",encoding="utf-8")  #打开一个文件，w是文件不存在则新建一个文件，这里不用wb是因为不用保存成二进制
file.write( response.text )
file.close()
