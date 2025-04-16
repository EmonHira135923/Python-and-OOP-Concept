# lamda argumments : expression 

N = int(input())

ans = lambda x : x*x

print(ans(N))

M = int(input())
val = lambda x,y:x+y
print(val(N,M))

key = int(input())
arr = list(map(int,input().split()))

val_sum = list(map(lambda val : val*val,arr))
print(*val_sum)