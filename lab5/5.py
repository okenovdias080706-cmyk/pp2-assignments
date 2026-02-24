import re
txt=input()

if re.match(r"^[A-Za-z].*\d$",txt):
    print("Yes")
else:
    print("No")