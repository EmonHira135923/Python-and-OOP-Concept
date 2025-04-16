num = int(input())
arr = list(map(int,input().split()))
mx_value = max(arr)
min_value = min(arr)
mx_value_index = arr.index(mx_value)
min_value_index = arr.index(min_value)
arr[mx_value_index],arr[min_value_index] = arr[min_value_index],arr[mx_value_index]
print(*arr)