"""
i = 0
s = 0
while i < 100:
    i = i + 2
    s = i + s
print(s,i)
"""
"""
i = 0
result = 0
while i <= 100 :
    if i % 2 == 0 :
        print(i)
        result += i
    i += 1
print(result)
"""
i = 0
while i <= 10:
    if i == 7:
        i += 1
        continue #break
    print(i)
    i+=1
