import sys
input = sys.stdin.readline

t = int(input())

for case in range(t):
    s = list(input().strip())

    check = True
    answer = ''

    for i in range(len(s)):
        if s[i] not in 'ABCDEF':
            check = False
    a, c, f = -1, -1, -1
    if check:
        for i in range(len(s)):
            if s[i] == 'A':
                if a == -1:
                    a = i
            if s[i] == 'C':
                if c == -1:
                    c = i
            if s[i] == 'F':
                if f == -1:
                    f = i
        
        if s[0] in 'BCDEF':
            answer += s[0]



        if s[0] not in 'ABCDEF':
            check = False

        if s[-1] not in 'ABCDEF':
            check = False

        for i in range(f-a):
            answer += 'A'

        for i in range(c-f):
            answer += 'F'
        
        for i in range(len(s) - c):
            answer +='C'
        
        if s[-1] in 'ABDEF':
            answer += s[-1]
    
    s = ''.join(s)
    if answer == s:
        print('Infected!')
    else:
        print('Good')