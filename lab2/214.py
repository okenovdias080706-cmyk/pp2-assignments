n = int(input())
a = list(map(int, input().split()))

best = a[0]
best_count = 0
for x in a:
    cnt = 0
    for y in a:
        if x == y:
            cnt += 1

    if cnt > best_count or (cnt == best_count and x < best):
        best = x
        best_count = cnt

print(best)
