num = int(input())
arr = list(map(int,input().split()))

cnt_2,cnt_3=0,0

for i in range(num):
    if arr[i]%2==0:
        cnt_2 += 1
    elif arr[i]%3==0 and arr[i]%2==0:
        cnt_2 += 1
    elif arr[i]%3==0:
        cnt_3 += 1    

print(cnt_2,cnt_3)