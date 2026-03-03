import re

txt=input()
result=re.findall(r"[A-Z]",txt)
print(len(result))