import re

txt=input()
word=input()
ment=input()
result=re.sub(word,ment,txt)
print(result)