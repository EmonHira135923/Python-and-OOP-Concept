def student(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
num = int(input())
arr = tuple(map(int,input().split()))      
student(numbers=arr)  