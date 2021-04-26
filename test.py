s=list(input())

tag=False
word=''
result=''

for i in s:
  if tag==False:
    if i=='<':
      tag=True
      word += i
    elif i==' ':
      word += i
      result += word
      word=''
    else:
      word = i + word
  else:
    word=word+i
    if i=='>':
      tag=False
      result += word
      word=''

print(result+word)