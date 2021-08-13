import re

try:
    while 1:
        s = input()
        while re.search('BUG', s):
            s = re.sub('BUG', "", s)
        print(s)
except EOFError:
    pass
