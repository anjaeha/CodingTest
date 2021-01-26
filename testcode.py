T = input()
answer = 0

for i in range(1, len(T)):
    if T[i-1] == T[i]:
        answer += 5
    else:
        answer += 10

print(answer + 10)
