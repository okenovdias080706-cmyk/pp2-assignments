import re

text = "I have 2 apples"
cod=re.search("\\d", text)
if cod:
    print("Found a number:", cod.group())