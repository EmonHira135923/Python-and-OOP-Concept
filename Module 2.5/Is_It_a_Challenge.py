num = int(input())

if num>0:
    for i in range(1,num+1,1):
        print(i,end=" ")
elif num<0:
    for i in range(num,1,1):
        print(i,end=" ")        