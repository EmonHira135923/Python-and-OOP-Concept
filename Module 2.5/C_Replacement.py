num = int(input())
arr = list(map(int, input().split()))
for i in range(num):
    if(arr[i]>0):
        print("1",end=" ")
    elif(arr[i]==0):
        print("0",end=" ")
    elif(arr[i]<0):
        print("2",end=" ")        