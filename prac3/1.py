#1
def dias(n):
    return n
n=int(input())
print(dias(n))

#2
def numbers(a, b):
    sum=a+b
    return sum

a = int(input())
b = int(input())
result=numbers(a,b)
print(result)

#3
def greet(name, message="Hello"):
    print(message, name)
greet("Dias")
greet("Dias", "Welcome")

#4
def sum_all(*numbers):
    total = 0
    
    for num in numbers:
        total += num
    return total
print(sum_all(1, 2, 3, 4, 5))