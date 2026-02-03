n = int(input())
a = {}

for _ in range(n):
    s, k = input().split()
    k = int(k)
    if s in a:
        a[s] += k
    else:
        a[s] = k
for s in sorted(a):
    print(s,a[s])
