import re 

txt=input()
sam=input()
if re.search(sam, txt):
    print("Yes")
else:       
    print("No")