"""
PROBLEM STATEMENT

Read N from input and print the sum of first N Natural Numbers.

Sample Input 0

5

Sample Output 0

15

Explanation 0

N is 5, Therefore sum of first 5 natural numbers is 1 + 2 + 3 + 4 + 5 = 15
"""

#SOLUTION

N = int(input())
i=0
current=1
sum=0
while(i<N):
    sum+=current
    current+=1
    i+=1
print(sum)





