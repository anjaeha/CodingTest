n = int(input())

a, b = 1, 1
for _ in range(n):
    a, b = b, (a+b) % 10

print(a)