"""
PROBLEM STATEMENT

Read a number and check if it is odd or even

Sample Input 0

5

Sample Output 0

odd

Explanation 0

5 is an odd number therefore output is "odd"

Sample Input 1

2

Sample Output 1

even

Explanation 1

2 is an even number therefore output is "even"
"""

#SOLUTION

n = int(input())
if (n % 2)!= 0:
    print("odd")
else:
    print("even")