# num = int(input())
# arr = list(map(int,input().split()))
# min_opreation = float('inf')

# for i in arr:
#     cnt = 0
#     while i%2==0:
#         i //= 2
#         cnt += 1
#     min_opreation = min(min_opreation,cnt)
# print(min_opreation)        
        
n = int(input())

arr = list(map(int,input().split()))

mn = float('inf')

for val in arr :
    cnt = 0
    while val % 2 == 0:
        val //= 2
        cnt += 1 
    mn = min(mn, cnt)

print(mn)