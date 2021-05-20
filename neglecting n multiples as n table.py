#missing 5,10,15,20 multiples for 5 table
n=int(input())#1 10
for i in range(1,51):#(low lim,upp lim,inc or dec)
    if i%n==0:
        continue
    print(n,"*",i,"=",n*i)
