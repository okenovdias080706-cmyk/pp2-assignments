n = int(input())

count_dict = {}
for _ in range(n):
    phone = input()
    if phone in count_dict:
        count_dict[phone] += 1
    else:
        count_dict[phone] = 1
result = 0
for val in count_dict.values():
    if val == 3:
        result += 1

print(result)
