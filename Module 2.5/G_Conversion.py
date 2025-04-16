word = str(input())

for size_t in word:
    if(size_t.islower()):
        print(size_t.upper(),end="")
    elif(size_t.isupper()):
        print(size_t.lower(),end="")
    elif(size_t==","):
        print(" ",end="")
    else:
        print(size_t,end="")    