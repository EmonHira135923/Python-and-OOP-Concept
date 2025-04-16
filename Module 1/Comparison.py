# and or not is not is
# < > <= >= == != ++ -- ** //

a = int(input("Enter your first number : "))
b = int(input("Enter your secend number : "))
d = int(input("Enter your third number : "))
c = int(input("Enter your fourth number : "))

if(a and b == c and d):
    print("YES")
    print(type(a))
else:
    print("NO")

if(a and b == c or d):
    print("YES")
    print(type(a))
else:
    print("NO")

