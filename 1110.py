# 일의자리 + 십의자리 => 일의자리 + 더한거의 일의자리 

num = int(input())

cnt = 0
new_num = 0
temp = 0
check = num

while True:
    temp = (num // 10) + (num % 10)
    new_num = (num % 10) * 10 + (temp % 10)
    cnt += 1
    num = new_num
    if num == check:
        break

print(cnt)