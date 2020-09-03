from collections import Counter

N = int(input())
K = list(map(int, input().split()))
 
print('{0:.1f}'.format(sum(K) / N)) # Mean

ind1, ind2 = 0, 0
if N % 2 == 0:
    ind1, ind2 = N // 2, (N // 2) - 1
else:
    ind1, ind2 = N // 2, (N // 2) + 1

K = sorted(K)
print('{0:.1f}'.format((K[ind1] + K[ind2]) / 2)) # Median

A = Counter(K).most_common(1)
print(A[0][0]) # Mode