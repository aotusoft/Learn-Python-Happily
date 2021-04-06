qq_num = 123456
qq_pwd = "123456"
num = int(input("请输入账号："))
pwd = input("请输入密码：")
if qq_num == num and qq_pwd == pwd:
   print("账号密码输入正确") 
else:
   print("账号或密码输入错误")
