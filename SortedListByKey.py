
"""
You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.

image

Note that  is indexed from  to , where  is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format

The first line contains  and  separated by a space.
The next  lines each contain  elements.
The last line contains .

Constraints



Each element 

Output Format

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.
"""

N, M = input().split()

workingList = []
for i in range(int(N)):
    workingList.append(list(map(int, input().split())))
K = int(input())

_list = sorted(workingList, key=lambda x: x[K])
for i in _list:
    print(*[j for j in i])