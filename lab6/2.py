n=int(input())
number=list(map(int,input().split()))
count=0
for i in number:
    if i%2==0:
        count+=1
print(count)