import re
text = "My number is 456"
# ['4', '5', '6']
print(re.findall("\d", text))
# ['My', 'number', 'is', '456']
print(re.findall("\w+", text))
# spaces
print(re.findall("\s", text))

#Sets & Character Classes
print(re.findall("[abc]", "apple banana cherry"))

print(re.findall("[a-zA-Z]", "Hello123"))
print(re.findall("[0-9]", "Hello123"))

print(re.findall("[^0-9]", "Hello123"))

print(re.findall("\d{3}", "123 4567 89"))   
print(re.findall("\d{2,}", "1 12 123 1234"))
print(re.findall("\d{2,4}", "1 12 123 1234 12345"))