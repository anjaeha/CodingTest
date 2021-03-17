# 소수 구하는 방법을 에라토스테네스의 체를 이용함


M = int(input())
N = int(input())
num = []
arr = set(i for i in range(2, N+1))

for i in range(2, N+1):
    if i in arr:
        arr -= set(range(i*2,N+1,i))
#에라토스테네스의 체를 이용하여 2부터 N까지의 소수를 구함.

for j in arr:
    if j >= M and j <= N:
        num.append(j)
# 2부터 N까지의 소수중 M부터 N까지의 소수를 구하기 위한 작업
# 일 두번안하고 한번에 하는 방법 있는지??

if not num:
    print(-1)
else:
    print(sum(num))
    print(min(num))