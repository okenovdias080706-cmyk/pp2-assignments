import re

txt=input()
sam=input()
count=0
if re.findall(sam, txt):
        for i in re.findall(sam, txt):
              count+=1
print(count)