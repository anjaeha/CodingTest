a = {1: 123, 2: 234, 3: 55}

b = sorted(a, key = lambda x : a[x])

print(b) # [3,1,2] 출력됨