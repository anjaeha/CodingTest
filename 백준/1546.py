T = int(input())

n = list(map(int, input().split()))[:T]

m = max(n)

for i in range(T):
    n[i] = n[i] / m * 100

print(sum(n) / T)