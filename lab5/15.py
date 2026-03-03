import re

txt = input()
def double_digit(match):
    digit = match.group()
    return digit * 2
result = re.sub(r'\d', double_digit, txt)
print(result)