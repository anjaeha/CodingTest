import sys
input = sys.stdin.readline

mo = ['a', 'e', 'i', 'o', 'u']

while 1:
    chk1 = False
    chk2 = True
    chk3 = True

    word = input().strip()

    if word == 'end':
        break

    for i in word:
        if i in mo:
            chk1 = True

    for i in range(len(word) - 2):
        if word[i] in mo and word[i+1] in mo and word[i+2] in mo:
            chk2 = False
        elif word[i] not in mo and word[i+1] not in mo and word[i+2] not in mo:
            chk2 = False


    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            if word[i] == 'e' or word[i] == 'o':
                chk3 = True
            else:
                chk3 = False



    if chk1 == True and chk2 == True and chk3 == True:
        print('<%s> is acceptable.' % (word))
    else:
        print('<%s> is not acceptable.' % (word))
