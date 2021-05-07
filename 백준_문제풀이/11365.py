import sys
input = sys.stdin.readline

while 1:
    string = input().strip()
    if string == 'END':
        break

    s = list(string)
    s.reverse()
    print(''.join(s))