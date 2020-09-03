N = input()
A = set(map(int, input().split()))
for _ in range(int(input())):
    inp = input().split()
    getattr(A, inp[0])(*[int(inp[1])] if len(inp) > 1 else [])
print(sum(A))