A = set(map(int, input().split()))

sets = list()
for _ in range(int(input())):
    cmd = set(map(int, input().split()))
    sets.append(cmd)

isFinished = list()
for i in range(len(sets)):
    if len(A) > len(sets[i]):
        if not A.issuperset(sets[i]):
            print('False')
            exit()
print('True')