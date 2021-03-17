
N = int(input())

m = 0

for i in range(N):
    k = str(i)
    an = i
    for j in range(len(k)):
        an += int(k[j])
    
    if an == N:
        m = i
        break
    else:
        m = 0

print(m)