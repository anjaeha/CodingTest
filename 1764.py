n, m = map(int, input().split())

hear = set()
see = set()

for i in range(n):
    hear.add(input())
for i in range(m):
    see.add(input())


answer = sorted(list(hear & see))

print(len(answer))
for i in range(len(answer)):
    print(answer[i])
