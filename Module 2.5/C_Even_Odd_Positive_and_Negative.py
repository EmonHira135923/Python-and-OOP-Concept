num = int(input())

input_val = input().split()

even,odd,pos,neg,zero=0,0,0,0,0

for val in input_val:
    val = int(val)
    if(val%2==0):
        even += 1
    else:
        odd += 1
    if(val==0):
        zero+=1
    elif(val>0):
        pos += 1
    else:
        neg += 1
print("Even:",even)                        
print("Odd:",odd)                        
print("Positive:",pos)                        
print("Negative:",neg)                        