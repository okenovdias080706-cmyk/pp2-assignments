#1
import re

text = "I have 2 apples"
cod=re.search("\\d", text)
if cod:
    print("Found a number:", cod.group())

#2
import re

text = "My email is test@mail.com"
x = re.search("@", text)
print(x)

#3
import re

text = "apple,banana,orange"
x = re.split(",", text)

print(x)

#4
import re

text = "I like cats"
x = re.sub("cats", "dogs", text)

print(x)

#5
import re

text = "world Hello"

x = re.match("Hello", text)
print(x)

#6
import re

text = "HELLO"

x = re.search("hello", text, re.IGNORECASE)
print(x)