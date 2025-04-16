def sum(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum(a,b,c)     