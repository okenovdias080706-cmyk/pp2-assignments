import sys
input = sys.stdin.readline
n = int(input())
doc = {}
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "set":
        doc[cmd[1]] = cmd[2]
    else:
        key = cmd[1]
        if key in doc:
            print(doc[key])
        else:
            print(f"KE: no key {key} found in the document")
