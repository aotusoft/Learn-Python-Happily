"""
i = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            x =a*100+b*10+c
            if a != b and b != c and a != c:
                i += 1
                print(a*100+b*10+c)
print(i)
"""
#水仙花数
"""
for i in range(100,1000):
    a = i//100
    b = i%100//10
    c = i%10
    if a**3+b**3+c**3 == i:
        print(i)
"""
#解方程
"""
#x+y=20 x-y=8
for x in range(1,21):
    for y in range(1,21):
        if x + y == 20 and x - y == 8:
            print(x,y)
"""
#母鸡
for m in range(1,100):
    for n in range(1,100):
        for b in range(1,100):
            if m+n+b==100 and 5*m+3*n+b/3==100:
                print(m,n,b)
