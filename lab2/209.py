x=int(input())
a=list(map(int,input().split()))

ma=max(a)
mi=min(a)
for i in range(x):
    if a[i]==ma:
        a[i]=mi
print(*a)