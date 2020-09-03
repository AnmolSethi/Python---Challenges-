N = int(input().strip())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))
    
LD, RD = 0, 0
for i in range(N):
    for j in range(N):
        if i == j:
            LD += arr[i][j]
        if (i + j) == (N - 1):
            RD += arr[i][j]
print(abs(LD - RD))