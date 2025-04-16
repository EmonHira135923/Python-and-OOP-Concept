num = int(input())

while num!=0:
    digit = num%10    
    num = num//10
if(digit%2==0):
    print("EVEN")
else:
    print("ODD")        