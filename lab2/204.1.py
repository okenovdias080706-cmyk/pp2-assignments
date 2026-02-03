x=int(input())
a=input().split()

count=0
for i in range(x):
    if int(a[i])>0:
        count+=1
print(count)