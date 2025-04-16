arr = {}
N = int(input())

for i in range(N):
    line = input()
    key, val = line.split(":", 1)
    arr[key.strip()] = val.strip()

pop_key = input()
print(arr.pop(pop_key,))

print(arr)
