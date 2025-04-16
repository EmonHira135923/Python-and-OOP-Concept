num = int(input())
ar = list(map(int,input().split()))

if(num%2!=0):
    for i in range(num-1,0,-1):
        if(i%2!=0):
            print(ar[i],end=" ")  
if(num%2==0):
    for i in range(num,0,-1):
        if(i%2!=0):
            print(ar[i],end=" ")
        