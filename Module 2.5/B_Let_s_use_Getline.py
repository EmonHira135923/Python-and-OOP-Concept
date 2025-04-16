word = str(input())

for ch in word:
    if(ch=='\\'):
        break
    print(ch,end="")