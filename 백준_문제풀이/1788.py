n = int(input())

a, b = 0, 1
for i in range(abs(n)):
    a, b = b, (a + b) % 1000000000

if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

print(a)