#missing 3 multiples
n,m=map(int,input().split())#1 10
for i in range(n,m+1):#(low lim,upp lim,inc or dec)
    if i%3==0:
        continue
    print(i,end=" ")
