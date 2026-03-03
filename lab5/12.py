import re

txt = input()
matches = re.findall(r'\d{2,}', txt)
print(" ".join(matches))