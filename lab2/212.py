x=int(input())
a=list(map(int,input().split()))
for i in range(x):
    a[i]=a[i]*a[i]
print(*a)