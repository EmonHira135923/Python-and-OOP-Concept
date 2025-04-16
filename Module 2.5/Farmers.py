def solve():
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    cal_value = min(a,b,c)
    print(cal_value)
t = int(input())
while t>0:
    solve()
    t -= 1