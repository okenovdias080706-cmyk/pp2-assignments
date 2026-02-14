nums = list(map(int, input().split()))
primes = []

for n in nums:
    if n > 1:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            primes.append(n)
if primes:
    print(*primes)
else:
    print("No primes")