"""
PROBLEM STATEMENT

Read N from input and print the first N odd numbers

Sample Input 0

3

Sample Output 0

1
3
5
"""

#SOLUTION

N = int(input())
i = 0
current = 1
while(i<N):
    print(current)
    current+=2
    i+=1