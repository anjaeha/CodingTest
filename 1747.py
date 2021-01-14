N = int(input())

# 에라토스테네스의 체 만들기
limit = 1003001
#1,000,000 까지 없으면 팰린드롬&소수를 만족하는 수.

era = [1] * (limit+1)
# 전부 1로 limit 크기만큼 만들기

era[0], era[1] = 0, 0
for i in range(2, limit):
  if era[i]:
    for j in range(i *2, limit, i):
      era[j] = 0

#팰린드롬인지 확인하기 위한 함수 생성
def pal(n : int):
  s = str(n)
  if s == s[::-1]:
    return True
  return False

# N부터 limit까지 팰린드롬&소수를 만족하는 수를 찾음
for num in range(N, limit+1):
  if era[num] and pal(num):
    print(num)
    break
else:
  print(1003001)
