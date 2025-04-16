a,b = input().split()
a = int(a)
b = int(b)

sum_a = a + b 
sum_mi = a - b 
sum_mu = a * b 
sum_di = float(a/b) 

print(f"{a} + {b} = {sum_a}")
print(f"{a} - {b} = {sum_mi}")
print(f"{a} * {b} = {sum_mu}")
print(f"{a} / {b} = {sum_di:.2f}")