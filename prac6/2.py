#1
import os
if os.path.exists("example.txt"):
  os.remove("example.txt")
else:
  print("The file does not exist")