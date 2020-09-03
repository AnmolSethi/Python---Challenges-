input()
A = set(map(int, input().split()))
input()
B = set(map(int, input().split()))

print(*[item for item in sorted(list(A.symmetric_difference(B)))], sep='\n')