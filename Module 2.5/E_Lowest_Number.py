num = int(input())
arr = list(map(int,input().split()))
mn_val = min(arr)
print(mn_val,arr.index(mn_val)+1)