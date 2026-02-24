def integer(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
for value in integer(n):
    print(value)