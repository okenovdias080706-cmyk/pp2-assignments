n = int(input())
a = [input().strip() for _ in range(n)]

x = {}
for i, s in enumerate(a):
    if s not in x:
        x[s] = i + 1

for s in sorted(x):
    print(s,x[s])