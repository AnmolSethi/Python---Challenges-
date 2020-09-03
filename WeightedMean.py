input()
X = list(map(int, input().split()))
W = list(map(int, input().split()))

A = list()
for i in range(len(X)):
    A.append(X[i] * W[i])
print('{0:.1f}'.format(sum(A) / sum(W)))