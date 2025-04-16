num = int(input())
arr = list(map(int,input().split()))

for i in range(num):
    if(arr[i]<=10):
        print(f"A[{i}] =",arr[i])