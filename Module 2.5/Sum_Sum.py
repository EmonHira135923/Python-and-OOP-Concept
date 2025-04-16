num = int(input())
arr = list(map(int,input().split()))

sum_pos,sum_neg=0,0

for i in range(num):
    if(arr[i]>=0):
        sum_pos += arr[i]
    else:
        sum_neg += arr[i]    

print(f"{sum_pos} {sum_neg}")        
