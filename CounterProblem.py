
"""
Task

Rahgu is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.
"""

from collections import Counter

N = int(input())

SHOES = input().split()
myList = Counter(SHOES)

C = int(input())
amount = 0

for i in range(C):
    X, Y = input().split()
    if myList[str(X)] >= 1:
        amount += int(Y)
        myList[str(X)] = myList[str(X)] - 1
print(amount)    