word = input()

alp = list(range(97,123))

for x in alp:
    print(word.find(chr(x)), end = ' ')