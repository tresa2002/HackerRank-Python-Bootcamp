"""
PROBLEM STATEMENT

Read a list and print the number of elements divisible by 3.

Input Format

First line contains n the number of elements in the list. The following n lines contains the elements of the list.

Sample Input 0

5
1
7
3
6
5

Sample Output 0

2

Explanation 0

First line 5 is the number of elements in the list. The following 5 lines contains the elements of the list. Here 3 and 6 is divisible by 3. Hence the output is 2.
"""

#SOLUTION

list1=[]
x=0
n=int(input())
for i in range(1,n+1):
    ele=int(input())
    list1.append(ele)
for j in list1:
    if(j%3==0):
        x=x+1
print(x) 