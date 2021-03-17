"""
T = input()

cnt = 0

for i in T:
    elif i == 'A' or i == 'B' or i == 'C':
        cnt += 3
    elif i == 'D' or i == 'E' or i == 'F':
        cnt += 4
    elif i == 'G' or i == 'H' or i == 'I':
        cnt += 5
    elif i == 'J' or i == 'K' or i == 'L':
        cnt += 6
    elif i == 'M' or i == 'N' or i == 'O':
        cnt += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        cnt += 8
    elif i == 'T' or i == 'U' or i == 'V':
        cnt += 9
    elif i == 'W' or i == 'X' or i == 'Y' or i =='Z':
        cnt += 10
    
print(cnt)
"""



words = input().lower()
s = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

time = 0
for i in range(len(words)):
    for j in s:
        if (words[i] in j):
            time += s.index(j) + 3

print(time)

