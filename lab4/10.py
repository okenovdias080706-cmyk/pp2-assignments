def limited_cycle(lst, k):
    for _ in range(k):
        for item in lst:
            yield item

lst = input().split()
k = int(input())

print(*limited_cycle(lst, k))