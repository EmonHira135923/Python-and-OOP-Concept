a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

mx_value = max({a,b,c})
mn_value = min({a,b,c})
print(f"{mn_value} {mx_value}")