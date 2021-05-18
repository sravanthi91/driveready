#Write A Program to find the Largest digit in a given number and display output as given below.#

"""
Example: 
Input- 1987
Output- 9
For example:
Test	Input	Result
1       1987      9
2       5463      6



"""
n=int(input())
large=0
while(n):
    r=n%10
    if(large<r):
        large=r
    n=n//10
    
print(large)        
