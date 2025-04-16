def solve():
    num = int(input())
    arr = list(map(int,input().split()))
    x = int(input())
    if x in arr:
        print("YES")
    else:
        print("NO")

t = int(input())
while t>0:
    solve()
    t -= 1