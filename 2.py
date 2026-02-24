x=list(map(int,input().split()))
orta=sum(x)/len(x)

count=0
for i in x:
    if i<orta:
        count+=1
print(count)