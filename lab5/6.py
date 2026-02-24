import re

txt=input()
if re.search("@",txt):
    print(txt)
else:
    print("No email")