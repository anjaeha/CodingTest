a = {1: 123, 2: 234, 3: 55}

b = sorted(a, key = lambda x : a[x])

print(b) # [3,1,2] 출력됨

c = sorted(a.items(), key = lambda x : x[1])

for i in range(len(c)):
    print(c[i][1], end = ' ')