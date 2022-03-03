s = input().strip()
flag = False
temp = ''
answer = ''

for i in s:
    if i == ' ':
        if flag:
            answer += i
        else:
            answer += temp[::-1] + i
            temp = ''
    elif i == '<':
        answer += temp[::-1]
        temp = ''
        flag = True
        answer += i
    elif i == '>':
        flag = False
        answer += i
    else:
        if flag:
            answer += i
        else:
            temp += i

answer += temp[::-1]
print(answer)