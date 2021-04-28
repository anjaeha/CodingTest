import sys
input = sys.stdin.readline

string = input().strip()

string = string.replace("XXXX", "AAAA")
string = string.replace("XX", "BB")


if 'X' in string:
    print(-1)
else:
    print(string)