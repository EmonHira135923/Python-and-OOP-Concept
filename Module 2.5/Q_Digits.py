testcase = int(input())
while testcase != 0:
    testcase -= 1

    N = int(input())
    while N!=0:
        if(N==0):
            v = N%10
            print(v,end=" ")
            N = N//10
        else:
            val = N%10
            print(val,end=" ")
            N = N//10  
    print()          
