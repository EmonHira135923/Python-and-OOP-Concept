def solve():
    word = str(input())
    cnt_0,cnt_a,cnt_z = 0,0,0
    for i in word:
        if i.isdigit():
            cnt_0 += 1
        elif i.isupper():
            cnt_a += 1
        else:
            cnt_z += 1    
    print(cnt_a,cnt_z,cnt_0)


t = int(input())
while t>0:
    solve()
    t -= 1