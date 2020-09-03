N = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))

S = []
for i in range(N):
    for j in range(F[i]):
        S.append(X[i])

workingData = sorted(S)
if len(workingData) % 2 == 0:
    UB = (len(workingData) // 2, len(workingData))
else:
    UB = (len(workingData) // 2 + 1, len(workingData))
    
LB = (0, len(workingData) // 2) 
A, B = workingData[LB[0]:LB[1]], workingData[UB[0]:UB[1]]

NUM = len(A)
if NUM % 2 == 0:
    Q1 = (A[NUM // 2 - 1] + A[NUM // 2]) / 2
    Q3 = (B[NUM // 2 - 1] + B[NUM // 2]) / 2
else:
    Q1 = A[NUM // 2]
    Q3 = B[NUM // 2]
print(round(float(Q3 - Q1), 1))