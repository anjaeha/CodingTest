n = input()
n_len = len(n) - 1
# 3자리의 숫자를 입력받으면 2자리 까지의 숫자만 계산하고 나중에 따로 계산

c = 0
# 카운팅을 위한 c

i = 0
# 몇자리인지 확인하기 위한 i

while i < n_len:
    c += 9 * (10 ** i) * (i+1)
    # 
    i+= 1

c += ((int(n) - (10 ** n_len)) + 1) * (n_len + 1)
# (120 - 100 + 1) * 3

print(c)

# 108ms 시간 소요