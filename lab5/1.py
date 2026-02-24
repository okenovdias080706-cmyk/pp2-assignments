import re

txt=input()
if re.match("^Hello", txt):
    print("Yes")
else:    
    print("No")