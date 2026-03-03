import re

text = "Hello 123"

# .
print(re.findall("H.llo", text))

# *
print(re.findall("l*", text))

# +
print(re.findall("l+", text))

# ^
print(re.findall("^Hello", text))

# $
print(re.findall("123$", text))         

# []
print(re.findall("[aeiou]", text))

# |
print(re.findall("Hello|Hi", text))