import re

txt=input()
if re.search("^Hello", txt):
    print("Yes")
else:    
    print("No")