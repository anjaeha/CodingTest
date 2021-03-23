import sys
input = sys.stdin.readline

T = int(input())


for case in range(T):
    n, m = map(int, input().split())
    for _ in range(m):
        x, y = map(int, input().split())
    
    print(n-1)