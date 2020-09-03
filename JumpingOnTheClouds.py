from itertools import groupby

M = input().split()

DATA = [(len(list(c)), int(k)) for k, c in groupby(M)]
JUMPS = 0
for i in DATA:
    if i[1] == 0:
        JUMPS += i[0]//2
    else:
        JUMPS += 1
print(JUMPS)