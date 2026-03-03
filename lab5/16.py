import re

s = input()
pattern = r'Name:\s*(.+),\s*Age:\s*(.+)'
match = re.search(pattern, s)
if match:
    name = match.group(1)
    age = match.group(2)
    print(name, age)