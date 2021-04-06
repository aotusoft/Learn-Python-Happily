print("请输入单价和质量")
p  =   float(input("请输入单价："))
w  =   float(input("请输入质量："))

num = p*w-5
print("原价为"+str(p*w)+"元")
if num < 0:
   print("价格为0元")
else:
   print("价格为"+ str(p*w-5) + '元')

