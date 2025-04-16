a,b = input().split()
a = int(a)
b = int(b)

if(a%b==0):
    print("Multiples")
elif(b%a==0):
    print("Multiples")    
else:
    print("No Multiples")    