import sys
input = sys.stdin.readline

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

h = h2 - h1
m = m2 - m1
s = s2 - s1

if s < 0:
    s += 60
    m -= 1

if m < 0:
    m += 60
    h -= 1

if h < 0:
    h += 24

if h == 0 and m == 0 and s == 0:
    print("24:00:00")
else:
    print("%02d:%02d:%02d" % (h, m, s))
