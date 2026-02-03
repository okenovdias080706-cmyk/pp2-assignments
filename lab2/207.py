x=int(input())
a=list(map(int,input().split()))

max=a[0]
poz=1
for i in range(x):
    if a[i]>max:
        max=a[i]
        poz=i+1
print(poz)