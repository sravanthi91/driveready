"""program for splitting input"""

n=int(input())
while(n!=0):
    r=n%10
    n=n//10
    print(r,n)

