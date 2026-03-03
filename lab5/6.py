import re

txt = input()
pattern = r"\S+@\S+\.\S+"
match = re.search(pattern, txt)
if match:
    print(match.group())
else:
    print("No email")