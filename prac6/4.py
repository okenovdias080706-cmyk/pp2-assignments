from functools import reduce

nums = [1, 2, 3, 4, 5]

# map → квадрат
squared = list(map(lambda x: x**2, nums))
print(squared)

# filter → тек тақ сандар
odd = list(filter(lambda x: x % 2 != 0, nums))
print(odd)

# reduce → қосынды
total = reduce(lambda x, y: x + y, nums)
print(total)

# enumerate → индекс + мән
print("Enumerate:")
for i, val in enumerate(nums):
    print(i, val)

# zip → біріктіру
names = ["Ali", "Dias", "Aruzhan"]
scores = [80, 90, 85]

print("Zip:")
for name, score in zip(names, scores):
    print(name, score)

# type тексеру және түрлендіру
x = "100"
print(type(x))

x = int(x)
print(type(x))

print("Нәтижелер:")
print("Squared:", squared)
print("Odd:", odd)
print("Total:", total)