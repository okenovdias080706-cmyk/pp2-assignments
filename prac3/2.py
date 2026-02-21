#1
add = lambda a, b: a + b
print(add(3, 5))

#2
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x**2, numbers))
print(result)

#3
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

#4
words = ["apple", "banana", "kiwi"]

result = sorted(words, key=lambda x: len(x))
print(result)