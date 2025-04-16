num = int(input())
val = input().split()
mx_value = 0
for i in val:
    i = int(i)
    if mx_value < i:
        mx_value = i
print(mx_value)    
    