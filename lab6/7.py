n=int(input())
word=list(map(str,input().split()))
maxi=word[0]
for i in word:
    if len(i)>len(maxi):
        maxi=i
print(maxi)