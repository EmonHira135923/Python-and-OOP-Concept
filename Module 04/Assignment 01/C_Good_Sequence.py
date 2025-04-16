from collections import *

N = int(input())
arr = list(map(int,input().split()))

freq = Counter(arr)

res = 0

for key,value in freq.items():
    if(key==value):
        continue
    elif(value>key):
        res += (value-key)
    else:
        res += value
print(res)        