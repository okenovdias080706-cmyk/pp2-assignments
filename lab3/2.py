n = int(input())

for i in [2, 3, 5]:
    while n % i == 0:
        n //= i 
print("Yes" if n == 1 else "No")