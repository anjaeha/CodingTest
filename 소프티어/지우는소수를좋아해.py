n, m = map(int, input().split())
root = [list(map(int, input().split())) for _ in range(m)]

max_num = max(root, key = lambda x : x[2])[2]

primes = []
erato = [False, False] + [True]*max_num
for i in range(2, max_num + 2):
    if erato[i]:
        primes.append(i)
        for j in range(2*i, max_num + 2, i):
            erato[j] = False

result = 0
for i in primes:
    temp = []
    for j in range(m):
        if root[j][2] <= i:
            temp.extend(root[j][0:2])
    if list(set(range(1, n + 1))) == list(sorted(set(temp))):
        result = i
        break

print(result)