import re

txt = input()
words = re.findall(r'\b[A-Za-z]{3}\b', txt)
print(len(words))