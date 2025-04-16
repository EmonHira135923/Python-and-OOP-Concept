num = int(input())
arr = list(map(int,input().split()))
x = int(input())
# print(num)
# for i in arr:
    # print(i,end=" ")
# print()
# print(x)    

if x in arr:
    print(arr.index(x))
else:
    print("-1")    