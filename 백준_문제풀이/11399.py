import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()

wait = 0
answer = 0

for i in range(n):
    answer += wait + p[i]
    wait += p[i]
    
print(answer)