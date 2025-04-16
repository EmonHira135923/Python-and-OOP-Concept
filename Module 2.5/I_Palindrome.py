word = str(input())
i = 0
j = len(word)-1
flag = True

while i<j:
    if(word[i]!=word[j]):
        flag = False
        break
    i+=1
    j-=1
if(flag==True):
    print("YES")
else:
    print("NO")    

# print(word,word_size)