from collections import *

N,M = (input().split())
N = int(N)
M = int(M)
arr = list(map(int,input().split()))

freq = Counter(arr)

for i in range(1,M+1):
    print(freq[i])