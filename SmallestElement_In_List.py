"""
PROBLEM STATEMENT

Read a list and print the smallest element.

Input Format

First line contains n the number of elements in the list. The following n lines contains the elements of the list.

Sample Input 0

5
8
4
7
4
5

Sample Output 0

4

Explanation 0

First line 5 is the number of elements in the list. The following 5 lines contains the elements of the list. The smallest element in the list is 4. Hence the output is 4.
"""

#SOLUTION

list1=[]
n=int(input())
for i in range(1,n+1):
    ele= int(input())
    list1.append(ele)
print(min(list1))






