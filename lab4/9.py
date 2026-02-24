def power(n):
    value = 1
    for _ in range(n + 1):
        yield value
        value *= 2

n = int(input())
print(*power(n))