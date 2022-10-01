"""
PROBLEM STATEMENT

Read n from input and print the first N odd numbers

Sample Input 0

3

Sample Output 0

1
3
5
"""

#SOLUTION

n = int(input("Enter the range: "))
for i in range(1,n+1,2):
    print(i)
