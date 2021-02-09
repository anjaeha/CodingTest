

N = int(input())

channel = []

for i in range(N):
    name = input()
    if name == 'KBS1':
        idx1 = i
    elif name == "KBS2":
        idx2 = i
    channel.append(name)

res = ''
res += '1' * idx1 # KBS1 으로 이동
res += '4' * idx1 # KBS1을 첫번째로 보냄

if idx1 > idx2: # KBS1 이 KBS2 보다 아래 있으면 KBS2의 위치를 하나 낮게함.
    idx2 += 1

res += '1' * idx2 # KBS2 로 이동
res += '4' * (idx2-1) # KBS2를 두번째로 보냄.

print(res)

#