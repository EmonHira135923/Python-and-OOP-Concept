word = str(input())

cnt = 0

for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt -= 0
    else:
        cnt += 1    
print(cnt)        