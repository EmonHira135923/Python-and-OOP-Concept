num = int(input())

ans = num%10
val = num//10

if(ans%val==0 or val%ans ==0):
    print("YES")
else:
    print("NO")    