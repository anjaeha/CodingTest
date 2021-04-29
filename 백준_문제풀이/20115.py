import sys
input = sys.stdin.readline

n = int(input())

drink = list(map(int, input().split()))

drink.sort(reverse=True)

for i in range(1, len(drink)):
    drink[i] = drink[i] / 2

print(sum(drink))