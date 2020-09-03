from itertools import combinations

N = int(input())
DATA = input().split()
M = int(input())

C = list(combinations(DATA, M))
F = filter(lambda c: 'a' in c, C)
print('{0:.3f}'.format(len(list(F)) / len(C)))