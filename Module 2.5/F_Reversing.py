num = int(input())
arr = []
for i in input().split():
    arr.append(int (i))
arr.reverse()
print(*arr)